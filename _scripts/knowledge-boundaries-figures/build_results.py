#!/usr/bin/env python3
"""Build direct result figures from verified values and original paper artwork."""

import argparse
import json
from pathlib import Path
import subprocess
from xml.sax.saxutils import escape

from pypdf import PageObject, PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "assets/img/project/knowledge-boundaries"
BLUE = "#0076df"
RUST = "#ad654d"
INK = "#223746"
MUTED = "#607180"
LINE = "#dde5eb"


def detection_figure(data):
    """Five methods, one fixed scale; labels reproduce all Table 2 values."""
    shapes = []

    def text(x, y, label, size=17, color=INK, weight="normal", anchor="start"):
        shapes.append(("text", dict(x=x, y=y, label=label, size=size,
                                    color=color, weight=weight, anchor=anchor)))

    def line(x1, y1, x2, y2, color=LINE, width=1, dash=None):
        shapes.append(("line", dict(x1=x1, y1=y1, x2=x2, y2=y2,
                                    color=color, width=width, dash=dash)))

    def circle(x, y, color, radius=6):
        shapes.append(("circle", dict(x=x, y=y, color=color, radius=radius)))

    shapes.append(("rect", dict(x=0, y=0, width=1100, height=560, color="#ffffff")))
    text(28, 40, "Self-consistent errors are harder to detect", 28)
    text(28, 69, "Qwen2.5-7B-Instruct / TriviaQA", 16, MUTED)
    circle(306, 106, BLUE, 5)
    text(320, 112, "Inconsistent errors", 16, BLUE)
    circle(590, 106, RUST, 5)
    text(604, 112, "Self-consistent errors", 16, RUST)

    left, right = 305, 1050
    x = lambda value: left + (value - 0.4) / 0.6 * (right - left)
    for tick in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        line(x(tick), 136, x(tick), 475,
             MUTED if tick == 0.5 else LINE,
             1.4 if tick == 0.5 else 1,
             "5 6" if tick == 0.5 else None)
        text(x(tick), 502, f"{tick:.1f}", 15, MUTED, anchor="middle")

    for index, row in enumerate(data["self_consistent_errors"]["rows"]):
        y = 170 + index * 70
        if row["id"] == "semantic_entropy":
            shapes.append(("rect", dict(x=17, y=y - 32, width=1066,
                                        height=66, color="#fbf3ef")))
            line(x(0.5), y - 32, x(0.5), y + 34, MUTED, 1.4, "5 6")
        text(28, y - 1, row["label"], 18,
             RUST if row["id"] == "semantic_entropy" else INK,
             "bold" if row["id"] == "semantic_entropy" else "normal")
        text(28, y + 20, row["training"], 12, MUTED)
        line(x(row["consistent"]), y, x(row["inconsistent"]), y,
             "#c8d5df", 3)
        circle(x(row["inconsistent"]), y, BLUE)
        circle(x(row["consistent"]), y, RUST)
        text(x(row["inconsistent"]), y - 14, f'{row["inconsistent"]:.4f}',
             15, BLUE, anchor="middle")
        text(x(row["consistent"]), y + 27, f'{row["consistent"]:.4f}',
             15, RUST, anchor="middle")

    text(28, 540, "AUROC: higher is better", 14, MUTED)
    text(x(0.5), 540, "0.5 = chance", 14, MUTED, anchor="middle")
    text(1072, 540, "Table 2 / EMNLP 2025", 13, MUTED, anchor="end")
    return shapes


def detection_mobile(data):
    """Keep each method and its complete paired comparison legible on phones."""
    shapes = [("rect", dict(x=0, y=0, width=440, height=760, color="#ffffff"))]

    def text(x, y, label, size=18, color=INK, weight="normal", anchor="start"):
        shapes.append(("text", dict(x=x, y=y, label=label, size=size,
                                    color=color, weight=weight, anchor=anchor)))

    def line(x1, y1, x2, y2, color=LINE, width=1, dash=None):
        shapes.append(("line", dict(x1=x1, y1=y1, x2=x2, y2=y2,
                                    color=color, width=width, dash=dash)))

    def circle(x, y, color, radius=6):
        shapes.append(("circle", dict(x=x, y=y, color=color, radius=radius)))

    text(22, 36, "Consistency can hide errors", 25)
    text(22, 64, "Qwen2.5-7B-Instruct / TriviaQA", 15, MUTED)
    circle(26, 101, BLUE, 5)
    text(39, 107, "Inconsistent errors", 15, BLUE)
    circle(221, 101, RUST, 5)
    text(234, 107, "Self-consistent errors", 15, RUST)
    x = lambda value: 34 + (value - 0.4) / 0.6 * 372

    for index, row in enumerate(data["self_consistent_errors"]["rows"]):
        label_y = 151 + index * 111
        y = label_y + 36
        if row["id"] == "semantic_entropy":
            shapes.append(("rect", dict(x=12, y=label_y - 27, width=416,
                                        height=103, color="#fbf3ef")))
        text(22, label_y, row["label"], 21,
             RUST if row["id"] == "semantic_entropy" else INK,
             "bold" if row["id"] == "semantic_entropy" else "normal")
        text(418, label_y + 1, row["training"], 13, MUTED, anchor="end")
        line(x(0.4), y, x(1.0), y, LINE, 1)
        for tick in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
            line(x(tick), y - 6, x(tick), y + 6)
        line(x(0.5), y - 12, x(0.5), y + 13, MUTED, 1.2, "3 4")
        line(x(row["consistent"]), y, x(row["inconsistent"]), y,
             "#c8d5df", 3)
        circle(x(row["inconsistent"]), y, BLUE)
        circle(x(row["consistent"]), y, RUST)
        text(x(row["inconsistent"]), y - 14, f'{row["inconsistent"]:.4f}',
             18, BLUE, anchor="middle")
        text(x(row["consistent"]), y + 29, f'{row["consistent"]:.4f}',
             18, RUST, anchor="middle")

    for tick in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        text(x(tick), 691, f"{tick:.1f}", 16, MUTED, anchor="middle")
    text(22, 729, "AUROC: higher is better", 15, MUTED)
    text(418, 729, "0.5 = chance", 15, MUTED, anchor="end")
    return shapes


