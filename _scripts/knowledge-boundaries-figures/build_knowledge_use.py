#!/usr/bin/env python3
"""Knowledgeable-R1: three training views and a precisely scoped Table 2 result."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets/img/project/knowledge-boundaries/knowledgeable-r1.svg"
BLUE, INK, MUTED, LINE = "#0076df", "#253d4e", "#627785", "#d8e3eb"
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="520" viewBox="0 0 1180 520" role="img" aria-labelledby="title desc">',
         '<title id="title">Knowledgeable-R1: learn from three views of the same question</title>',
         '<desc id="desc">Left: PK generates an answer from the question; CK generates with context; RPK scores the same PK answer under context. Rewards are compared jointly. Right: Table 2, Qwen2.5-7B-Instruct on ConFiQA-MC with incorrect context: query only 25.82%, RAG 8.06%, GRPO with RAG 19.74%, Knowledgeable-R1 37.34%.</desc>',
         '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="#8aa5b7"/></marker></defs>',
         '<rect width="1180" height="520" fill="#fff"/>',
         '<g font-family="Arial, Helvetica, sans-serif">']

def text(x, y, value, size=17, color=INK, weight="normal", anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

def line(x1, y1, x2, y2, color=LINE, width=1, arrow=False):
    marker = ' marker-end="url(#arrow)"' if arrow else ''
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{marker}/>')

text(30, 41, "One question. Three training views.", 26)
text(30, 72, "Learn how to use knowledge under different evidence conditions.", 16, MUTED)
line(752, 27, 752, 472)

rows = [
    (145, "PK", "Question", "Sample a parametric answer", BLUE),
    (244, "CK", "Question + context", "Sample a context-aware answer", "#628d9f"),
    (343, "RPK", "Question + context", "Score the same PK answer", "#377c70"),
]
for y, label, prompt, behavior, color in rows:
    parts.append(f'<rect x="30" y="{y-39}" width="49" height="49" rx="24.5" fill="{color}" fill-opacity=".09"/>')
    text(54.5, y-9, label, 15, color, "bold", "middle")
    text(96, y-14, prompt, 18)
    text(96, y+14, behavior, 15, MUTED)
    line(363, y-10, 446, y-10, "#8aa5b7", 1.8, True)
parts.append('<path d="M453 135 L475 135 L475 333 L453 333" fill="none" stroke="#8aa5b7" stroke-width="1.5"/>')
text(502, 196, "Compare rewards", 20)
text(502, 226, "Local + global", 16, MUTED)
text(502, 250, "advantages", 16, MUTED)
line(578, 271, 578, 305, "#8aa5b7", 1.8, True)
text(502, 338, "Update the policy", 19, BLUE)
line(30, 397, 710, 397)
text(30, 433, "Use helpful evidence. Resist misleading context.", 20, BLUE)
text(30, 465, "RPK reuses the PK trajectory; it does not sample a separate answer.", 13, MUTED)

text(792, 41, "When the context is wrong", 24)
text(792, 72, "Qwen2.5-7B-Instruct / ConFiQA-MC", 15, MUTED)
text(792, 97, "Accuracy (%) · Table 2, scenario S2", 14, MUTED)
baseline, top = 391, 145
for tick in [0, 20, 40]:
    y = baseline - tick/40*(baseline-top)
    line(810, y, 1145, y)
    text(801, y+5, str(tick), 12, MUTED, anchor="end")
values = [
    (846, 25.82, "Query", "only", "#8aa5b7"),
    (928, 8.06, "RAG", "", "#ad654d"),
    (1010, 19.74, "GRPO", "w/ RAG", "#607b8c"),
    (1092, 37.34, "Knowledgeable", "-R1", BLUE),
]
for x, value, first, second, color in values:
    height=value/40*(baseline-top)
    parts.append(f'<rect x="{x-22}" y="{baseline-height:.3f}" width="44" height="{height:.3f}" fill="{color}" rx="2"/>')
    text(x, baseline-height-13, f"{value:.2f}", 19, color, "bold", "middle")
    text(x, 419, first, 12, INK, anchor="middle")
    text(x, 438, second, 12, INK, anchor="middle")
text(792, 479, "A result for this test setting, not a universal guarantee.", 12, MUTED)
parts.append('</g></svg>\n')
OUT.write_text('\n'.join(parts))
print(OUT)
