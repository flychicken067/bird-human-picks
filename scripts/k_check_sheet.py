#!/usr/bin/env python3
"""Write a contact sheet of a fixed random sample of selected photos for an eye check.

Usage: k_check_sheet.py <picks.csv> <out.html> <n>
"""
import csv
import html
import random
import sys

rows = sorted(csv.DictReader(open(sys.argv[1], encoding="utf-8")), key=lambda r: r["id"])
random.Random(20261106).shuffle(rows)
cells = "".join(f'<figure><img src="{html.escape(r["photo"], quote=True)}" alt=""><figcaption>{i} {html.escape(r["chinese"] or r["english"])} · {html.escape(r["scientific_name"])}</figcaption></figure>'
                for i, r in enumerate(rows[:int(sys.argv[3])], 1))
open(sys.argv[2], "w", encoding="utf-8").write(
    '<!doctype html><meta charset="utf-8"><title>Photo check</title><style>body{margin:6px;font:11px sans-serif;background:#fff;color:#111}'
    '.g{display:grid;grid-template-columns:repeat(5,1fr);gap:5px}figure{margin:0}img{width:100%;height:118px;object-fit:contain;background:#eee;display:block}'
    'figcaption{white-space:nowrap;overflow:hidden}</style><div class="g">' + cells + "</div>")
