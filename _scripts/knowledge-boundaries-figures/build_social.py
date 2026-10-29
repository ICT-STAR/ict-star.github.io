#!/usr/bin/env python3
"""Render the research page's 1200x630 social image using Node.js and sharp."""

import argparse
from pathlib import Path
import subprocess


SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#f1f6fa"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="72" y="68" font-size="19" letter-spacing="3" fill="#506b80">STAR GROUP / RESEARCH</text>
<path d="M72 96H1128" stroke="#cbdde9"/>
<text x="72" y="196" font-size="62" letter-spacing="-2" fill="#243f53">From latent knowledge</text>
<text x="72" y="272" font-size="62" letter-spacing="-2" fill="#0076df">to reliable answers.</text>
<text x="72" y="335" font-size="25" fill="#506b80">Knowledge boundaries, uncertainty, and reliable generation</text>
<path d="M138 443H1058" stroke="#9bbdd4" stroke-width="2"/>
<g fill="#f1f6fa" stroke="#0076df" stroke-width="2"><circle cx="138" cy="443" r="19"/><circle cx="550" cy="443" r="19"/><circle cx="962" cy="443" r="19"/></g>
<g fill="#0076df"><circle cx="138" cy="443" r="5"/><circle cx="550" cy="443" r="5"/><circle cx="962" cy="443" r="5"/></g>
<g font-size="22" fill="#243f53"><text x="72" y="499">Access knowledge</text><text x="462" y="499">Assess reliability</text><text x="874" y="499">Choose a response</text></g>
<path d="M72 549H1128" stroke="#cbdde9"/>
<text x="72" y="589" font-size="18" fill="#506b80">8 studies / 2024–2026</text><text x="1128" y="589" text-anchor="end" font-size="18" fill="#506b80">ict-star.github.io</text>
</g></svg>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sharp-module', default='sharp', help='sharp module name or absolute module directory')
    args = parser.parse_args()
    output = Path(__file__).resolve().parents[2] / 'assets/img/project/cover/knowledge-boundaries-social.png'
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        'node', '-e',
        'const sharp=require(process.argv[1]);let chunks=[];process.stdin.on("data",c=>chunks.push(c));process.stdin.on("end",()=>sharp(Buffer.concat(chunks)).png().toFile(process.argv[2]).catch(e=>{process.stderr.write(e.message);process.exitCode=1}));',
        args.sharp_module, str(output),
    ], input=SVG.encode('utf-8'), check=True)
    print(output)


if __name__ == '__main__':
    main()
