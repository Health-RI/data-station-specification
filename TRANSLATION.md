# Translation Log: Dutch → English

This document records all actions taken to translate the MkDocs documentation project from Dutch into English for the [data-station-specification](https://github.com/health-ri/data-station-specification) repository.

## Goal

Translate the entire MkDocs project from Dutch into English. The project is a technical specification document for "Data stations for secondary use of health data" (EHDS/health data infrastructure). The i18n infrastructure uses `mkdocs-static-i18n` v1.3.0 with `docs_structure: suffix`, meaning `filename.md` is Dutch and `filename.en.md` is English.

---

## Translation approach

- Direct AI-assisted translation, preserving technical terminology, markdown formatting and internal links.
- BibTeX citation keys (`[@key]`), admonitions, footnotes and mermaid/tab content blocks are preserved exactly as-is.
- SVG diagrams: English `.en.svg` variants were generated for all diagrams containing Dutch text; image references in `.en.md` files point to these translated variants.
- For the glossary: a separate `includes/woordenlijst.en.md` was created with English definitions (not an in-place replacement).
- The DataSHIELD section (commented out of nav) was translated but kept commented out.
- `docs/applicatie/data-pooling.en.md` is empty — the Dutch original is also 0 bytes.

---

## Infrastructure changes

| File | Action | Description |
|------|--------|-------------|
| `mkdocs.yml` | Modified | Added comprehensive `nav_translations` for all numbered sections and subsections (~45 entries); added `hooks: - hooks.py` |
| `overrides/main.html` | Modified | Made announce banner language-aware using Jinja2 `{% if config.theme.language == 'en' %}` conditional |
| `hooks.py` | Created | New file — swaps `auto_append` in `pymdownx.snippets` config at build time to use `woordenlijst.en.md` for English builds |
| `includes/woordenlijst.en.md` | Created | Full English translation of all 47 glossary entries |

### Technical notes

- `pymdownx.snippets` `auto_append` is static and cannot switch per locale natively; `hooks.py` reads `config.plugins['i18n'].current_language` to swap the appended file at build time.
- LSP errors in `mkdocs.yml` (unresolved Python name tags) are false positives — the YAML is valid for MkDocs.
- The `toc` title `"Op deze pagina"` in `mkdocs.yml` applies only to the Dutch build; the English build uses the Material theme's built-in English label automatically.

---

## Content translations

### Pre-existing English files (not translated in this project)

These files already existed in English before work began and have not been replaced:

| File |
|------|
| `docs/appendix/tehdas2-requirements.en.md` |
| `docs/scratch.en.md` |

### Session 1 — Infrastructure setup + sections 1–4

| Created file | Dutch source |
|-------------|--------------|
| `docs/waarom.en.md` | `docs/waarom.md` |
| `docs/proces/vinden.en.md` | `docs/proces/vinden.md` |
| `docs/proces/aanvragen.en.md` | `docs/proces/aanvragen.md` |
| `docs/proces/klaarzetten.en.md` | `docs/proces/klaarzetten.md` |
| `docs/proces/analyseren.en.md` | `docs/proces/analyseren.md` |
| `docs/proces/publiceren.en.md` | `docs/proces/publiceren.md` |
| `docs/informatie/index.en.md` | `docs/informatie/index.md` |
| `docs/informatie/syntactisch.en.md` | `docs/informatie/syntactisch.md` |
| `docs/informatie/semantisch.en.md` | `docs/informatie/semantisch.md` |
| `docs/informatie/metadata.en.md` | `docs/informatie/metadata.md` |
| `docs/applicatie/index.en.md` | `docs/applicatie/index.md` |
| `docs/applicatie/data-station.en.md` | `docs/applicatie/data-station.md` |
| `docs/applicatie/catalogus.en.md` | `docs/applicatie/catalogus.md` |
| `docs/applicatie/daams.en.md` | `docs/applicatie/daams.md` |
| `docs/applicatie/processing-hub.en.md` | `docs/applicatie/processing-hub.md` |
| `docs/applicatie/federatieve-analyse.en.md` | `docs/applicatie/federatieve-analyse.md` |
| `docs/applicatie/federatief-leren.en.md` | `docs/applicatie/federatief-leren.md` |
| `docs/applicatie/data-pooling.en.md` | `docs/applicatie/data-pooling.md` (both empty) |

### Session 2 — Sections 5–7 + appendix + DataSHIELD

| Created file | Dutch source | Notes |
|-------------|--------------|-------|
| `docs/infrastructuur/index.en.md` | `docs/infrastructuur/index.md` | |
| `docs/infrastructuur/evolutie.en.md` | `docs/infrastructuur/evolutie.md` | |
| `docs/infrastructuur/composable-data-stack.en.md` | `docs/infrastructuur/composable-data-stack.md` | |
| `docs/implementaties/KIK-V/index.en.md` | `docs/implementaties/KIK-V/index.md` | |
| `docs/implementaties/KIK-V/proces.en.md` | `docs/implementaties/KIK-V/proces.md` | |
| `docs/implementaties/KIK-V/informatie.en.md` | `docs/implementaties/KIK-V/informatie.md` | |
| `docs/implementaties/KIK-V/applicatie.en.md` | `docs/implementaties/KIK-V/applicatie.md` | |
| `docs/implementaties/KIK-V/infrastructuur.en.md` | `docs/implementaties/KIK-V/infrastructuur.md` | |
| `docs/implementaties/PLUGIN/index.en.md` | `docs/implementaties/PLUGIN/index.md` | |
| `docs/implementaties/PLUGIN/proces.en.md` | `docs/implementaties/PLUGIN/proces.md` | Mermaid diagram labels translated |
| `docs/implementaties/PLUGIN/informatie.en.md` | `docs/implementaties/PLUGIN/informatie.md` | |
| `docs/implementaties/PLUGIN/applicatie.en.md` | `docs/implementaties/PLUGIN/applicatie.md` | |
| `docs/implementaties/PLUGIN/infrastructuur.en.md` | `docs/implementaties/PLUGIN/infrastructuur.md` | HTML comment block preserved |
| `docs/implementaties/DataSHIELD/index.en.md` | `docs/implementaties/DataSHIELD/index.md` | Empty (nav commented out) |
| `docs/implementaties/DataSHIELD/informatie.en.md` | `docs/implementaties/DataSHIELD/informatie.md` | Empty (nav commented out) |
| `docs/implementaties/DataSHIELD/applicatie.en.md` | `docs/implementaties/DataSHIELD/applicatie.md` | Captions already in English; minor typo fix |
| `docs/discussie/index.en.md` | `docs/discussie/index.md` | |
| `docs/discussie/centraal-vs-decentraal.en.md` | `docs/discussie/centraal-vs-decentraal.md` | |
| `docs/discussie/primair-vs-secundair.en.md` | `docs/discussie/primair-vs-secundair.md` | |
| `docs/discussie/permit-vs-request.en.md` | `docs/discussie/permit-vs-request.md` | |
| `docs/discussie/dataspace-initiatieven.en.md` | `docs/discussie/dataspace-initiatieven.md` | |
| `docs/discussie/ontwikkelagenda.en.md` | `docs/discussie/ontwikkelagenda.md` | |
| `docs/appendix/index.en.md` | `docs/appendix/index.md` | Empty |
| `docs/appendix/tehdas2-hdab.en.md` | `docs/appendix/tehdas2-hdab.md` | PDF embed, no text to translate |
| `docs/appendix/tehdas2-spe.en.md` | `docs/appendix/tehdas2-spe.md` | PDF embed, no text to translate |

### Session 3 — Re-translation of pre-existing stub files

The following files existed before session 1 but contained incorrect, incomplete or empty content. They have been replaced with full translations of their Dutch source files.

| Updated file | Dutch source | Notes |
|-------------|--------------|-------|
| `docs/index.en.md` | `docs/index.md` | Previous content was a generic Health-RI intro stub; replaced with full Section 1 translation including LDN description, key concepts admonition (6 tabs), scope, EHDS timeline info box, and attribution |
| `docs/leeswijzer.en.md` | `docs/leeswijzer.md` | File was empty (0 bytes); filled with translation of research questions and reading guide |
| `docs/proces/index.en.md` | `docs/proces/index.md` | Previous content was an unrelated academic abstract; replaced with full process perspective translation including EHDS process steps, use-case methodology, and communication patterns info box |

`docs/waarom.en.md` (also listed as a stub) was reviewed against `docs/waarom.md` and found to be a faithful existing translation — left unchanged.

### Session 4 — Re-translation of remaining pre-existing stub files

The following files existed before session 1 but contained incorrect or empty content. They have been replaced with full translations of their Dutch source files.

| Updated file | Dutch source | Notes |
|-------------|--------------|-------|
| `docs/data-stations-als-hoeksteen.en.md` | `docs/data-stations-als-hoeksteen.md` | Previous content was an unrelated generic FAIR hourglass description with `[cite:]` tags; replaced with full Section 1.2 translation including hourglass model, FAIR principles admonition, five-layer description, data product admonition, and footnote |
| `docs/implementaties/index.en.md` | `docs/implementaties/index.md` | File was empty (0 bytes); filled with grid cards layout for KIK-V and PLUGIN implementations (DataSHIELD card kept commented out) |
| `docs/infrastructuur/standaarden.en.md` | `docs/infrastructuur/standaarden.md` | Previous content was outdated (missing `DuckLake` and `CSVW` entries, had `Kuzu` instead of `LadybugDB`, different intro text and section structure); replaced with full translation of the current Dutch source |

---

## Bug fixes

### Broken links in `implementaties/PLUGIN/proces.md` and `proces.en.md`

Three anchor links in the Dutch file pointed to non-existent section numbers (the use-case headings in `applicatie/data-station.md` had shifted from 4.1.3/4/5 to 4.1.5/6/7 at some point). The English translation initially inherited these stale links plus two additional path errors introduced during translation. All six links were corrected:

| File | Old anchor | Fixed anchor |
|------|-----------|--------------|
| `implementaties/PLUGIN/proces.md` | `#414-verwerk-algoritme-en-geef-resultaat-terug` | `#416-verwerk-algoritme-en-geef-resultaat-terug` |
| `implementaties/PLUGIN/proces.md` | `#415-geef-antwoord-op-dataverzoek` | `#417-geef-antwoord-op-dataverzoek` |
| `implementaties/PLUGIN/proces.md` | `#413-maak-data-beschikbaar-voor-secundair-gebruik` | `#415-maak-data-beschikbaar-voor-secundair-gebruik` |
| `implementaties/PLUGIN/proces.en.md` | `../applicatie/data-station.en.md#416-…` (wrong relative path) | `../../applicatie/data-station.md#416-process-algorithm-and-return-result` |
| `implementaties/PLUGIN/proces.en.md` | `../../applicatie/laag-3/data-station.md#415-…` (phantom path) | `../../applicatie/data-station.md#417-answer-data-request` |
| `implementaties/PLUGIN/proces.en.md` | `../../applicatie/laag-3/data-station.md#413-…` (phantom path) | `../../applicatie/data-station.md#415-make-data-available-for-secondary-use` |

---

## SVG diagram translations

### Approach

Draw.io-exported SVGs store each label in up to three redundant locations within the file:
1. As `value="..."` attributes inside a HTML-entity-encoded `<mxfile>` / `<mxGraphModel>` blob in the `content=` attribute on the `<svg>` root.
2. As literal text inside `<foreignObject><div>` elements in the SVG body (the visual rendering).
3. As `<text>` fallback elements inside `<switch>` blocks (older draw.io web exports only).

Some labels contain inline HTML with `&nbsp;` entities that split words across markup boundaries. The translation script normalises these before matching.

Plain Inkscape SVGs (`ehds-simpel.svg`) store text directly as `<text>` / `<tspan>` content nodes.

A one-shot Python script (`translate_svgs.py`, not committed) applied a ~100-entry Dutch→English dictionary across all three locations for each file.

### SVGs translated (18 `.en.svg` files created)

| Original SVG | English variant | Dutch labels |
|---|---|---|
| `docs/proces/uc-vinden.drawio.svg` | `uc-vinden.drawio.en.svg` | 8 |
| `docs/proces/uc-aanvragen.drawio.svg` | `uc-aanvragen.drawio.en.svg` | 13 |
| `docs/proces/uc-aanvragen-state.drawio.svg` | `uc-aanvragen-state.drawio.en.svg` | 19 |
| `docs/proces/uc-klaarzetten.drawio.svg` | `uc-klaarzetten.drawio.en.svg` | 2 |
| `docs/proces/uc-analyseren.drawio.svg` | `uc-analyseren.drawio.en.svg` | 9 |
| `docs/proces/uc-publiceren.drawio.svg` | `uc-publiceren.drawio.en.svg` | 5 |
| `docs/applicatie/datastation-4corner.drawio.svg` | `datastation-4corner.drawio.en.svg` | 9 |
| `docs/applicatie/datastation-netwerk.drawio.svg` | `datastation-netwerk.drawio.en.svg` | 5 |
| `docs/applicatie/uc-datastation.drawio.svg` | `uc-datastation.drawio.en.svg` | 10 |
| `docs/applicatie/datastation-beheren.drawio.svg` | `datastation-beheren.drawio.en.svg` | 5 |
| `docs/applicatie/datastation-ophalen.drawio.svg` | `datastation-ophalen.drawio.en.svg` | 4 |
| `docs/applicatie/datastation-organiseren.drawio.svg` | `datastation-organiseren.drawio.en.svg` | 12 |
| `docs/applicatie/datastation-klaarzetten.drawio.svg` | `datastation-klaarzetten.drawio.en.svg` | 8 |
| `docs/applicatie/datastation-analyseren.drawio.svg` | `datastation-analyseren.drawio.en.svg` | 7 |
| `docs/applicatie/datastation-leveren.drawio.svg` | `datastation-leveren.drawio.en.svg` | 7 |
| `docs/applicatie/datastation-dataverzoek.drawio.svg` | `datastation-dataverzoek.drawio.en.svg` | 7 |
| `docs/implementaties/PLUGIN/plugin-overzicht.drawio.svg` | `plugin-overzicht.drawio.en.svg` | 7 |
| `docs/ehds-simpel.svg` | `ehds-simpel.en.svg` | 4 |

### SVGs without `.en.svg` (no translation needed)

| SVG | Reason |
|-----|--------|
| `docs/proces/fair-hourglass.svg` | Text rendered as path geometry — no text nodes |
| `docs/implementaties/PLUGIN/vantage6-rollen.svg` | Already fully English |
| `docs/implementaties/kik-v.svg` | Logo, no text content |
| `docs/assets/noun-hourglass-7893158.svg` | Attribution text only |

### `.en.md` files updated (19 image references)

| File | References updated |
|------|--------------------|
| `docs/proces/publiceren.en.md` | 1 |
| `docs/proces/vinden.en.md` | 1 |
| `docs/proces/klaarzetten.en.md` | 1 |
| `docs/proces/aanvragen.en.md` | 2 |
| `docs/proces/analyseren.en.md` | 1 |
| `docs/applicatie/data-station.en.md` | 10 |
| `docs/implementaties/PLUGIN/applicatie.en.md` | 1 |
| `docs/implementaties/PLUGIN/index.en.md` | 1 |

Note: `docs/implementaties/PLUGIN/proces.en.md` references `vantage6-rollen.svg` which is already English — no change needed.

`docs/ehds-simpel.en.svg` was created for completeness but is not currently referenced by any `.en.md` file.

---

## Known limitations

- **Bibtex citation warnings**: `informatie/metadata.md` and `informatie/metadata.en.md` contain Turtle (RDF) code blocks with `@prefix`, `@nl` and `@en` language tags. The `mkdocs-bibtex` plugin mistakenly scans these as citation keys, producing four `WARNING - Inline reference to unknown key` messages per build. This is a known plugin limitation and the warnings are harmless.

---

## Total files

| Category | Count |
|----------|-------|
| Infrastructure files modified/created | 4 |
| Pre-existing English files (untouched) | 2 |
| English translations created — session 1 | 18 |
| English translations created — session 2 | 25 |
| Pre-existing stub files re-translated — session 3 | 3 |
| Pre-existing stub files re-translated — session 4 | 3 |
| **Total `.en.md` files in project** | **51** |
| English SVG diagrams created | 18 |
| **Total `.en.svg` files in project** | **18** |
