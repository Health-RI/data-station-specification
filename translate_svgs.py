#!/usr/bin/env python3
"""
One-shot script to produce .en.svg translations of all Dutch SVG diagrams.
Run from the project root: python3 translate_svgs.py
"""

import re
import html
from pathlib import Path

# ---------------------------------------------------------------------------
# Translation dictionary — Dutch → English
# Ordered longest-first to avoid partial replacements of shorter substrings.
# ---------------------------------------------------------------------------

TRANSLATIONS = {
    # --- Full sentences / long phrases ---
    "een afgewezen aanvraag voor een vergunning kan als gegevensverzoek wel toegewezen worden": "a rejected permit application may still be approved as a data request",
    "Niet volledig, reactie niet ontvangen of reactie is onvoldoende": "Not complete, no response received, or response is insufficient",
    "Register met Verzoek van natuurlijke personen om niet geïnformeerd te worden over bevindingen": "Register of natural persons' requests not to be informed of findings",
    "Registreer en bezorg significante bevinding over een individu": "Register and deliver significant finding about an individual",
    "Update Nationale catalogus met catalogussen van dataleveranciers": "Update national catalogue with data holder catalogues",
    "Stel data beschikbaar in centrale beveiligde verwerkingsomgeving": "Make data available in central secure processing environment",
    "Haal periodiek catalogus van datasets op": "Periodically retrieve dataset catalogue",
    "Meld significante bevinding over een individu": "Report significant finding about an individual",
    "Meld publicatie van onderzoeksresultaten": "Report publication of research results",
    "Voer gefedereerd een algoritme uit": "Execute an algorithm in a federated manner",
    "Voer gecentraliseerd een algoritme uit": "Execute an algorithm centrally",
    "als algoritme centraal moet worden uitgevoerd (data pooling)": "when algorithm must be executed centrally (data pooling)",
    "Maak data beschikbaar voor secundair gebruik": "Make data available for secondary use",
    "Verwerk algoritme en geef resultaat terug": "Process algorithm and return result",
    "Datasets die aangeboden worden in de datacatalogus": "Datasets offered in the data catalogue",
    "Nationale catalogus van datasets (HDAB generieke functie)": "National dataset catalogue (HDAB generic function)",
    "Nationale catalogus van datasets": "National dataset catalogue",
    "Nationaal contactpunt voor secundair gebruik": "National contact point for secondary use",
    "Instantie voor toegang tot gezondheidsgegevens (HDAB)": "Health Data Access Body (HDAB)",
    "Verstrek vergunning of toestemming": "Grant permit or consent",
    "Vraag (toegang tot) gezondheidsgegevens aan": "Request (access to) health data",
    "Raadpleeg ingediende aanvragen": "View submitted requests",
    "Trek attestatie in": "Revoke attestation",
    "Geef antwoord op dataverzoek": "Answer data request",
    "Beheer catalogus van datasets": "Manage dataset catalogue",
    "aanmaken of uploaden catalogus": "create or upload catalogue",
    "ok := aanmelden catalogus": "ok := register catalogue",
    "verifiëren deelnemercredentials en goedkeuring dataverzoek": "verify participant credentials and approval of data request",
    "verifiëren deelnemercredentials en datavergunning": "verify participant credentials and data permit",
    "verifiëren deelnemercredentials": "verify participant credentials",
    "registreren datacatalogus van dataleverancier": "register data catalogue of data holder",
    "ophalen adres van Nationale catalogus": "retrieve address of national catalogue",
    "catalogus := ophalen catalogus": "catalogue := retrieve catalogue",
    "Update Nationale catalogus": "Update national catalogue",
    "catalogus vrijgeven": "release catalogue",
    "opdracht om data beschikbaar te stellen": "instruction to make data available",
    "ok := notificatie dat data gedownload kan worden": "ok := notification that data can be downloaded",
    "ok := notificatie dat data beschikbaar is met omgevingsvariabelen": "ok := notification that data is available with environment variables",
    "Overbrugging van tijd": "Time bridging",
    "verificatie datavergunning": "data permit verification",
    "integreren dataset in de data pool": "integrate dataset into the data pool",
    "dataset := downloaden dataset": "dataset := download dataset",
    "configureren omgeving en toegangsregels tot data": "configure environment and data access rules",
    "opdracht geven tot uitvoering": "issue execution instruction",
    "verifiëren integriteit dataverzoek": "verify integrity of data request",
    "uitvoeren dataverzoek": "execute data request",
    "ophalen algoritme (query)": "retrieve algorithm (query)",
    "verifiëren integriteit algoritme": "verify integrity of algorithm",
    "ophalen algoritme (docker image)": "retrieve algorithm (docker image)",
    "uitvoeren algoritme": "execute algorithm",
    "niet uitgezonderd door artikel 50 EHDS": "not exempted by Article 50 EHDS",
    "Niet uitgezonderd door artikel 50 EHDS": "Not exempted by Article 50 EHDS",
    "... levert een knooppunt met een datastation voor aansluiting op de dataspace aan ...": "... provides a node with a data station for connection to the dataspace ...",
    "... is een ... van de dataspace voor secundair gebruik": "... is a ... of the dataspace for secondary use",
    "... wordt gefaciliteerd door ...": "... is facilitated by ...",
    "Gebruiker van gezondheidsgegevens": "Health data user",
    "Natuurlijk persoon of rechtspersoon": "Natural or legal person",
    "Registreer algoritme": "Register algorithm",
    "Voer dataverzoek uit": "Execute data request",
    "Geef resultaten vrij": "Release results",
    "Algoritmeregister": "Algorithm registry",
    "Ontvangst aanvraag": "Request received",
    "In behandeling": "In progress",
    "Aanvraag is volledig": "Request is complete",
    "Verzoek om aanvullende informatie": "Request for additional information",
    "Reactie ontvangen": "Response received",
    "Ter beoordeling": "Under review",
    "Start vooronderzoek": "Start preliminary review",
    "In onderzoek": "Under investigation",
    "Aanvraag is onvolledig": "Request is incomplete",
    "Start beoordeling": "Start assessment",
    "Beoordeling positief": "Assessment positive",
    "Aanvraag ingetrokken": "Request withdrawn",
    "Geen beoordeling": "No assessment",
    "Meld catalogus aan": "Register catalogue",
    "Zoek datasets": "Search datasets",
    "Potentiële aanvrager": "Potential applicant",
    # --- Shorter labels ---
    "Datagebruikers voeren": "Data users perform",
    "analyses uit op": "analyses on",
    "gezondheidsgegevens": "health data",
    "in een processing hub": "in a processing hub",
    "die voldoet aan de vereisten van de EHDS": "that meets the requirements of the EHDS",
    "start: vergunningsverlening door HDAB": "start: permit granting by HDAB",
    "eind: output controle en publicatie": "end: output control and publication",
    "Data governance principes": "Data governance principles",
    "dat is verbonden verschillende datastations": "that is connected to various data stations",
    "die worden beheerd door de data houders": "that are managed by the data holders",
    "Knooppunt Dataleverancier": "Data holder node",
    "Knooppunt HDAB": "HDAB node",
    "Werkomgeving voor analyse": "Analysis workspace",
    "Werkomgeving voor leren": "Learning workspace",
    "Werkomgeving voor ...": "Workspace for ...",
    "Regionaal samenwerkingsverband": "Regional collaboration",
    "Service medewerker": "Service employee",
    "Data Integratie Transformatie Aggregatie": "Data Integration Transformation Aggregation",
    "Data Preparatie": "Data Preparation",
    "Datagebruiker": "Data user",
    "Dataleverancier": "Data holder",
    "Datahouder": "Data holder",
    "Databronnen": "Data sources",
    "Behandelaar": "Handler",
    "Beoordelaar": "Assessor",
    "Aanvrager": "Applicant",
    "Deelnemer": "Participant",
    "Dienstverlener": "Service provider",
    "Datastation": "Data station",
    "Knooppunt": "Node",
    "datapreparatie": "data preparation",
    "resultaat": "result",
    "Analyseren": "Analyse",
    "Leveren": "Deliver",
    "Organiseren": "Organise",
    "Verkrijgen": "Acquire",
    "Documenten": "Documents",
    "Beelden": "Images",
    "Bestand": "File",
    "Gereed": "Ready",
    "Ingediend": "Submitted",
    "Volledig": "Complete",
    "Wachtend": "Waiting",
    "Onvolledig": "Incomplete",
    "Afgewezen": "Rejected",
    "Toegewezen": "Approved",
    "Publiek": "Public",
    "Tijd": "Time",
    # Elektronisch patiënten- of cliëntendossier (needs care with special chars)
    "Elektronisch patiënten- of cliëntendossier": "Electronic patient or client record",
}

