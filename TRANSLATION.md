# Translation Log: Dutch → English

This document records all actions taken to translate the MkDocs documentation project from Dutch into English for the [data-station-specification](https://github.com/health-ri/data-station-specification) repository.

## Goal

Translate the entire MkDocs project from Dutch into English. The project is a technical specification document for "Data stations for secondary use of health data" (EHDS/health data infrastructure). The i18n infrastructure uses `mkdocs-static-i18n` v1.3.0 with `docs_structure: suffix`, meaning `filename.md` is Dutch and `filename.en.md` is English.

---

## Translation approach

- Direct AI-assisted translation, preserving technical terminology, markdown formatting and internal links.
- BibTeX citation keys (`[@key]`), SVG/image references, admonitions, footnotes and mermaid/tab content blocks are preserved exactly as-is.
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

These files already existed in English before work began:

| File |
|------|
| `docs/index.en.md` |
| `docs/leeswijzer.en.md` |
| `docs/data-stations-als-hoeksteen.en.md` |
| `docs/infrastructuur/standaarden.en.md` |
| `docs/proces/index.en.md` |
| `docs/implementaties/index.en.md` |
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

---

## Total files

| Category | Count |
|----------|-------|
| Infrastructure files modified/created | 4 |
| Pre-existing English files (untouched) | 8 |
| English translations created — session 1 | 18 |
| English translations created — session 2 | 25 |
| **Total `.en.md` files in project** | **51** |
