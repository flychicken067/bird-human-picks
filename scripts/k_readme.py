#!/usr/bin/env python3
"""Write README.md and its 10 translations, in the same order of sections as huashu-bird-sticker's README.

Usage: k_readme.py   (run from the repo root, after k_export_data.py and k_previews.py)

Numbers come from data/coverage.json, data/species.json, docs/stats.json, docs/site-stats.json and
previews/credits.json, so every language shows the same, current figures. Text is in scripts/readme_i18n.json.
"""
import json

LANGS = [  # code, file, label, site path
    ("en", "README.md", "English", "en/"), ("zh-Hans", "README.zh-Hans.md", "简体中文", ""), ("zh-Hant", "README.zh-Hant.md", "繁體中文", "zh-hant/"),
    ("ja", "README.ja.md", "日本語", "ja/"), ("ko", "README.ko.md", "한국어", "ko/"), ("es", "README.es.md", "Español", "es/"),
    ("fr", "README.fr.md", "Français", "fr/"), ("de", "README.de.md", "Deutsch", "de/"), ("pt", "README.pt.md", "Português", "pt-br/"),
    ("ru", "README.ru.md", "Русский", "ru/"), ("ar", "README.ar.md", "العربية", "en/"),
]
SITE = "https://flychicken067.github.io/bird-human-picks/"
REPO = "https://github.com/flychicken067/bird-human-picks"
GROUP_ORDER = ["trochilidae", "colourful", "columbidae", "anatidae", "phasianidae", "owls", "raptors", "herons", "shorebirds", "songbirds"]

T = json.load(open("scripts/readme_i18n.json", encoding="utf-8"))
cov = json.load(open("data/coverage.json", encoding="utf-8"))
sp = json.load(open("data/species.json", encoding="utf-8"))["species"]
stats = json.load(open("docs/stats.json", encoding="utf-8"))
site = json.load(open("docs/site-stats.json", encoding="utf-8"))
cr = json.load(open("previews/credits.json", encoding="utf-8"))
f = cov["fields"]
nums = {"n": f"{cov['count']:,}", "orders": len({s["taxonomy"]["order"] for s in sp}), "families": len({s["taxonomy"]["family"] for s in sp}),
        "fetched": f"{stats['fetched_species']:,}", "cc0": sum(1 for s in sp if s["photo"]["license"] == "CC0"), "med_a": site["median_agree"],
        "med_m": site["median_months"], "wd": f"{f['ids.wikidata']:,}", "gbif": f"{f['ids.gbif']:,}", "size": f"{f['size']:,}",
        "fg": f"{cov['fieldGuide']:,}", "removed": site["removed"]}


def fill(s, **extra):
    for k, v in {**nums, **extra}.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def credit_list(photos, t):
    rows = "\n".join(f"{i}. *{p['scientificName']}* — [{p['author']}]({p['page']}), {p['license']}" for i, p in enumerate(photos, 1))
    return f"<details><summary>{t['credits']}</summary>\n\n{rows}\n\n</details>\n"


for code, fname, label, path in LANGS:
    t = T[code]
    links = " · ".join(f"**{l[2]}**" if l[0] == code else f"[{l[2]}]({l[1]})" for l in LANGS)
    site_url = SITE + path
    out = [f"# {t['title']}\n",
           f'<img src="previews/header.jpg" alt="{t["site_alt"]}" width="100%">\n',
           links + "\n",
           f'<a href="{site_url}"><img src="docs/assets/og.png" alt="{t["site_alt"]}" width="100%"></a>\n',
           fill(t["site_para"], site=site_url) + "\n",
           fill(t["intro"]) + "\n",
           "> " + fill(t["status"]) + "\n",
           fill(t["licence"]) + "\n",
           f"## {t['gallery_h']}\n", t["gallery_intro"] + "\n"]
    for key in GROUP_ORDER:
        g = cr["groups"][key]
        fams = " · ".join(f"*{x}*" for x in g["families"] if any(s["taxonomy"]["family"] == x for s in sp))
        out.append(f"### {t['groups'][key]} · {fams} — {t['species'].replace('{n}', str(g['species']))}\n")
        out.append(f"![{t['groups'][key]}](previews/families/{key}.jpg)\n")
        out.append(credit_list(g["photos"], t))
    out.append(f"### {t['orders_h']}\n")
    out.append(f"![{t['orders_h']}](previews/orders.jpg)\n")
    out.append(credit_list(cr["orders"], t))
    out.append(f"## {t['inside_h']}\n")
    out.append("| | |\n|---|---|\n" + "".join(f"| `{k}` | {fill(v)} |\n" for k, v in t["inside"].items()))
    out.append(f"## {t['coverage_h']}\n")
    out.append("".join(f"- {fill(x)}\n" for x in t["coverage"]))
    out.append(f"## {t['quality_h']}\n")
    out += [fill(x) + "\n" for x in t["quality"]]
    out.append("".join(f"- {x}\n" for x in t["limits"]))
    out.append(t["report"] + "\n")
    out.append(f"## {t['removal_h']}\n")
    out.append(t["removal"] + "\n")
    out.append(f"## {t['use_h']}\n")
    out.append(t["use1"] + "\n")
    out.append(t["use2"] + "\n")
    out.append(f"```bash\ngit clone --filter=blob:none --sparse {REPO}\ncd bird-human-picks && git sparse-checkout set data\n```\n")
    out.append(f"## {t['thanks_h']}\n")
    out.append("".join(f"- {x}\n" for x in t["thanks"]))
    out.append(f"\n[BUILD.md](BUILD.md) · [RULES.md](RULES.md) · [PARITY.md](PARITY.md) · [NOTICE.md](NOTICE.md)\n")
    text = "\n".join(out)
    if code == "ar":
        text = '<div dir="rtl">\n\n' + text + '\n</div>\n'
    open(fname, "w", encoding="utf-8").write(text)
    print(fname, len(text))