def write_svg(shapes, path, width=1100, height=560):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             '<title id="title">Self-consistent errors are harder to detect</title>',
             '<desc id="desc">Five error-detection methods on Qwen2.5-7B-Instruct and TriviaQA. Blue points show AUROC on inconsistent errors and rust points on self-consistent errors, using the same 0.4 to 1.0 scale. Semantic entropy falls from 0.9119 to 0.4453. Source: Table 2, Too Consistent to Detect, EMNLP 2025.</desc>',
             '<g font-family="Arial, Helvetica, sans-serif">']
    for kind, a in shapes:
        if kind == "text":
            parts.append(f'<text x="{a["x"]:.3f}" y="{a["y"]}" font-size="{a["size"]}" fill="{a["color"]}" font-weight="{a["weight"]}" text-anchor="{a["anchor"]}">{escape(a["label"])}</text>')
        elif kind == "line":
            dash = f' stroke-dasharray="{a["dash"]}"' if a["dash"] else ""
            parts.append(f'<line x1="{a["x1"]:.3f}" y1="{a["y1"]}" x2="{a["x2"]:.3f}" y2="{a["y2"]}" stroke="{a["color"]}" stroke-width="{a["width"]}"{dash}/>')
        elif kind == "circle":
            parts.append(f'<circle cx="{a["x"]:.3f}" cy="{a["y"]}" r="{a["radius"]}" fill="{a["color"]}" stroke="#fff" stroke-width="1.5"/>')
        else:
            parts.append(f'<rect x="{a["x"]}" y="{a["y"]}" width="{a["width"]}" height="{a["height"]}" fill="{a["color"]}" rx="4"/>')
    parts.append("</g></svg>\n")
    path.write_text("\n".join(parts))


def write_pdf(shapes, path):
    pdf = canvas.Canvas(str(path), pagesize=(1100, 560), invariant=1)
    pdf.setTitle("Too Consistent to Detect — Table 2 comparison")
    pdf.setAuthor("STAR Group; plotted from the published Table 2")
    for kind, a in shapes:
        if kind == "text":
            pdf.setFillColor(a["color"])
            pdf.setFont("Helvetica-Bold" if a["weight"] == "bold" else "Helvetica", a["size"])
            draw = {"start": pdf.drawString, "middle": pdf.drawCentredString,
                    "end": pdf.drawRightString}[a["anchor"]]
            draw(a["x"], 560 - a["y"], a["label"])
        elif kind == "line":
            pdf.setStrokeColor(a["color"])
            pdf.setLineWidth(a["width"])
            pdf.setDash([5, 6] if a["dash"] else [])
            pdf.line(a["x1"], 560 - a["y1"], a["x2"], 560 - a["y2"])
        elif kind == "circle":
            pdf.setFillColor(a["color"])
            pdf.setStrokeColor("#ffffff")
            pdf.setLineWidth(1.5)
            pdf.circle(a["x"], 560 - a["y"], a["radius"], fill=1, stroke=1)
        else:
            pdf.setFillColor(a["color"])
            pdf.roundRect(a["x"], 560 - a["y"] - a["height"], a["width"],
                          a["height"], 4, fill=1, stroke=0)
    pdf.save()


def export_original_passk(source):
    # Fig. 5 is a standalone vector Form in arXiv:2605.07153v1, PDF page 7.
    reader = PdfReader(source)
    form = reader.pages[6]["/Resources"]["/XObject"]["/Im5"]
    left, bottom, right, top = map(float, form.get_object()["/BBox"])
    page = PageObject.create_blank_page(width=right - left, height=top - bottom)
    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/XObject"): DictionaryObject({NameObject("/Figure"): form})
    })
    contents = DecodedStreamObject()
    contents.set_data(f"q 1 0 0 1 {-left} {-bottom} cm /Figure Do Q".encode("ascii"))
    page[NameObject("/Contents")] = contents
    writer = PdfWriter()
    writer.add_page(page)
    pdf = OUTPUT / "results-beyond-reasoning-fig5.pdf"
    writer.write(pdf)
    subprocess.run(["pdftocairo", "-svg", str(pdf), str(pdf.with_suffix(".svg"))], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beyond-pdf", required=True, type=Path,
                        help="Original arXiv:2605.07153v1 PDF")
    args = parser.parse_args()
    data = json.loads((ROOT / "_data/knowledge_boundaries.json").read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    shapes = detection_figure(data)
    write_svg(shapes, OUTPUT / "results-too-consistent.svg")
    write_pdf(shapes, OUTPUT / "results-too-consistent.pdf")
    write_svg(detection_mobile(data), OUTPUT / "results-too-consistent-mobile.svg", 440, 760)
    export_original_passk(args.beyond_pdf)
    print("Built the five-method detection comparison and original pass@k figure.")


if __name__ == "__main__":
    main()