# Sort by descending length to avoid partial-match issues
SORTED_TRANSLATIONS = sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0]))


def translate_string(text: str) -> str:
    """Replace all Dutch strings with English equivalents."""
    for dutch, english in SORTED_TRANSLATIONS:
        text = text.replace(dutch, english)
    return text


def translate_value_attr(val_xml: str) -> str:
    """
    Translate the inner XML of a mxCell value="..." attribute.
    The value may contain HTML markup with &nbsp; entities splitting words.
    Strategy: fully decode inner HTML, strip tags to get plain text, translate,
    then reconstruct (keeping any surrounding HTML structure intact if possible).
    For simple plain-text values this is a no-op pass-through if no Dutch found.
    For values with embedded HTML we normalise &nbsp; → space, strip tags,
    translate, then re-encode.
    """
    # Decode inner HTML entities one level
    decoded = html.unescape(val_xml)
    # Normalise non-breaking spaces to regular spaces
    decoded_norm = decoded.replace("\u00a0", " ").replace("&nbsp;", " ")
    # Strip HTML tags for comparison
    plain = re.sub(r"<[^>]+>", " ", decoded_norm)
    plain = re.sub(r"\s+", " ", plain).strip()
    # Try direct translation on the normalised plain text
    translated_plain = translate_string(plain)
    if translated_plain != plain:
        # Something changed — return the translated plain text (tags stripped out)
        # Re-encode for use inside value="" attribute XML
        return translated_plain
    # Nothing changed — return the original decoded (without extra normalisation)
    # but still run translate_string on it for simple cases
    return translate_string(decoded)


