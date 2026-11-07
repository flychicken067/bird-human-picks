#!/usr/bin/env python3
"""Write data/README.md from data/coverage.json, so the field table always shows the real coverage.

Usage: k_data_readme.py <data dir>
"""
import json
import os
import sys

d = sys.argv[1]
cov = json.load(open(os.path.join(d, "coverage.json"), encoding="utf-8"))
meta = json.load(open(os.path.join(d, "species.json"), encoding="utf-8"))
n, f = cov["count"], cov["fields"]
hu = meta["huashuData"]


def c(key):
    v = f[key]
    return "all" if v == n else f"{v:,}"


licences = {}
for s in meta["species"]:
    licences[s["photo"]["license"]] = licences.get(s["photo"]["license"], 0) + 1

text = f"""# Data

`species.json` is the complete dataset, one record per species, in AviList v2026 sequence. The CSV files are flattened subsets for spreadsheets. The layout and the shared fields follow [huashu-bird-sticker's data](https://github.com/alchaincyf/huashu-bird-sticker/tree/{hu['commit']}/data) (version {hu['version']}, commit `{hu['commit']}`), so the two datasets can be joined on `id`.

| File | Contents | License |
|---|---|---|
| `species.json` | Everything below except the Chinese field-guide text | CC BY 4.0 for our compilation; fields copied from huashu-bird-sticker stay MIT; third-party fields keep their terms (see Sources) |
| `species.csv` | Taxonomy, main names, IDs, photo, evidence and the matching huashu sticker | as above |
| `names.csv` | Names in 43 languages for the {n:,} species, one column per language | English: CC BY 4.0 (AviList); others: CC BY 3.0 (IOC) |
| `languages.json` | Language codes and the IOC multilingual column each comes from | MIT (huashu-bird-sticker) |
| `field-guide.zh-Hans.json` | Chinese field-guide notes for {cov['fieldGuide']:,} of the species | CC BY-SA 4.0 (huashu-bird-sticker) |
| `coverage.json` | How many records have each field; this README is generated from it | CC BY 4.0 |

## Fields in `species.json`

{n:,} records. Coverage counts records where the field is present and not empty.

| Field | What it is | Source | Coverage |
|---|---|---|---|
| `id` | `Genus_species`, the same ID huashu-bird-sticker uses | huashu-bird-sticker | {c('id')} |
| `scientificName`, `authority` | | AviList v2026 via huashu-bird-sticker | {c('scientificName')} |
| `taxonomy` | AviList sequence, order, family, family English name, genus | AviList v2026 via huashu-bird-sticker | {c('taxonomy')} |
| `names` | Common names keyed by language code; `en` is the AviList English name | AviList; IOC 15.2 multilingual | `en` {c('names.en')}, `zh-Hans` {c('names.zh-Hans')} |
| `otherEnglishNames` | Clements and BirdLife English names where they differ from AviList | AviList | {c('otherEnglishNames')} |
| `ids` | eBird, Avibase, Wikidata, GBIF, iNaturalist IDs | AviList; Wikidata; iNaturalist | eBird {c('ids.ebird')}, Avibase {c('ids.avibase')}, Wikidata {c('ids.wikidata')}, GBIF {c('ids.gbif')}, iNaturalist {c('ids.inaturalist')} |
| `range` | `text`: AviList range statement; `ioc`: IOC 15.2 breeding ranges; `zh-Hans`: Chinese summary | AviList v2026; IOC 15.2 | `text` {c('range.text')}, `ioc` {c('range.ioc')}, `zh-Hans` {c('range.zh-Hans')} |
| `subspecies` | Subspecies with authority and range | AviList v2026 | {c('subspecies')} (species with subspecies) |
| `traits` | Mass, wing, tail, tarsus, bill, hand-wing index, habitat, migration, diet, lifestyle | AVONET | {c('traits')} |
| `size` | Body length and wingspan in cm as `[min, max]` | Wikidata, Wikipedia text | {c('size')} |
| `conservation` | IUCN Red List category and other status fields | AviList (BirdLife v10); Wikidata; China's 2021 list | IUCN {c('conservation.iucn')} |
| `zh` | Pinyin, Chinese aliases, order and family names, Chinese Wikipedia page | IOC 15.2 Chinese; Wikidata; Chinese Wikipedia | {c('zh')} |
| `taxonConcept`, `previous`, `dataNotes` | What changed in the move to AviList | huashu-bird-sticker | {c('taxonConcept')}; `dataNotes` {c('dataNotes')} |
| `photo` | The chosen photo: iNaturalist observation and photo page, original and large URLs, original width and height, author, author profile, the attribution text iNaturalist gives, license and license URL | iNaturalist | page {c('photo.page')}, size {c('photo.width')}, author {c('photo.author')}, author profile {c('photo.authorUrl')}, license {c('photo.license')} |
| `evidence` | Identifiers who currently agree on this species, not counting the photographer and not counting identifications made by accepting iNaturalist's AI suggestion; in how many different months; dissenting identifiers (always 0); faves; research-grade observations of the species | iNaturalist identifications | {c('evidence.agreeingIdentifiers')} |
| `checks` | `framing`: what the detector found (number of birds, how much of the frame the bird spans, whether a person is visible); `eyeCheck`: passed the photo-by-photo look. Neither decides the species | this project | {c('checks.framing')} |
| `huashu` | The matching huashu-bird-sticker AI sticker: file URL at the pinned commit, kind, review score, whether it meets his quality bar | huashu-bird-sticker | {c('huashu.sticker')} |

Notes:

- Fields copied from huashu-bird-sticker are unchanged; gaps there are gaps here (for example `size`, which he fills from Wikidata and Wikipedia only where they give a value). See his data README for how each was compiled.
- `ids.inaturalist`: huashu-bird-sticker has it for 645 of 11,011 species. We matched every selected species to an iNaturalist taxon by exact scientific name and filled the {f['ids.inaturalist'] - sum(1 for s in meta['species'] if (s.get('ids') or {}).get('inaturalist') and not (s.get('ids') or {}).get('inaturalistSource')):,} that were missing; those records carry `ids.inaturalistSource: "bird-human-picks"`.
- `photo.author` is empty for the {n - f['photo.author']:,} CC0 photos: their photographers waived attribution and iNaturalist gives no name. `photo.authorUrl` still links to their profile.
- `photo.licenseUrl` points to version 4.0 of each license. iNaturalist's attribution text does not state a version and we did not check each photo, so some may carry an earlier version; the license shown on the photo page is authoritative.
- No identifier names and no observation coordinates are stored.

## Photos

Every record has exactly one photo; the photos themselves are not in this repository. By license:

| License | Photos |
|---|---|
""" + "".join(f"| {k} | {v:,} |\n" for k, v in sorted(licences.items(), key=lambda x: -x[1])) + f"""
All three allow commercial use. CC BY and CC BY-SA require crediting the photographer; CC BY-SA also requires sharing changed versions under the same license.

## Sources

- iNaturalist observations, photos and identifications, <https://www.inaturalist.org>. Each photo under its own license as listed.
- huashu-bird-sticker data {hu['version']}, Huashu (alchaincyf), MIT, <https://github.com/alchaincyf/huashu-bird-sticker>.
- AviList Core Team. 2026. AviList: The Global Avian Checklist, v2026. <https://doi.org/10.2173/avilist.v2026>. CC BY 4.0.
- IOC World Bird List v15.2, Gill, Donsker & Rasmussen (Eds), CC BY 3.0. <https://worldbirdnames.org/>
- AVONET: Tobias, J. A. et al. (2022). *Ecology Letters* 25: 581–597. doi:10.1111/ele.13898. CC BY 4.0.
- Wikidata, CC0.
- 国家重点保护野生动物名录 (2021).
- Chinese field-guide notes: huashu-bird-sticker, CC BY-SA 4.0.
"""
open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(text)
print("written", len(text), "chars")
