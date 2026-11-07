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
R = stats["reasons"]
unsel = sum(v for k, v in R.items() if k != "checked")
raw = {"n": cov["count"], "orders": len({s["taxonomy"]["order"] for s in sp}), "families": len({s["taxonomy"]["family"] for s in sp}),
        "fetched": stats["fetched_species"], "cc0": sum(1 for s in sp if s["photo"]["license"] == "CC0"), "med_a": site["median_agree"],
       "med_m": site["median_months"], "wd": f["ids.wikidata"], "gbif": f["ids.gbif"], "size": f["size"], "fg": cov["fieldGuide"],
       "removed": site["removed"], "all": 11011, "unmatched": 11011 - stats["fetched_species"], "stickers": stats["huashu_stickers"],
       "unsel": unsel, "r_three": R.get("no_three_people_three_months", 0), "r_frame": R.get("framing_not_checked_yet", 0) + R.get("strict_not_checked_yet", 0),
       "r_clear": R.get("no_single_clear_bird", 0) + R.get("photo_too_small", 0), "r_small": R.get("photo_too_small", 0), "r_taxon": R.get("taxon_changed", 0),
       "r_other": R.get("name_not_exact", 0) + R.get("eye_check_species", 0)}
SEP = {"zh-Hans": "", "zh-Hant": "", "en": ",", "ja": ",", "ko": ",", "ar": ",", "es": ".", "de": ".", "pt": ".", "fr": "\u202f", "ru": "\u00a0"}


def fmt(v, lang):
    """Numbers as each language writes them; Chinese like huashu's README: no thousands separator."""
    if not isinstance(v, int) or v < 1000:
        return str(v)
    return f"{v:,}".replace(",", SEP[lang])


def fill(s, lang, **extra):
    for k, v in {**{k: fmt(v, lang) for k, v in raw.items()}, "n_zh": fmt(raw["n"], "zh-Hans"), **extra}.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def credit_list(photos, t):
    rows = "\n".join(f"{i}. *{p['scientificName']}* — [{p['author']}]({p['page']}), {p['license']}" for i, p in enumerate(photos, 1))
    return f"<details><summary>{t['credits']}</summary>\n\n{rows}\n\n</details>\n"


for code, fname, label, path in LANGS:
    t = T[code]
    links = " · ".join(f"**{l[2]}**" if l[0] == code else f"[{l[2]}]({l[1]})" for l in LANGS)
    site_url = SITE + path
    F = lambda x, **kw: fill(x, code, **kw)
    out = [f"# {t['title']}\n",
           f'<img src="previews/header.jpg" alt="{F(t["site_alt"])}" width="100%">\n']
    if t.get("cn_summary"):
        out.append(F(t["cn_summary"]) + "\n")
    out += [links + "\n",
            f'<a href="{site_url}"><img src="docs/assets/og.png" alt="{F(t["site_alt"])}" width="100%"></a>\n',
            F(t["site_para"], site=site_url) + "\n",
            F(t["intro"]) + "\n",
            "> " + F(t["status"]) + "\n",
            F(t["licence"]) + "\n",
            f"## {t['gallery_h']}\n", F(t["gallery_intro"]) + "\n"]
    for key in GROUP_ORDER:
        g = cr["groups"][key]
        fams = " · ".join(f"*{x}*" for x in g["families"] if any(s["taxonomy"]["family"] == x for s in sp))
        out.append(f"### {t['groups'][key]} · {fams} — {t['species'].replace('{n}', fmt(g['species'], code))}\n")
        out.append(f"![{t['groups'][key]}](previews/families/{key}.jpg)\n")
        out.append(credit_list(g["photos"], t))
    out.append(f"### {t['orders_h']}\n")
    out.append(f"![{t['orders_h']}](previews/orders.jpg)\n")
    out.append(credit_list(cr["orders"], t))
    out.append(f"## {t['inside_h']}\n")
    out.append("| | |\n|---|---|\n" + "".join(f"| `{k}` | {F(v)} |\n" for k, v in t["inside"].items()))
    out.append(f"## {t['coverage_h']}\n")
    out.append("".join(f"- {F(x)}\n" for x in t["coverage"]))
    out.append(f"## {t['quality_h']}\n")
    out += [F(x) + "\n" for x in t["quality"]]
    out.append("- " + F(t["unselected"]) + "\n")
    out.append(F(t["disclaimer"]) + " " + F(t["compare"]) + "\n")
    out.append(t["report"] + "\n")
    out.append(f"## {t['removal_h']}\n")
    out.append(t["removal"] + "\n")
    out.append(f"## {t['use_h']}\n")
    out.append(t["use1"] + "\n")
    out.append("```\nhttps://inaturalist-open-data.s3.amazonaws.com/photos/<photoId>/original.jpg\n```\n")
    out.append(t["use1b"] + "\n")
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