def translate_svg_drawio(content: str) -> str:
    """
    Translate a draw.io-exported SVG.
    Text appears in three locations:
      1. content= attribute (HTML-entity-encoded mxGraphModel XML)
      2. <foreignObject> / <div> body
      3. <text> fallback elements (older draw.io exports)
    """

    # --- Location 1: content= attribute ---
    # The attribute value is HTML-entity-encoded. We decode → translate → re-encode.
    def replace_content_attr(m):
        raw = m.group(1)
        decoded = html.unescape(raw)

        # Translate value="..." attributes inside the mxGraphModel XML,
        # handling embedded HTML with &nbsp; etc.
        def replace_mxcell_value(vm):
            inner = vm.group(1)
            translated = translate_value_attr(inner)
            return f'value="{translated}"'

        translated = re.sub(r'value="([^"]*)"', replace_mxcell_value, decoded)
        # Also translate any remaining plain text (tooltips, labels not in value=)
        translated = translate_string(translated)

        encoded = (
            translated.replace("&", "&amp;")
            .replace('"', "&quot;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "&#10;")
        )
        return f'content="{encoded}"'

    content = re.sub(r'content="([^"]*)"', replace_content_attr, content)

    # --- Location 2: foreignObject / div body ---
    # Labels appear as literal text nodes inside <div> elements. We translate
    # all text nodes that appear between tags (but not attribute values, which
    # are already handled in location 1 as part of the content= blob).
    # Strategy: translate text between > and < that is not inside a tag.
    def replace_text_node(m):
        text = m.group(1)
        translated = translate_string(text)
        return f">{translated}<"

    content = re.sub(r">([^<>]+)<", replace_text_node, content)

    return content


def translate_svg_inkscape(content: str) -> str:
    """
    Translate a plain Inkscape SVG.
    All text is in <text> / <tspan> text nodes — same approach: replace text
    between > and <.
    """

    def replace_text_node(m):
        text = m.group(1)
        translated = translate_string(text)
        return f">{translated}<"

    content = re.sub(r">([^<>]+)<", replace_text_node, content)
    return content


# ---------------------------------------------------------------------------
# SVG files to translate
# ---------------------------------------------------------------------------

PROJECT = Path(__file__).parent

DRAWIO_SVGS = [
    "docs/proces/uc-publiceren.drawio.svg",
    "docs/proces/uc-aanvragen.drawio.svg",
    "docs/proces/uc-aanvragen-state.drawio.svg",
    "docs/proces/uc-vinden.drawio.svg",
    "docs/proces/uc-klaarzetten.drawio.svg",
    "docs/proces/uc-analyseren.drawio.svg",
    "docs/applicatie/datastation-4corner.drawio.svg",
    "docs/applicatie/datastation-netwerk.drawio.svg",
    "docs/applicatie/uc-datastation.drawio.svg",
    "docs/applicatie/datastation-beheren.drawio.svg",
    "docs/applicatie/datastation-ophalen.drawio.svg",
    "docs/applicatie/datastation-klaarzetten.drawio.svg",
    "docs/applicatie/datastation-dataverzoek.drawio.svg",
    "docs/applicatie/datastation-analyseren.drawio.svg",
    "docs/applicatie/datastation-leveren.drawio.svg",
    "docs/applicatie/datastation-organiseren.drawio.svg",
    "docs/implementaties/PLUGIN/plugin-overzicht.drawio.svg",
]

INKSCAPE_SVGS = [
    "docs/ehds-simpel.svg",
]


def make_en_path(src: Path) -> Path:
    """foo.drawio.svg → foo.drawio.en.svg  |  foo.svg → foo.en.svg"""
    name = src.name
    if name.endswith(".drawio.svg"):
        en_name = name[: -len(".drawio.svg")] + ".drawio.en.svg"
    else:
        en_name = name[: -len(".svg")] + ".en.svg"
    return src.parent / en_name


def process_file(rel_path: str, translator):
    src = PROJECT / rel_path
    dst = make_en_path(src)
    content = src.read_text(encoding="utf-8")
    translated = translator(content)
    dst.write_text(translated, encoding="utf-8")
    # Report changed labels
    changed = sum(
        1
        for dutch, english in SORTED_TRANSLATIONS
        if dutch in content and english in translated and dutch not in translated
    )
    print(f"  {src.name} → {dst.name}  ({changed} substitution types applied)")


if __name__ == "__main__":
    print("Translating draw.io SVGs...")
    for rel in DRAWIO_SVGS:
        process_file(rel, translate_svg_drawio)

    print("\nTranslating Inkscape SVGs...")
    for rel in INKSCAPE_SVGS:
        process_file(rel, translate_svg_inkscape)

    print("\nDone.")
