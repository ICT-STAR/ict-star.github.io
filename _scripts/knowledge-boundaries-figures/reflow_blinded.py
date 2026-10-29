#!/usr/bin/env python3
"""Move the original Fig. 2(c) below (a,b), preserving all vector artwork."""
from copy import deepcopy
from pathlib import Path
import subprocess

from pypdf import PageObject, PdfReader, PdfWriter, Transformation
from pypdf.generic import DecodedStreamObject, NameObject, RectangleObject

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets/img/project/knowledge-boundaries"
SOURCE = ASSETS / "original-blinded-fig2.pdf"
OUTPUT = ASSETS / "blinded-fig2-stacked.pdf"

# Coordinates refer to the original page; no panel is scaled or redrawn.
# AB remains at the top, and C is centered beneath it with a 10 pt gap.
PANELS = (
    ((70, 632, 298, 773), (0, 122)),
    ((308, 646, 524, 758), (6, 0)),
)


def main():
    original = PdfReader(SOURCE).pages[0]
    result = PageObject.create_blank_page(width=228, height=263)
    background = DecodedStreamObject()
    background.set_data(b"q 1 1 1 rg 0 0 228 263 re f Q\n")
    result[NameObject("/Contents")] = background
    for bounds, position in PANELS:
        panel = deepcopy(original)
        panel.mediabox = panel.cropbox = RectangleObject(bounds)
        if "/Annots" in panel:
            del panel["/Annots"]
        dx, dy = position[0] - bounds[0], position[1] - bounds[1]
        result.merge_transformed_page(panel, Transformation().translate(dx, dy))
    writer = PdfWriter()
    writer.add_page(result)
    writer.add_metadata({"/Title": "Blinded by Generated Contexts — Figure 2, vertically arranged"})
    writer.write(OUTPUT)
    subprocess.run(["pdftocairo", "-svg", str(OUTPUT), str(OUTPUT.with_suffix(".svg"))], check=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
