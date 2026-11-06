#!/usr/bin/env python3
"""Build the public site in docs/: a home page, one page per species and a method page, in 15 languages.

Usage: build_site.py <picks.csv> <eye-check.csv> <huashu species.json> <huashu field-guide.zh-Hans.json> <huashu commit> <docs_dir> [photo_cache_dir]

picks.csv comes from scripts/k_build_select.py. The huashu files are data from
https://github.com/alchaincyf/huashu-bird-sticker at <huashu commit> (taxonomy, names, size, status: MIT;
names: AviList CC BY 4.0 / IOC CC BY 3.0; Chinese field notes: CC BY-SA 4.0).
The optional photo cache (sha1(photo_url).jpg) is used to draw the share image from CC0 photos only.
"""
import csv
import hashlib
import html
import json
import os
import re
import shutil
import statistics
import sys
import unicodedata
import urllib.parse

SITE = "https://flychicken067.github.io/bird-human-picks/"
REPO = "https://github.com/flychicken067/bird-human-picks"
HERE = os.path.dirname(os.path.abspath(__file__))
# code, url prefix, html lang, key in huashu names, label
LANGS = [
    ("zh-Hans", "", "zh-CN", "zh-Hans", "简体中文"),
    ("en", "en/", "en", "en", "English"),
    ("zh-Hant", "zh-hant/", "zh-TW", "zh-Hant", "繁體中文"),
    ("ja", "ja/", "ja", "ja", "日本語"),
    ("ko", "ko/", "ko", "ko", "한국어"),
    ("de", "de/", "de", "de", "Deutsch"),
    ("fr", "fr/", "fr", "fr", "Français"),
    ("es", "es/", "es", "es", "Español"),
    ("pt-br", "pt-br/", "pt-BR", "pt-x-lusophone", "Português"),
    ("it", "it/", "it", "it", "Italiano"),
    ("nl", "nl/", "nl", "nl", "Nederlands"),
    ("ru", "ru/", "ru", "ru", "Русский"),
    ("sv", "sv/", "sv", "sv", "Svenska"),
    ("da", "da/", "da", "da", "Dansk"),
    ("pl", "pl/", "pl", "pl", "Polski"),
]
e = html.escape


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def clean_credit(c):
    """'(c) Jane Doe, some rights reserved (CC BY)' -> 'Jane Doe'."""
    c = re.sub(r"^\(c\)\s*", "", c or "").strip()
    c = re.sub(r",?\s*(some|no|all) rights reserved.*$", "", c, flags=re.I).strip()
    # CC0 photos carry no name on iNaturalist ("no rights reserved"); the observation link identifies them
    return re.sub(r"\s*\((CC[^)]*|public domain)\)$", "", c, flags=re.I).strip() or "iNaturalist"


def clean_licence(l):
    return (l or "").replace("CC-BY-SA", "CC BY-SA").replace("CC-BY", "CC BY")


def mass(g):
    if not g:
        return ""
    return f"{g / 1000:.3g} kg" if g >= 1000 else f"{g:.3g} g"


def photo_size(url, size):
    return re.sub(r"/(medium|small|large|original)\.", f"/{size}.", url)


def fmt_range(lo_hi, unit):
    if not lo_hi:
        return ""
    lo, hi = lo_hi
    f = lambda x: f"{x:g}"
    return f"{f(lo)}–{f(hi)} {unit}" if hi and hi != lo else f"{f(lo)} {unit}"


