#!/usr/bin/env python3
"""Export the paper's original vector figures, without redrawing their data."""

import argparse
from pathlib import Path
import subprocess

from pypdf import PageObject, PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject, RectangleObject


FIGURES = (
    {
        "name": "original-basecal-fig1",
        "source": "basecal.pdf",
        "page": 0,
        "crop": (305.5, 512, 524, 624),
    },
    {
        "name": "original-taps-fig1",
        "source": "taps-v2.pdf",
        "page": 1,
        "form": "/Im1",
    },
    {
        "name": "original-blinded-fig2",
        "source": "blinded.pdf",
        "page": 2,
        "crop": (70, 632, 524, 773),
    },
)


def extract(figure, source_dir, output_dir):
    reader = PdfReader(source_dir / figure["source"])
    page = reader.pages[figure["page"]]
    if "form" in figure:
        # Fig. 1 is an independent vector Form in the original TAPS PDF.
        # Its original bounding box keeps every axis label and no paper text.
        form = page["/Resources"]["/XObject"][figure["form"]]
        left, bottom, right, top = map(float, form.get_object()["/BBox"])
        page = PageObject.create_blank_page(width=right - left, height=top - bottom)
        page[NameObject("/Resources")] = DictionaryObject({
            NameObject("/XObject"): DictionaryObject({NameObject("/Figure"): form})
        })
        contents = DecodedStreamObject()
        contents.set_data(f"q 1 0 0 1 {-left} {-bottom} cm /Figure Do Q".encode("ascii"))
        page[NameObject("/Contents")] = contents
    else:
        page.mediabox = RectangleObject(figure["crop"])
        page.cropbox = RectangleObject(figure["crop"])
        if "/Annots" in page:
            del page["/Annots"]
    writer = PdfWriter()
    writer.add_page(page)
    pdf = output_dir / f"{figure['name']}.pdf"
    writer.write(pdf)
    subprocess.run(["pdftocairo", "-svg", str(pdf), str(pdf.with_suffix(".svg"))], check=True)
    print(f"Exported {figure['name']} ({float(page.mediabox.width):g} × {float(page.mediabox.height):g} pt)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path,
                        help="Directory containing basecal.pdf, taps-v2.pdf, and blinded.pdf")
    args = parser.parse_args()
    output_dir = Path(__file__).resolve().parents[2] / "assets/img/project/knowledge-boundaries"
    output_dir.mkdir(parents=True, exist_ok=True)
    for figure in FIGURES:
        extract(figure, args.source_dir, output_dir)


if __name__ == "__main__":
    main()
