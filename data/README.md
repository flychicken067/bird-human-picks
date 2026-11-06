# Data

`species.json` is the complete dataset, one record per species, in AviList v2026 sequence. The CSV files are flattened subsets for spreadsheets. The layout and the shared fields follow [huashu-bird-sticker's data](https://github.com/alchaincyf/huashu-bird-sticker/tree/8f28a08/data) (version 2.2.11, commit `8f28a08`), so the two datasets can be joined on `id`.

| File | Contents | License |
|---|---|---|
| `species.json` | Everything below except the Chinese field-guide text | CC BY 4.0 for our compilation; fields copied from huashu-bird-sticker stay MIT; third-party fields keep their terms (see Sources) |
| `species.csv` | Taxonomy, main names, IDs, photo, evidence and the matching huashu sticker | as above |
| `names.csv` | Names in 43 languages for the 1,209 species, one column per language | English: CC BY 4.0 (AviList); others: CC BY 3.0 (IOC) |
| `languages.json` | Language codes and the IOC multilingual column each comes from | MIT (huashu-bird-sticker) |
| `field-guide.zh-Hans.json` | Chinese field-guide notes for 325 of the species | CC BY-SA 4.0 (huashu-bird-sticker) |
| `coverage.json` | How many records have each field; this README is generated from it | CC BY 4.0 |

## Fields in `species.json`

1,209 records. Coverage counts records where the field is present and not empty.

| Field | What it is | Source | Coverage |
|---|---|---|---|
| `id` | `Genus_species`, the same ID huashu-bird-sticker uses | huashu-bird-sticker | all |
| `scientificName`, `authority` | | AviList v2026 via huashu-bird-sticker | all |
| `taxonomy` | AviList sequence, order, family, family English name, genus | AviList v2026 via huashu-bird-sticker | all |
| `names` | Common names keyed by language code; `en` is the AviList English name | AviList; IOC 15.2 multilingual | `en` all, `zh-Hans` 1,208 |
| `otherEnglishNames` | Clements and BirdLife English names where they differ from AviList | AviList | 227 |
| `ids` | eBird, Avibase, Wikidata, GBIF, iNaturalist IDs | AviList; Wikidata; iNaturalist | eBird all, Avibase all, Wikidata 1,194, GBIF 1,176, iNaturalist all |
| `range` | `text`: AviList range statement; `ioc`: IOC 15.2 breeding ranges; `zh-Hans`: Chinese summary | AviList v2026; IOC 15.2 | `text` all, `ioc` all, `zh-Hans` 1,208 |
| `subspecies` | Subspecies with authority and range | AviList v2026 | 563 (species with subspecies) |
| `traits` | Mass, wing, tail, tarsus, bill, hand-wing index, habitat, migration, diet, lifestyle | AVONET | 1,177 |
| `size` | Body length and wingspan in cm as `[min, max]` | Wikidata, Wikipedia text | 616 |
| `conservation` | IUCN Red List category and other status fields | AviList (BirdLife v10); Wikidata; China's 2021 list | IUCN 1,146 |
| `zh` | Pinyin, Chinese aliases, order and family names, Chinese Wikipedia page | IOC 15.2 Chinese; Wikidata; Chinese Wikipedia | 1,208 |
| `taxonConcept`, `previous`, `dataNotes` | What changed in the move to AviList | huashu-bird-sticker | all; `dataNotes` 0 |
| `photo` | The chosen photo: iNaturalist observation and photo page, original and large URLs, original width and height, author, author profile, the attribution text iNaturalist gives, license and license URL | iNaturalist | page all, size all, author 1,046, author profile all, license all |
| `evidence` | Identifiers who currently agree on this species, in how many different months, dissenting identifiers (always 0), faves, research-grade observations of the species | iNaturalist identifications | all |
| `checks` | `framing`: what the detector found (number of birds, how much of the frame the bird spans, whether a person is visible); `eyeCheck`: passed the photo-by-photo look. Neither decides the species | this project | all |
| `huashu` | The matching huashu-bird-sticker AI sticker: file URL at the pinned commit, kind, review score, whether it meets his quality bar | huashu-bird-sticker | all |

Notes:

- Fields copied from huashu-bird-sticker are unchanged; gaps there are gaps here (for example `size`, which he fills from Wikidata and Wikipedia only where they give a value). See his data README for how each was compiled.
- `ids.inaturalist`: huashu-bird-sticker has it for 645 of 11,011 species. We matched every selected species to an iNaturalist taxon by exact scientific name and filled the 1,066 that were missing; those records carry `ids.inaturalistSource: "bird-human-picks"`.
- `photo.author` is empty for the 163 CC0 photos: their photographers waived attribution and iNaturalist gives no name. `photo.authorUrl` still links to their profile.
- `photo.licenseUrl` points to version 4.0 of each license. iNaturalist's attribution text does not state a version and we did not check each photo, so some may carry an earlier version; the license shown on the photo page is authoritative.
- No identifier names and no observation coordinates are stored.

## Photos

Every record has exactly one photo; the photos themselves are not in this repository. By license:

| License | Photos |
|---|---|
| CC BY | 923 |
| CC0 | 163 |
| CC BY-SA | 123 |

All three allow commercial use. CC BY and CC BY-SA require crediting the photographer; CC BY-SA also requires sharing changed versions under the same license.

## Sources

- iNaturalist observations, photos and identifications, <https://www.inaturalist.org>. Each photo under its own license as listed.
- huashu-bird-sticker data 2.2.11, Huashu (alchaincyf), MIT, <https://github.com/alchaincyf/huashu-bird-sticker>.
- AviList Core Team. 2026. AviList: The Global Avian Checklist, v2026. <https://doi.org/10.2173/avilist.v2026>. CC BY 4.0.
- IOC World Bird List v15.2, Gill, Donsker & Rasmussen (Eds), CC BY 3.0. <https://worldbirdnames.org/>
- AVONET: Tobias, J. A. et al. (2022). *Ecology Letters* 25: 581–597. doi:10.1111/ele.13898. CC BY 4.0.
- Wikidata, CC0.
- 国家重点保护野生动物名录 (2021).
- Chinese field-guide notes: huashu-bird-sticker, CC BY-SA 4.0.
