#!/usr/bin/env python3
"""Stack the original Fig. 5 panels without redrawing curves, axes, or text."""
from copy import deepcopy
from pathlib import Path
import subprocess

from pypdf import PageObject, PdfReader, PdfWriter, Transformation
from pypdf.generic import DecodedStreamObject, NameObject, RectangleObject

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets/img/project/knowledge-boundaries"
SOURCE = ASSETS / "results-beyond-reasoning-fig5.pdf"
OUTPUT = ASSETS / "beyond-reasoning-fig5-stacked.pdf"
WIDTH, HEIGHT = 500, 1023.0825

# Source SVG coordinates: x, y, width, height; destination: x, y.
# Shared dataset/metric labels move to the HTML caption. Keep the common
# sample-budget label only beneath the last panel, and pad both sides evenly.
PANELS = (
    ((525, 5, 310, 30), (95, 12)),
    ((74, 37, 426, 297), (37, 54)),
    ((508.252761, 37, 426, 297), (37, 365)),
    ((942.505522, 37, 426, 331.0825), (37, 676)),
)


def main():
    original = PdfReader(SOURCE).pages[0]
    source_height = float(original.mediabox.height)
    result = PageObject.create_blank_page(width=WIDTH, height=HEIGHT)
    background = DecodedStreamObject()
    background.set_data(f"q 1 1 1 rg 0 0 {WIDTH} {HEIGHT} re f Q\n".encode())
    result[NameObject("/Contents")] = background
    for (x, y, width, height), (dest_x, dest_y) in PANELS:
        bounds = RectangleObject((x, source_height-y-height, x+width, source_height-y))
        panel = deepcopy(original)
        panel.mediabox = panel.cropbox = bounds
        if "/Annots" in panel:
            del panel["/Annots"]
        dx = dest_x - x
        dy = HEIGHT - dest_y - height - float(bounds.bottom)
        result.merge_transformed_page(panel, Transformation().translate(dx, dy))
    writer = PdfWriter()
    writer.add_page(result)
    writer.add_metadata({"/Title": "Beyond Reasoning — Figure 5, vertically arranged"})
    writer.write(OUTPUT)
    subprocess.run(["pdftocairo", "-svg", str(OUTPUT), str(OUTPUT.with_suffix(".svg"))], check=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