class Site:
    def __init__(self, args):
        picks, eye, species_json, guide_json, self.commit, self.out = args[:6]
        self.cache = args[6] if len(args) > 6 else None
        self.t = json.load(open(os.path.join(HERE, "i18n.json"), encoding="utf-8"))
        self.picks = list(csv.DictReader(open(picks, encoding="utf-8")))
        eye_rows = list(csv.DictReader(open(eye, encoding="utf-8")))
        self.removed = sum(1 for r in eye_rows if r["verdict"] == "reject" and not r["obs"].startswith("species:"))
        self.species = {s["id"]: s for s in json.load(open(species_json, encoding="utf-8"))["species"]}
        self.guide = json.load(open(guide_json, encoding="utf-8"))["species"]
        self.raw = f"https://raw.githubusercontent.com/alchaincyf/huashu-bird-sticker/{self.commit}/"
        used = set()
        self.birds = []
        for p in sorted(self.picks, key=lambda p: self.species[p["id"]]["taxonomy"].get("seq", 0)):
            s = self.species[p["id"]]
            slug = slugify(s["names"].get("en") or p["id"]) or slugify(p["id"])
            if slug in used:
                slug = slugify(p["id"])
            used.add(slug)
            p = dict(p, credit=clean_credit(p["credit"]), licence=clean_licence(p["licence"]))
            self.birds.append({"p": p, "s": s, "slug": slug})
        self.median_a = int(statistics.median(int(p["people_agree"]) for p in self.picks))
        self.median_m = int(statistics.median(int(p["id_months"]) for p in self.picks))

    # ---------- helpers ----------
    def tr(self, lang, key, **kw):
        s = self.t[lang].get(key) or self.t["en"].get(key, "")
        for k, v in kw.items():
            s = s.replace("{" + k + "}", str(v))
        return s

    def name(self, b, lang):
        names = b["s"]["names"]
        key = [l for l in LANGS if l[0] == lang][0][3]
        return names.get(key) or (names.get("zh-Hans") if lang == "zh-Hant" else None) or names.get("en") or b["s"]["scientificName"]

    def taxon_line(self, s, lang):
        zh, tx = s.get("zh") or {}, s["taxonomy"]
        if lang in ("zh-Hans", "zh-Hant") and zh.get("family"):
            return f"{zh['family']} {tx['family']} · {zh.get('order', '')} {tx['order']}"
        return " · ".join(x for x in (tx.get("familyEnglish", ""), tx["family"], tx["order"]) if x)

    def report_url(self, b):
        q = {"template": "wrong-photo.yml", "title": f"[photo] {b['s']['scientificName']} {b['s']['names'].get('en', '')}",
             "species": f"{b['s']['scientificName']} ({b['s']['names'].get('zh-Hans', '')} / {b['s']['names'].get('en', '')})",
             "photo": b["p"]["observation"]}
        return f"{REPO}/issues/new?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)

    def sticker(self, b):
        st = b["s"].get("sticker") or {}
        return (self.raw + st["file"]) if st.get("file") else "", st.get("reviewScore", ""), st.get("meetsQualityBar", True)

    def head(self, lang, title, desc, path, image, depth):
        root = "../" * depth
        alts = "".join(f'<link rel="alternate" hreflang="{l[2]}" href="{SITE}{l[1]}{path}">' for l in LANGS)
        return f"""<!doctype html>
<html lang="{[l for l in LANGS if l[0] == lang][0][2]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{[l for l in LANGS if l[0] == lang][0][1]}{path}">
{alts}<link rel="alternate" hreflang="x-default" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(self.tr(lang, 'site_name'))}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{e(image)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f7f6f1">
<link rel="icon" href="{root}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
"""

    def header(self, lang, depth, path):
        root = "../" * depth
        pre = [l for l in LANGS if l[0] == lang][0][1]
        cur = ' aria-current="true"'
        langs = "".join(f'<li><a href="{root}{l[1]}{path}" hreflang="{l[2]}" lang="{l[2]}"{cur if l[0] == lang else ""}>{e(l[4])}</a></li>' for l in LANGS)
        return f"""<header class="top"><div class="wrap">
<a class="brand" href="{root}{pre}">{e(self.tr(lang, 'site_name'))}</a>
<nav><a href="{root}{pre}">{e(self.tr(lang, 'nav_home'))}</a><a href="{root}{pre}method/">{e(self.tr(lang, 'nav_method'))}</a>
<details class="langs"><summary>{e(self.tr(lang, 'nav_lang'))}</summary><ul>{langs}</ul></details></nav>
</div></header>
"""

    def footer(self, lang, depth):
        root = "../" * depth
        note = self.tr(lang, "translated_note")
        return f"""<footer class="foot"><div class="wrap">
{f'<p class="note">{e(note)}</p>' if note else ''}<p>{e(self.tr(lang, 'footer'))} <a href="{REPO}">{e(self.tr(lang, 'source_code'))}</a> · <a href="{root}privacy.html">Privacy</a></p>
</div></footer>
</body>
</html>
"""

    def write(self, rel, text):
        path = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(text)

    # ---------- pages ----------
    def home(self, lang, pre):
        depth = pre.count("/")
        n = len(self.birds)
        rows = []
        for b in self.birds:
            st, score, ok = self.sticker(b)
            rows.append([b["slug"], self.name(b, lang), b["s"]["scientificName"], b["s"]["taxonomy"].get("familyEnglish", "") + " " + b["s"]["taxonomy"]["family"],
                         int(b["p"]["people_agree"]), int(b["p"]["id_months"]), photo_size(b["p"]["photo"], "small"), st,
                         b["s"]["names"].get("en", ""), b["s"]["names"].get("zh-Hans", ""), b["p"]["observation"].rsplit("/", 1)[-1]])
        data = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        strings = {k: self.tr(lang, k) for k in ("evidence", "count", "report", "no_result", "huashu_cap", "photo_cap")}
        strings["repo"] = REPO
        title = f"{self.tr(lang, 'site_name')} · {self.tr(lang, 'tagline')}"
        body = f"""<main class="wrap">
<section class="hero">
<h1>{e(self.tr(lang, 'tagline'))}</h1>
<p class="lead">{e(self.tr(lang, 'lead'))}</p>
<div class="facts">
<div><b>{n:,}</b><span>{e(self.tr(lang, 'fact_species'))}</span></div>
<div><b>{self.median_a}</b><span>{e(self.tr(lang, 'fact_evidence', m=self.median_m))}</span></div>
<div><b>100%</b><span>{e(self.tr(lang, 'fact_licence'))}</span></div>
<div><b>{self.removed}</b><span>{e(self.tr(lang, 'fact_removed'))}</span></div>
</div>
<p class="more-link"><a href="method/">{e(self.tr(lang, 'nav_method'))} →</a></p>
</section>
<div class="bar">
<input id="q" type="search" placeholder="{e(self.tr(lang, 'search'))}" aria-label="{e(self.tr(lang, 'search'))}">
<select id="f" aria-label="filter"><option value="all">{e(self.tr(lang, 'filter_all'))}</option><option value="five">{e(self.tr(lang, 'filter_five'))}</option></select>
<label class="toggle"><input id="cmp" type="checkbox"> {e(self.tr(lang, 'compare'))}</label>
<span id="count" aria-live="polite"></span>
</div>
<div class="grid" id="grid"></div>
<button id="more" type="button">{e(self.tr(lang, 'more'))}</button>
<noscript><ul class="plain">{''.join(f'<li><a href="birds/{b["slug"]}/">{e(self.name(b, lang))}</a></li>' for b in self.birds)}</ul></noscript>
</main>
<script>window.BIRDS={data};window.T={json.dumps(strings, ensure_ascii=False)};</script>
<script src="{'../' * depth}assets/site.js"></script>
"""
        self.write(pre + "index.html", self.head(lang, title, self.tr(lang, "meta_desc", n=f"{n:,}"), "", SITE + "assets/og.png", depth)
                   + self.header(lang, depth, "") + body + self.footer(lang, depth))

    def bird_page(self, lang, pre, b):
        depth = pre.count("/") + 2
        s, p = b["s"], b["p"]
        name, sci = self.name(b, lang), s["scientificName"]
        path = f"birds/{b['slug']}/"
        a, m = int(p["people_agree"]), int(p["id_months"])
        large = photo_size(p["photo"], "large")
        parts = []
        size = s.get("size") or {}
        traits = s.get("traits") or {}
        cells = [(self.tr(lang, "length"), fmt_range(size.get("bodyLengthCm"), "cm")),
                 (self.tr(lang, "wingspan"), fmt_range(size.get("wingspanCm"), "cm")),
                 (self.tr(lang, "weight"), mass(traits.get("massG")))]
        cells = [c for c in cells if c[1]]
        if cells:
            parts.append(f'<section><h2>{e(self.tr(lang, "size_title"))}</h2><dl class="kv">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in cells) + "</dl></section>")
        iucn = ((s.get("conservation") or {}).get("iucn") or "").split(" ")[0]
        if iucn:
            parts.append(f'<section><h2>{e(self.tr(lang, "iucn_title"))}</h2><p><span class="iucn iucn-{e(iucn)}">{e(iucn)}</span> {e(self.tr(lang, "iucn_" + iucn))}</p></section>')
        rng = s.get("range") or {}
        if lang in ("zh-Hans",) and rng.get("zh-Hans"):
            rtext, rnote = rng["zh-Hans"], ""
        else:
            rtext, rnote = rng.get("text") or "", ("" if lang == "en" else self.tr(lang, "range_note"))
        if rtext:
            parts.append(f'<section><h2>{e(self.tr(lang, "range_title"))}</h2><p>{e(rtext)} <span class="muted">{e(rnote)}</span></p></section>')
        g = self.guide.get(s["id"]) if lang == "zh-Hans" else None
        if g:
            items = "".join(f"<li>{e(x)}</li>" for x in g.get("marks", []))
            parts.append(f"""<section><h2>{e(self.tr(lang, 'guide_title'))}</h2>
{f'<p class="impression">{e(g["impression"])}</p>' if g.get('impression') else ''}{f'<ul>{items}</ul>' if items else ''}
{f'<p>{e(g["sexAge"])}</p>' if g.get('sexAge') else ''}{f'<p>{e(g["funFact"])}</p>' if g.get('funFact') else ''}
<p class="muted small">{e(self.tr(lang, 'guide_source'))}{f' <a href="{e(g["basedOn"])}">Wikipedia</a>' if g.get('basedOn') else ''}</p></section>""")
        names = "".join(f'<li><span class="muted">{e(l[4])}</span> {e(s["names"][l[3]])}</li>' for l in LANGS if l[0] != lang and s["names"].get(l[3]))
        if names:
            parts.append(f'<section><h2>{e(self.tr(lang, "names_title"))}</h2><ul class="names">{names}</ul></section>')
        cite = self.tr(lang, "cite_line", c=p["credit"], l=p["licence"])
        parts.append(f'<section><h2>{e(self.tr(lang, "cite_title"))}</h2><p class="cite">{e(cite)}</p></section>')
        st, score, ok = self.sticker(b)
        if st:
            note = self.tr(lang, "compare_note", s=score, bar="" if ok else self.tr(lang, "bar_no"))
            parts.append(f"""<section><details class="compare"><summary>{e(self.tr(lang, 'compare_title'))}</summary>
<div class="pair"><figure><img loading="lazy" src="{e(photo_size(p['photo'], 'medium'))}" alt="{e(name)}"><figcaption>{e(self.tr(lang, 'photo_cap'))}</figcaption></figure>
<figure><img loading="lazy" data-sticker="{e(st[len(self.raw):])}" alt="{e(self.tr(lang, 'huashu_cap'))} {e(name)}"><figcaption>{e(self.tr(lang, 'huashu_cap'))}</figcaption></figure></div>
<p class="muted small">{e(note)}</p></details></section>
<script src="{'../' * depth}assets/huashu.js"></script>""")
        sub = [x for x in [s["names"].get("en") if lang != "en" else None, s["names"].get("zh-Hans") if lang not in ("zh-Hans", "zh-Hant") else None] if x and x != name]
        body = f"""<main class="wrap species">
<h1>{e(name)}</h1>
<p class="sci"><i>{e(sci)}</i> {e(s.get('authority', ''))}{''.join(f' · {e(x)}' for x in sub)}</p>
<p class="muted">{e(self.taxon_line(s, lang))}</p>
<figure class="hero-photo"><img src="{e(large)}" alt="{e(name)}" width="1024">
<figcaption>{e(self.tr(lang, 'photo_by', c=p['credit']))} · {e(self.tr(lang, 'licence', l=p['licence']))}</figcaption></figure>
<div class="evidence">
<p class="ev"><b>{e(self.tr(lang, 'evidence', a=a, m=m))}</b></p>
<p>{e(self.tr(lang, 'evidence_long', a=a, m=m))}</p>
<p class="muted">{e(self.tr(lang, 'real_photo'))}</p>
<p><a href="{e(p['observation'])}">{e(self.tr(lang, 'view_obs'))} ↗</a> · <a class="report" href="{e(self.report_url(b))}">{e(self.tr(lang, 'report_long'))} ↗</a></p>
</div>
{''.join(parts)}
</main>
"""
        title = f"{name} ({sci}) · {self.tr(lang, 'site_name')}"
        desc = f"{name} ({sci}): {self.tr(lang, 'evidence', a=a, m=m)}. {self.tr(lang, 'real_photo')}"
        self.write(pre + path + "index.html", self.head(lang, title, desc, path, large, depth) + self.header(lang, depth, path) + body + self.footer(lang, depth))

    def method(self, lang, pre):
        depth = pre.count("/") + 1
        steps = "".join(f"<li>{e(self.tr(lang, f'm_s{i}', r=self.removed))}</li>" for i in range(1, 7))
        faq = "".join(f'<details class="faq"><summary>{e(self.tr(lang, f"q{i}"))}</summary><p>{e(self.tr(lang, f"a{i}"))}</p></details>' for i in range(1, 7))
        srcs = "".join(f"<li>{e(self.tr(lang, f'src{i}'))}</li>" for i in range(1, 5))
        body = f"""<main class="wrap prose">
<h1>{e(self.tr(lang, 'm_title'))}</h1>
<p class="lead">{e(self.tr(lang, 'm_intro'))}</p>
<p>{e(self.tr(lang, 'm_numbers', n=f"{len(self.birds):,}"))}</p>
<h2>{e(self.tr(lang, 'm_steps_title'))}</h2><ol>{steps}</ol>
<h2>{e(self.tr(lang, 'm_faq_title'))}</h2>{faq}
<h2>{e(self.tr(lang, 'm_sources_title'))}</h2><ul>{srcs}</ul>
<p class="muted small"><a href="{'../' * depth}picks.csv">picks.csv</a> · <a href="{'../' * depth}eye-check.csv">eye-check.csv</a> · <a href="{REPO}/blob/main/RULES.md">RULES.md</a></p>
</main>
"""
        title = f"{self.tr(lang, 'm_title')} · {self.tr(lang, 'site_name')}"
        self.write(pre + "method/index.html", self.head(lang, title, self.tr(lang, "m_intro"), "method/", SITE + "assets/og.png", depth)
                   + self.header(lang, depth, "method/") + body + self.footer(lang, depth))

    # ---------- assets ----------
    def assets(self):
        os.makedirs(os.path.join(self.out, "assets"), exist_ok=True)
        for f in ("site.css", "site.js"):
            shutil.copy(os.path.join(HERE, f), os.path.join(self.out, "assets", f))
        # The pinned huashu commit lives only here, so a new commit rewrites one file instead of every species page.
        open(os.path.join(self.out, "assets", "huashu.js"), "w", encoding="utf-8").write(
            "// Huashu sticker base URL, pinned to the data commit this site was built from.\n"
            f"(function(){{var base={json.dumps(self.raw)};document.querySelectorAll('img[data-sticker]').forEach(function(i){{i.src=base+i.getAttribute('data-sticker');}});}})();\n")
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            print("PIL missing: skipping icons and share image")
            return
        icon = os.path.join(HERE, "..", "ios", "App", "Assets.xcassets", "AppIcon.appiconset", "icon-1024.png")
        im = Image.open(icon).convert("RGB")
        im.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(self.out, "assets", "apple-touch-icon.png"))
        im.resize((64, 64), Image.Resampling.LANCZOS).save(os.path.join(self.out, "assets", "favicon.png"))
        # share image: only CC0 photos, so the image itself needs no credit line
        og = Image.new("RGB", (1200, 630), (247, 246, 241))
        cc0 = [b for b in self.birds if b["p"]["licence"] == "CC0"]
        tiles = []
        if self.cache:
            for b in cc0:
                f = os.path.join(self.cache, hashlib.sha1(b["p"]["photo"].encode()).hexdigest() + ".jpg")
                if os.path.exists(f):
                    tiles.append(f)
                if len(tiles) == 6:
                    break
        for i, f in enumerate(tiles):
            t = Image.open(f).convert("RGB")
            w, h = t.size
            side = min(w, h)
            t = t.crop(((w - side) // 2, (h - side) // 2, (w + side) // 2, (h + side) // 2)).resize((200, 200), Image.Resampling.LANCZOS)
            og.paste(t, (580 + (i % 3) * 205, 110 + (i // 3) * 205))
        d = ImageDraw.Draw(og)
        font = "/System/Library/Fonts/Hiragino Sans GB.ttc"
        big = ImageFont.truetype(font, 64) if os.path.exists(font) else ImageFont.load_default()
        small = ImageFont.truetype(font, 30) if os.path.exists(font) else ImageFont.load_default()
        d.text((60, 160), "人选鸟图", fill=(29, 29, 27), font=big)
        d.text((60, 260), "每种鸟一张真实照片", fill=(47, 107, 79), font=small)
        d.text((60, 305), "每张都经至少 3 人认定", fill=(47, 107, 79), font=small)
        d.text((60, 380), f"{len(self.birds):,} species · Bird Human Picks", fill=(107, 106, 101), font=small)
        og.save(os.path.join(self.out, "assets", "og.png"), optimize=True)

    def sitemap(self):
        urls = []
        for l in LANGS:
            urls += [SITE + l[1], SITE + l[1] + "method/"] + [f"{SITE}{l[1]}birds/{b['slug']}/" for b in self.birds]
        self.write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                   + "".join(f"<url><loc>{e(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
        self.write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")

    def build(self):
        for l in LANGS:
            if l[1]:
                shutil.rmtree(os.path.join(self.out, l[1]), ignore_errors=True)
        shutil.rmtree(os.path.join(self.out, "birds"), ignore_errors=True)
        shutil.rmtree(os.path.join(self.out, "method"), ignore_errors=True)
        self.assets()
        for code, pre, *_ in LANGS:
            self.home(code, pre)
            self.method(code, pre)
            for b in self.birds:
                self.bird_page(code, pre, b)
        self.sitemap()
        below = sum(1 for b in self.birds if not self.sticker(b)[2])
        stats = {"species": len(self.birds), "languages": len(LANGS), "pages": len(LANGS) * (len(self.birds) + 2), "removed": self.removed,
                 "median_agree": self.median_a, "median_months": self.median_m, "huashu_commit": self.commit, "huashu_below_bar": below}
        self.write("site-stats.json", json.dumps(stats, indent=1))
        print(json.dumps(stats))


if __name__ == "__main__":
    Site(sys.argv[1:]).build()
