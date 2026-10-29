#!/usr/bin/env python3
"""Export a readable, linked Markdown overview from the publication registry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
catalog = json.loads((ROOT / "_data/knowledge_publications.json").read_text())
page = "https://ict-star.github.io/projects/knowledge_boundaries/"
lines = [
    f"# {catalog['name']}", "", "STAR Group · Knowledge Boundaries & Uncertainty",
    "", f"Canonical project page: {page}", f"Last checked: {catalog['checked_on']}", "",
    "## Research questions", "",
    "We study how language models can recall more of their existing knowledge, assess answer reliability, and use evidence or abstain appropriately. The studies form a shared research agenda, rather than a single integrated system.", "",
    "- Access: improve factual recall and understand knowledge accessibility.",
    "- Assess: study confidence alignment, reference signals, and fact-level judgments.",
    "- Act: resist misleading context and control selective answering.", "",
    "Calibration, answer accuracy, error discrimination, and selective risk are distinct evaluation dimensions. A failed answer or a finite sample budget does not prove that knowledge is absent.",
    "", "## Papers and primary sources", "",
]
for paper in catalog["papers"]:
    lines += [f"### {paper['title']}", "", ", ".join(paper["authors"]) + ".", "",
              f"{paper['venue']} · {paper['status']} · {paper['version']}", "", paper["summary"], "",
              f"- Primary paper: {paper['url']}", f"- PDF: {paper['pdf']}",
              f"- Research summary: {page}#{paper['id']}"]
    for key, label in [("doi", "DOI"), ("code", "Code"), ("project", "Project"), ("preprint", "Author preprint")]:
        if paper.get(key):
            value = "https://doi.org/" + paper[key] if key == "doi" else paper[key]
            lines.append(f"- {label}: {value}")
    lines.append("")
output = ROOT / "assets/research/knowledge-boundaries.md"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text("\n".join(lines))
print(output)
