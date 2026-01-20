# 3.3. Metadata interoperabiliteit

## 3.3.1. Waarom metadata essentieel is voor datastations

Metadata speelt een cruciale rol in een datastation. Zonder goede metadata weten onderzoekers en systemen niet welke data beschikbaar is, wat de kwaliteit ervan is, en onder welke voorwaarden deze gebruikt mag worden. Metadata maakt het mogelijk om:

- **Datasets te vinden**: Een onderzoeker kan in een catalogus zoeken naar datasets over hartfalen in een bepaalde leeftijdsgroep.
- **Datasets te begrijpen**: De beschrijving vertelt welke variabelen er zijn, hoe de data is verzameld, en welke beperkingen er gelden.
- **Datasets automatisch te verwerken**: Systemen kunnen op basis van gestandaardiseerde metadata beoordelen of een dataset geschikt is voor een bepaalde analyse.

Voor het realiseren van interoperabiliteit tussen datastations is het van groot belang dat metadata op een gestandaardiseerde manier wordt beschreven. Hiervoor zijn internationale standaarden en profielen ontwikkeld.

=== "**DCAT**"

    **DCAT** (Data Catalog Vocabulary) is een W3C-standaard die oorspronkelijk is ontworpen voor het beschrijven van datasets in datacatalogi. Het biedt een gemeenschappelijk vocabulaire waarmee organisaties hun datasets kunnen beschrijven, ongeacht het domein. DCAT versie 3 (2024) introduceert onder andere de `DatasetSeries` klasse voor het beschrijven van gerelateerde datasets.

=== "**DCAT-AP**"

    **DCAT-AP** is een Europees applicatieprofiel van DCAT, ontwikkeld door de Europese Commissie. Het verfijnt DCAT met extra verplichte en aanbevolen velden die relevant zijn voor Europese overheidsdata, zoals toegangsrechten en toepasselijke wetgeving. DCAT-AP vormt de basis voor veel nationale datacatalogi.

=== "**HealthDCAT-AP**"

    **HealthDCAT-AP** is een uitbreiding van DCAT-AP specifiek voor de gezondheidszorgsector. Het voegt metadata-elementen toe die essentieel zijn voor gezondheidsdata, zoals:

    - Gezondheidscategorieën (EHR, beelden, genomische data)
    - Populatiekenmerken (leeftijdsbereik, aantal unieke individuen)
    - Coderingssystemen (SNOMED CT, ICD-10, LOINC)
    - Retentieperiodes en bewaartermijnen
    - De verantwoordelijke Health Data Access Body (HDAB)

=== "**Health-RI metadata schema**"

    Het **Health-RI metadata schema** is een Nederlands profiel gebaseerd op DCAT-AP en HealthDCAT-AP, met specifieke aanpassingen voor de Health-RI Datacatalogus. Dit schema definieert welke metadata-elementen verplicht, aanbevolen of optioneel zijn voor Nederlandse gezondheidsdata.

## 3.3.2. DCAT-klassen in een datastation

In DCAT worden verschillende klassen gebruikt om de structuur van een datacatalogus te beschrijven. Voor datastations zijn de volgende klassen het meest relevant.

**De catalogus: `dcat:Catalog`**

Een `dcat:Catalog` vertegenwoordigt het datastation zelf als een verzameling van datasets en dataservices. De catalogus fungeert als het toegangspunt voor gebruikers en systemen die willen weten welke data beschikbaar is. De catalogus beschrijft niet alleen welke datasets er zijn, maar ook via welke services deze toegankelijk zijn. De volgende eigenschappen zijn essentieel voor een catalogus:

| Eigenschap        | Beschrijving                            | Voorbeeld                                         |
| ----------------- | --------------------------------------- | ------------------------------------------------- |
| `dct:title`       | Naam van de catalogus                   | "Data Catalogus Ziekenhuis X"                     |
| `dct:description` | Beschrijving van de inhoud              | "Catalogus met klinische datasets voor onderzoek" |
| `dct:publisher`   | Organisatie die de catalogus publiceert | Ziekenhuis X                                      |
| `dcat:dataset`    | Verwijzingen naar datasets              | Links naar beschikbare datasets                   |
| `dcat:service`    | Verwijzingen naar dataservices          | Links naar API-endpoints                          |

In de praktijk kan één organisatie meerdere catalogi hebben. Bijvoorbeeld een ziekenhuis kan een catalogus hebben voor beeldvormende data (MRI, CT, PET) en een aparte catalogus voor klinische data uit het EPD.

**De dataset: `dcat:Dataset`**

Een `dcat:Dataset` vertegenwoordigt een logische verzameling van gegevens die als eenheid wordt beschreven en beschikbaar gesteld. De granulariteit van een dataset is niet technisch voorgeschreven, maar wordt bepaald door de organisatie van de dataleverancier en de manier waarop onderzoekers de data willen kunnen vinden en aanvragen. Datasets kunnen bijvoorbeeld worden georganiseerd:

- **Per ziektebeeld**: "COVID-19 opnamegegevens 2020-2024"
- **Per domein**: "Cardiologie patiëntgegevens"
- **Per onderzoeksproject**: "IMPROVE-studie diabetes cohort"

Voor datasets in de gezondheidszorg zijn de volgende metadata-elementen in het bijzonder relevant:

| Categorie        | HealthDCAT-AP elementen                                                                                | Doel                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Populatie**    | `numberOfUniqueIndividuals`, `numberOfRecords`, `populationCoverage`, `minTypicalAge`, `maxTypicalAge` | Inzicht in omvang en samenstelling                              |
| **Terminologie** | `hasCodingSystem`                                                                                      | Welke coderingssystemen worden gebruikt (SNOMED, ICD-10, LOINC) |
| **Juridisch**    | `accessRights`, `applicableLegislation`                                                                | Toegangsvoorwaarden en wetgeving (EHDS, AVG)                    |
| **Kwaliteit**    | `hasQualityAnnotation`                                                                                 | Verwijzing naar kwaliteitsrapportage                            |
| **Privacy**      | `retentionPeriod`, `hdab`                                                                              | Bewaartermijn en verantwoordelijke instantie                    |

**De dataset serie: `dcat:DatasetSeries`**

De klasse `dcat:DatasetSeries` is bedoeld voor het beschrijven van verzamelingen van gerelateerde datasets die afzonderlijk worden gepubliceerd maar logisch samenhangen. Dit is bijzonder geschikt voor:

- **Periodieke cohorten**: Jaarlijks gepubliceerde extracties van dezelfde patiëntpopulatie
- **Versies van onderzoeksdatasets**: Opeenvolgende versies van een cohort na correcties of uitbreidingen
- **Longitudinale data**: Meetmomenten in een follow-up studie

De serie definieert gemeenschappelijke metadata (zoals toegangsrechten en coderingssystemen), terwijl individuele datasets hun specifieke kenmerken behouden (zoals het aantal records en de temporele dekking).

**De distributie: `dcat:Distribution`**

Een `dcat:Distribution` beschrijft een concrete realisatie van een dataset: hoe de data daadwerkelijk kan worden verkregen of benaderd. Eén dataset kan meerdere distributies hebben:

| Type distributie        | Beschrijving                                | Typisch gebruik                          |
| ----------------------- | ------------------------------------------- | ---------------------------------------- |
| **Bulk export**         | Eenmalige download van de volledige dataset | Onderzoek in een centrale BVO            |
| **API-toegang**         | Programmatische toegang via een service     | Federatieve analyse                      |
| **Synthetische sample** | Representatieve testdata                    | Ontwikkeling en validatie van algoritmes |
| **View/subset**         | Voorgedefinieerde selectie                  | Specifiek onderzoeksdoel                 |

De distributie specificeert technische details zoals het bestandsformaat (`dcat:mediaType`), de toegangs-URL (`dcat:accessURL`), en eventueel een verwijzing naar de onderliggende dataservice.

**De dataservice: `dcat:DataService`**

Een `dcat:DataService` beschrijft een operationele service die toegang biedt tot datasets. Waar een distributie een statische momentopname of downloadbaar bestand vertegenwoordigt, biedt een dataservice dynamische toegang tot de onderliggende data. De service kan realtime queries uitvoeren, actuele data opvragen, of zelfs berekeningen uitvoeren zonder dat de data het datastation verlaat. Verschillende typen dataservices zijn mogelijk, bijvoorbeeld:

| Type dataservice        | Voorbeeld                        | Beschrijving                                |
| ----------------------- | -------------------------------- | ------------------------------------------- |
| **FHIR API**            | `https://fhir.example.org/`      | REST API volgens HL7 FHIR standaard         |
| **OMOP query service**  | SQL-interface voor OMOP-CDM      | Gestandaardiseerde queries op OMOP-database |
| **DICOM WADO-RS**       | Web access voor medische beelden | Ophalen van beelden via web protocol        |
| **Federatief endpoint** | KIK-V of PLUGIN-node             | Ontvangst en uitvoering van algoritmes      |

Voor automatische verwerking door systemen is het essentieel dat de dataservice duidelijk maakt _hoe_ deze benaderd kan worden. Dit wordt gedaan via:

- `dcat:endpointURL`: Het basisadres van de service
- `dcat:endpointDescription`: Link naar de technische documentatie (bijv. OpenAPI specificatie of FHIR CapabilityStatement)
- `dct:conformsTo`: De standaard waaraan de service voldoet

## 3.3.3. Statische versus dynamische databronnen

Een belangrijk onderscheid bij het modelleren van databronnen is het verschil tussen _statische_ en _dynamische_ databronnen. Dit onderscheid heeft directe gevolgen voor hoe metadata wordt beheerd en hoe versiebeheer wordt toegepast.

**Statische databronnen: cohorten en extracties**

Statische databronnen zijn datasets die op een bepaald moment zijn gedefinieerd en geëxtraheerd. De data verandert na extractie niet meer, wat zorgt voor reproduceerbaarheid van onderzoeksresultaten. Dit type databron is gebruikelijk bij onderzoeksprojecten waar een vaste populatie en observatieperiode worden gedefinieerd. Typische voorbeelden van statische databronnen zijn:

- **Onderzoekscohorten**: Een vooraf gedefinieerde groep patiënten voor een specifieke studie
- **Periodieke snapshots**: Jaarlijkse of kwartaal-extracties van een bronsysteem
- **Geanonimiseerde datasets**: Eenmalig gegenereerde datasets voor open onderzoek

Voor statische databronnen is expliciet versiebeheer essentieel:

| Eigenschap      | Gebruik                       | Voorbeeld                                 |
| --------------- | ----------------------------- | ----------------------------------------- |
| `dcat:version`  | Versienummer van de dataset   | "2024.1"                                  |
| `dct:issued`    | Datum van publicatie          | "2024-03-15"                              |
| `dct:modified`  | Datum van laatste wijziging   | "2024-03-20"                              |
| `dcat:inSeries` | Koppeling aan een serie       | Link naar de overkoepelende DatasetSeries |
| `dcat:prev`     | Verwijzing naar vorige versie | Link naar vorige dataset                  |

De DatasetSeries klasse is bijzonder nuttig voor statische databronnen wanneer:

1. Er periodiek nieuwe versies van dezelfde soort data worden gepubliceerd
2. Onderzoekers de mogelijkheid moeten hebben om specifieke versies te selecteren
3. Er gemeenschappelijke metadata is die op serie-niveau kan worden gedefinieerd

**Dynamische databronnen: actieve databases**

Dynamische databronnen zijn databases die continu worden bijgewerkt, zoals EPD-systemen, OMOP-CDM databases of XNAT-omgevingen. Het is hier niet zinvol om bij elke data-wijziging een nieuwe versie aan te maken.

Voor dynamische databronnen adviseren we de volgende aanpak:

| Aspect                     | Aanbeveling                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **De database als geheel** | Beschrijf als `dcat:Dataset` met `dcat:accrualPeriodicity` om de update-frequentie aan te geven                            |
| **Versiebeheer**           | Gebruik `dcat:version` alleen voor _structurele_ wijzigingen (bijv. upgrade van OMOP CDM v5.3 naar v5.4)                   |
| **Temporele dekking**      | Gebruik `dct:temporal` met alleen een startdatum (geen einddatum) om aan te geven dat de data actief groeit                |
| **Statistieken**           | Update periodiek de populatiestatistieken (`numberOfRecords`, `numberOfUniqueIndividuals`) met bijbehorende `dct:modified` |
| **Schema-documentatie**    | Beschrijf via `dcat:Distribution` met verwijzing naar schema-documentatie                                                  |

??? example "Praktijkvoorbeeld: versioning strategie"

    Een ziekenhuis heeft een OMOP-CDM database die dagelijks wordt bijgewerkt met nieuwe patiëntgegevens. De metadata wordt als volgt beheerd:

    - **Schema-versie**: `dcat:version` = "OMOP CDM v5.4" – wijzigt alleen bij upgrade van het datamodel
    - **Update-frequentie**: `dcat:accrualPeriodicity` = DAILY – geeft aan dat data dagelijks wordt toegevoegd
    - **Statistieken**: `numberOfRecords` en `numberOfUniqueIndividuals` worden maandelijks bijgewerkt, met `dct:modified` op de bijgewerkte datum
    - **Temporele dekking**: `dct:temporal` met startdatum 2018-01-01 en geen einddatum

## 3.3.4. Metadata voor primair versus secundair gebruik

Bij het beschrijven van metadata is het belangrijk om onderscheid te maken tussen primair en secundair gebruik van gegevens. Dit onderscheid beïnvloedt welke metadata-elementen de nadruk krijgen.

**Primair gebruik: focus op de service**

Voor primair gebruik (directe zorgverlening) blijven bronsystemen leidend. In DCAT wordt vooral beschreven _wat_ er beschikbaar is en _hoe_ het kan worden geraadpleegd. Omdat niet voor elke individuele patiënt een dataset wordt aangemaakt, ligt de nadruk op het beschrijven van het bronsysteem en de bijbehorende dataservice.

De `dcat:DataService` speelt hier een centrale rol. Het is van belang dat de service goed wordt beschreven, zodat een vragend systeem (bijvoorbeeld een ander EPD of een zorgapplicatie) de data correct kan opvragen en gebruiken.

**Secundair gebruik: focus op inhoud en context**

Voor secundair gebruik (onderzoek, beleid, innovatie) verschuift de nadruk naar de _inhoud_ en _kwaliteit_ van de data, evenals de context waarin de gegevens zijn verzameld. HealthDCAT-AP maakt expliciete modellering van deze aspecten mogelijk:

| Aspect                    | HealthDCAT-AP elementen                                              |
| ------------------------- | -------------------------------------------------------------------- |
| **Toegangsrechten**       | `NON_PUBLIC`, `RESTRICTED`, `PUBLIC`                                 |
| **Wetgeving**             | Verwijzingen naar EHDS, AVG, nationale wetten                        |
| **Doelbinding**           | `dpv:hasPurpose` (bijv. academisch onderzoek, volksgezondheid)       |
| **Rechtmatige grondslag** | `dpv:hasLegalBasis` (bijv. publiek belang, toestemming)              |
| **Kwaliteit**             | Verwijzing naar kwaliteitsrapportages via `dqv:hasQualityAnnotation` |
| **HDAB**                  | `healthdcatap:hdab` – de verantwoordelijke Health Data Access Body   |

**Endpoint descriptions voor automatische verwerking**

Wanneer een catalogus browser of federatieve query-engine automatisch de mogelijkheden van een dataservice wil bepalen, moet bekend zijn welk type specificatie de `dcat:endpointDescription` bevat. Een FHIR CapabilityStatement heeft bijvoorbeeld een andere structuur dan een OpenAPI specificatie, en systemen moeten weten hoe ze deze moeten interpreteren. Door het type specificatie expliciet te maken met `dct:conformsTo`, kan een systeem de juiste keuze maken en de beschikbare mogelijkheden ontdekken.

???+ success "Combineren van endpointDescription met conformsTo"

    Combineer `dcat:endpointDescription` altijd met `dct:conformsTo` om het type specificatie expliciet te maken:

    ```turtle
    <https://example.org/service/fhir-api> a dcat:DataService ;
        dcat:endpointURL <https://fhir.example.org/> ;
        dcat:endpointDescription <https://fhir.example.org/metadata> ;
        # Expliciet aangeven dat het een FHIR CapabilityStatement betreft
        dct:conformsTo <http://hl7.org/fhir/StructureDefinition/CapabilityStatement> .

    <https://example.org/service/rest-api> a dcat:DataService ;
        dcat:endpointURL <https://api.example.org/> ;
        dcat:endpointDescription <https://api.example.org/openapi.json> ;
        # Expliciet aangeven dat het een OpenAPI specificatie betreft
        dct:conformsTo <https://spec.openapis.org/oas/v3.1.0> .
    ```

## 3.3.5. Voorbeelden van metadata voor een datastation

De volgende voorbeelden illustreren hoe verschillende typen databronnen in een datastation kunnen worden beschreven met DCAT en HealthDCAT-AP. Elk voorbeeld demonstreert specifieke aspecten van de standaard.

??? example "Voorbeeld 1: FHIR-systeem (dynamische databron)"

    Een FHIR-systeem in een ziekenhuis kan op verschillende manieren worden ontsloten. In dit voorbeeld wordt een COVID-19 dataset beschreven die dynamisch groeit naarmate er nieuwe opnames worden geregistreerd.

    **Kenmerken van dit voorbeeld:**

    - Dynamische dataset met dagelijkse updates
    - Secundair gebruik met beperkte toegang
    - Volledige HealthDCAT-AP metadata inclusief populatiekenmerken en coderingssystemen
    - Kwaliteitsrapportage gekoppeld via DQV

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix dqv: <http://www.w3.org/ns/dqv#> .
    @prefix oa: <http://www.w3.org/ns/oa#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    # De catalogus: vertegenwoordigt het datastation
    <https://example.org/catalog/fhir> a dcat:Catalog ;
        dct:title "Catalogus – FHIR (voorbeeld)"@nl ;
        dct:description "Catalogus met FHIR-gebaseerde datasets van Ziekenhuis X."@nl ;
        dcat:dataset <https://example.org/dataset/fhir-covid-admissions> ;
        dcat:service <https://example.org/service/fhir-api> .

    # De dataset: COVID-19 opnamegegevens
    <https://example.org/dataset/fhir-covid-admissions> a dcat:Dataset ;
        dct:title "Dataset – COVID-19 opnames (FHIR, secundair gebruik)"@nl ;
        dct:description "Dynamische dataset met COVID-19 opnamegegevens uit het EPD-systeem van Ziekenhuis X. Bevat demografische gegevens, opname-informatie, diagnoses en behandelingen."@nl ;

        # Dynamische dataset: update frequentie in plaats van versie per wijziging
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/DAILY> ;

        # Toegangsrechten en toepasselijke wetgeving
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,  # EHDS Regulation
            <http://data.europa.eu/eli/reg/2016/679/oj> ; # AVG/GDPR

        # Gezondheidscategorie en verantwoordelijke HDAB
        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;

        # Populatiekenmerken (periodiek bijgewerkt)
        healthdcatap:numberOfUniqueIndividuals "85000"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "430000"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Opnames van volwassen patiënten met bevestigde COVID-19 diagnose in Ziekenhuis X."@nl ;
        healthdcatap:minTypicalAge "18"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "95"^^xsd:nonNegativeInteger ;

        # Temporele dekking: groeiende dataset zonder einddatum
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2020-03-01"^^xsd:date
        ] ;

        # Gebruikte coderingssystemen voor semantische interoperabiliteit
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q45127>,   # ICD-10
            <https://www.wikidata.org/wiki/Q1753883>, # SNOMED CT
            <https://www.wikidata.org/wiki/Q502480> ; # LOINC

        # Doelbinding en rechtmatige grondslag (Data Privacy Vocabulary)
        dpv:hasPurpose dpv:AcademicResearch, dpv:PublicHealth ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dpv:hasPersonalData dpv:HealthData ;

        # Bewaartermijn
        healthdcatap:retentionPeriod [
            a dct:PeriodOfTime ;
            dcat:startDate "2020-03-01"^^xsd:date ;
            dcat:endDate "2030-03-01"^^xsd:date
        ] ;

        # Kwaliteitsrapportage
        dqv:hasQualityAnnotation <https://example.org/qualitycertificate/fhir-covid-dq-report> ;

        dcat:distribution <https://example.org/distribution/fhir-covid-bulk> .

    # Kwaliteitsrapport
    <https://example.org/qualitycertificate/fhir-covid-dq-report> a dqv:QualityCertificate ;
        dct:title "Kwaliteitsrapport – COVID-19 opnames (FHIR)"@nl ;
        oa:hasTarget <https://example.org/dataset/fhir-covid-admissions> ;
        oa:hasBody <https://example.org/docs/quality/fhir-covid-admissions-quality-report.pdf> .

    # Distributie: hoe de data kan worden verkregen
    <https://example.org/distribution/fhir-covid-bulk> a dcat:Distribution ;
        dct:title "Distributie – FHIR bulk export (via aanvraag)"@nl ;
        dct:description "Bulk export van FHIR resources. Toegang via formele aanvraagprocedure."@nl ;
        dcat:accessURL <https://example.org/access-request/fhir-covid-admissions> ;
        dcat:accessService <https://example.org/service/fhir-api> .

    # Dataservice: de FHIR API
    <https://example.org/service/fhir-api> a dcat:DataService ;
        dct:title "Dataservice – FHIR API Ziekenhuis X"@nl ;
        dct:description "HL7 FHIR R4 API voor gestructureerde patiëntgegevens."@nl ;
        dct:conformsTo <http://hl7.org/fhir/R4> ;
        dcat:endpointURL <https://fhir.ziekenhuisx.nl/> ;
        dcat:endpointDescription <https://fhir.ziekenhuisx.nl/metadata> ;
        dcat:servesDataset <https://example.org/dataset/fhir-covid-admissions> .
    ```

??? example "Voorbeeld 2: XNAT-omgeving met DICOM-beelden (dynamische databron)"

    Een XNAT-omgeving bevat medische beelden die regelmatig worden aangevuld. Dit voorbeeld toont hoe beeldvormende data wordt beschreven, inclusief afgeleide producten zoals segmentaties.

    **Kenmerken van dit voorbeeld:**

    - Imaging-specifieke metadata
    - Meerdere distributies voor dezelfde dataset (originele beelden en afgeleide segmentaties)
    - Endpoint description met verwijzing naar OpenAPI specificatie

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix dqv: <http://www.w3.org/ns/dqv#> .
    @prefix oa: <http://www.w3.org/ns/oa#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/xnat> a dcat:Catalog ;
        dct:title "Catalogus – Beeldvormende data (XNAT)"@nl ;
        dct:description "Catalogus met DICOM-collecties uit de XNAT-omgeving van het radiologie-onderzoekscentrum."@nl ;
        dcat:dataset <https://example.org/dataset/dicom-neuro-mri> .

    <https://example.org/dataset/dicom-neuro-mri> a dcat:Dataset ;
        dct:title "Dataset – Neurologie MRI collectie"@nl ;
        dct:description "Dynamische collectie van neurologische MRI-scans voor onderzoek naar neurodegeneratieve aandoeningen. Bevat T1, T2 en FLAIR sequenties."@nl ;

        # Wekelijkse toevoegingen van nieuwe scans
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/WEEKLY> ;

        # Niet-publieke toegang
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        # Imaging-specifieke gezondheidscategorie
        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;
        healthdcatap:healthTheme <https://healthdcat-ap.eu/vocab/health-theme/NONCOMMUNICABLE_DISEASES> ;

        # Populatiekenmerken
        healthdcatap:numberOfUniqueIndividuals "1200"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "4800"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Patiënten met neurologische indicatie; selectie op basis van studie/protocol."@nl ;

        # Conformiteit aan DICOM standaard
        dct:conformsTo <https://www.wikidata.org/wiki/Q81095> ;

        # Bewaartermijn
        healthdcatap:retentionPeriod [
            a dct:PeriodOfTime ;
            dcat:startDate "2024-01-01"^^xsd:date ;
            dcat:endDate "2029-01-01"^^xsd:date
        ] ;

        # Kwaliteitscertificaat
        dqv:hasQualityAnnotation <https://example.org/qualitycertificate/xnat-neuro-mri-qc> ;

        # Twee distributies: originele beelden en afgeleide producten
        dcat:distribution
            <https://example.org/distribution/xnat-dicom-bulk>,
            <https://example.org/distribution/xnat-derived-segmentation> .

    <https://example.org/qualitycertificate/xnat-neuro-mri-qc> a dqv:QualityCertificate ;
        dct:title "Kwaliteitscertificaat – Neurologie MRI"@nl ;
        oa:hasTarget <https://example.org/dataset/dicom-neuro-mri> ;
        oa:hasBody <https://example.org/docs/quality/xnat-neuro-mri-qc.pdf> .

    # Distributie voor originele DICOM-beelden
    <https://example.org/distribution/xnat-dicom-bulk> a dcat:Distribution ;
        dct:title "Distributie – DICOM bulk set"@nl ;
        dct:description "Originele DICOM-bestanden met volledige metadata headers."@nl ;
        dcat:accessURL <https://example.org/access-request/dicom-neuro-mri> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/dicom> ;
        dcat:accessService <https://example.org/service/xnat> .

    # Distributie voor afgeleide segmentaties
    <https://example.org/distribution/xnat-derived-segmentation> a dcat:Distribution ;
        dct:title "Distributie – Afgeleide segmentaties"@nl ;
        dct:description "Automatisch gegenereerde hersenstructuur segmentaties (FreeSurfer)."@nl ;
        dcat:accessURL <https://example.org/access-request/dicom-neuro-mri/derived> ;
        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dcat:accessService <https://example.org/service/xnat> .

    # De XNAT dataservice met OpenAPI documentatie
    <https://example.org/service/xnat> a dcat:DataService ;
        dct:title "Dataservice – XNAT REST API"@nl ;
        dct:description "XNAT REST API voor programmatische toegang tot de beeldcollectie."@nl ;
        dcat:endpointURL <https://xnat.ziekenhuisx.nl/> ;
        dcat:endpointDescription <https://xnat.ziekenhuisx.nl/xapi/openapi.json> ;
        dct:conformsTo <https://spec.openapis.org/oas/v3.0.0> ;
        dcat:servesDataset <https://example.org/dataset/dicom-neuro-mri> .
    ```

??? example "Voorbeeld 3: OMOP-CDM database (dynamische databron)"

    Een OMOP-CDM database vormt een gestandaardiseerde representatie van klinische data. Dit voorbeeld toont hoe een diabetes-cohort binnen een OMOP-database wordt beschreven.

    **Kenmerken van dit voorbeeld:**

    - Schema-versioning (OMOP CDM versie)
    - Meerdere distributies met verschillende toegangsvormen
    - Verwijzing naar specifieke OMOP concept codes

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/omop> a dcat:Catalog ;
        dct:title "Catalogus – OMOP-CDM Ziekenhuis X"@nl ;
        dct:description "Catalogus met OMOP-CDM gebaseerde datasets voor observationeel onderzoek."@nl ;
        dcat:dataset <https://example.org/dataset/omop-diabetes> .

    <https://example.org/dataset/omop-diabetes> a dcat:Dataset ;
        dct:title "Dataset – Type 2 diabetes cohort (OMOP-CDM)"@nl ;
        dct:description "Dynamische dataset met gegevens van patiënten met type 2 diabetes in OMOP-CDM formaat. Inclusief medicatie, lab-uitslagen, consulten en comorbiditeiten."@nl ;

        # Dagelijkse ETL-updates
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/DAILY> ;

        # Schema-versie: wijzigt alleen bij CDM upgrade
        dcat:version "OMOP CDM v5.4"^^xsd:string ;

        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;

        # Populatiekenmerken
        healthdcatap:numberOfUniqueIndividuals "25000"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "375000"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Volwassenen met type 2 diabetes; inclusie op basis van OMOP concept sets voor diabetes diagnose en/of medicatie."@nl ;
        healthdcatap:minTypicalAge "40"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "70"^^xsd:nonNegativeInteger ;

        # Coderingssystemen in de OMOP-CDM
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q1753883>,  # SNOMED CT
            <https://www.wikidata.org/wiki/Q45127>,    # ICD-10
            <https://www.wikidata.org/wiki/Q502480> ;  # LOINC

        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:Consent, dpv:PublicInterest ;
        dpv:hasPersonalData dpv:HealthData ;

        # Verwijzing naar specifieke codes in de coderingssystemen
        healthdcatap:hasCodeValues
            <https://icd.who.int/browse10/2019/en#/E11>, # Type 2 diabetes mellitus (ICD-10)
            <https://loinc.org/LA10552-0>,               # Diabetes Type 2 (LOINC)
            <http://purl.bioontology.org/ontology/SNOMEDCT/372567009> ; # Metformin (SNOMED CT)

        # Temporele dekking: actief groeiende database
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2018-01-01"^^xsd:date
        ] ;

        dcat:distribution
            <https://example.org/distribution/omop-diabetes-sqlview>,
            <https://example.org/distribution/omop-diabetes-export> .

    # SQL view voor federatieve toegang
    <https://example.org/distribution/omop-diabetes-sqlview> a dcat:Distribution ;
        dct:title "Distributie – SQL view (federatief)"@nl ;
        dct:description "Beveiligde SQL view voor federatieve queries binnen een geautoriseerde omgeving."@nl ;
        dcat:accessURL <https://example.org/access-request/omop-diabetes/sql> ;
        dcat:accessService <https://example.org/service/omop-sql> .

    # Export voor centrale analyse
    <https://example.org/distribution/omop-diabetes-export> a dcat:Distribution ;
        dct:title "Distributie – Data export (centraal)"@nl ;
        dct:description "Gepseudonimiseerde export voor verwerking in een centrale BVO."@nl ;
        dcat:accessURL <https://example.org/access-request/omop-diabetes/export> ;
        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dcat:accessService <https://example.org/service/omop-sql> .

    <https://example.org/service/omop-sql> a dcat:DataService ;
        dct:title "Dataservice – OMOP Query Service"@nl ;
        dct:description "SQL-interface voor gestandaardiseerde queries op de OMOP-CDM database."@nl ;
        dcat:endpointURL <https://data.ziekenhuisx.nl/omop/query> ;
        dcat:servesDataset <https://example.org/dataset/omop-diabetes> .
    ```

??? example "Voorbeeld 4: Onderzoekscohort als DatasetSeries (statische databron)"

    Voor onderzoekscohorten die periodiek worden gepubliceerd is `dcat:DatasetSeries` bijzonder geschikt. Dit voorbeeld toont een jaarlijks gepubliceerd hartfalen-cohort met meerdere versies.

    **Kenmerken van dit voorbeeld:**

    - Gemeenschappelijke metadata op serie-niveau
    - Individuele versies met specifieke populatiestatistieken
    - Relaties tussen versies via `dcat:prev`, `dcat:first`, `dcat:last`

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/research> a dcat:Catalog ;
        dct:title "Catalogus – Onderzoekscohorten"@nl ;
        dct:description "Catalogus met voorgedefinieerde onderzoekscohorten voor secundair gebruik."@nl ;
        dcat:dataset <https://example.org/dataset-series/heart-failure-cohort> .

    # De DatasetSeries: gemeenschappelijke metadata voor alle versies
    <https://example.org/dataset-series/heart-failure-cohort> a dcat:DatasetSeries ;
        dct:title "Cohort serie – Hartfalen patiënten"@nl ;
        dct:description "Jaarlijks gepubliceerd cohort van patiënten met hartfalen, geëxtraheerd uit het EPD-systeem. Elke versie bevat een snapshot van patiënten die aan de inclusiecriteria voldoen tot en met het voorgaande jaar."@nl ;

        # Periodieke publicatie
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/ANNUAL> ;

        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;
        healthdcatap:healthTheme <https://healthdcat-ap.eu/vocab/health-theme/NONCOMMUNICABLE_DISEASES> ;

        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q1753883>, # SNOMED CT
            <https://www.wikidata.org/wiki/Q45127> ;  # ICD-10

        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dpv:hasPersonalData dpv:HealthData ;

        # Navigatie door de serie
        dcat:first <https://example.org/dataset/heart-failure-cohort-2023> ;
        dcat:last <https://example.org/dataset/heart-failure-cohort-2025> ;

        dcat:seriesMember
            <https://example.org/dataset/heart-failure-cohort-2023>,
            <https://example.org/dataset/heart-failure-cohort-2024>,
            <https://example.org/dataset/heart-failure-cohort-2025> .

    # Versie 2023: eerste publicatie
    <https://example.org/dataset/heart-failure-cohort-2023> a dcat:Dataset ;
        dct:title "Cohort – Hartfalen 2023"@nl ;
        dct:description "Eerste versie van het hartfalen cohort, bevat patiënten t/m 2022."@nl ;
        dcat:version "2023.1"^^xsd:string ;
        dct:issued "2023-03-15"^^xsd:date ;

        dcat:inSeries <https://example.org/dataset-series/heart-failure-cohort> ;

        healthdcatap:numberOfUniqueIndividuals "5200"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "78000"^^xsd:nonNegativeInteger ;

        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2018-01-01"^^xsd:date ;
            dcat:endDate "2022-12-31"^^xsd:date
        ] ;

        dcat:distribution <https://example.org/distribution/heart-failure-2023-parquet> .

    # Versie 2024: uitgebreid cohort
    <https://example.org/dataset/heart-failure-cohort-2024> a dcat:Dataset ;
        dct:title "Cohort – Hartfalen 2024"@nl ;
        dct:description "Tweede versie van het hartfalen cohort, uitgebreid met patiënten uit 2023."@nl ;
        dcat:version "2024.1"^^xsd:string ;
        dct:issued "2024-03-15"^^xsd:date ;

        dcat:inSeries <https://example.org/dataset-series/heart-failure-cohort> ;
        dcat:prev <https://example.org/dataset/heart-failure-cohort-2023> ;

        healthdcatap:numberOfUniqueIndividuals "6100"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "91500"^^xsd:nonNegativeInteger ;

        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2018-01-01"^^xsd:date ;
            dcat:endDate "2023-12-31"^^xsd:date
        ] ;

        dcat:distribution <https://example.org/distribution/heart-failure-2024-parquet> .

    # Versie 2025: meest recente versie
    <https://example.org/dataset/heart-failure-cohort-2025> a dcat:Dataset ;
        dct:title "Cohort – Hartfalen 2025"@nl ;
        dct:description "Derde versie van het hartfalen cohort, uitgebreid met patiënten uit 2024."@nl ;
        dcat:version "2025.1"^^xsd:string ;
        dct:issued "2025-03-15"^^xsd:date ;

        dcat:inSeries <https://example.org/dataset-series/heart-failure-cohort> ;
        dcat:prev <https://example.org/dataset/heart-failure-cohort-2024> ;

        healthdcatap:numberOfUniqueIndividuals "7300"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "109500"^^xsd:nonNegativeInteger ;

        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2018-01-01"^^xsd:date ;
            dcat:endDate "2024-12-31"^^xsd:date
        ] ;

        dcat:distribution <https://example.org/distribution/heart-failure-2025-parquet> .

    # Distributies in Parquet formaat
    <https://example.org/distribution/heart-failure-2023-parquet> a dcat:Distribution ;
        dct:title "Distributie – Hartfalen 2023 (Parquet)"@nl ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2023> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .

    <https://example.org/distribution/heart-failure-2024-parquet> a dcat:Distribution ;
        dct:title "Distributie – Hartfalen 2024 (Parquet)"@nl ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2024> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .

    <https://example.org/distribution/heart-failure-2025-parquet> a dcat:Distribution ;
        dct:title "Distributie – Hartfalen 2025 (Parquet)"@nl ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2025> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .
    ```

??? example "Voorbeeld 5: Validatieset voor federated learning (statische databron zonder serie)"

    Een gestandaardiseerde validatieset die door meerdere datastations wordt gebruikt om federated learning modellen te testen is een praktisch voorbeeld van een statische databron zonder DatasetSeries.

    **Kenmerken van dit voorbeeld:**

    - Centrale validatieset gedistribueerd naar meerdere datastations
    - Dataset moet stabiel blijven voor vergelijkbare evaluatieresultaten
    - Eenmalig samengesteld voor een specifiek federated learning project
    - Gebruikt voor lokale validatie tijdens iteratief modeltraining

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/federated-learning> a dcat:Catalog ;
        dct:title "Catalogus – Federated learning project"@nl ;
        dct:description "Datasets voor een federated learning project over sepsis voorspelling."@nl ;
        dcat:dataset <https://example.org/dataset/sepsis-validation-set> .

    # Vaste validatieset voor federated learning: geen serie
    <https://example.org/dataset/sepsis-validation-set> a dcat:Dataset ;
        dct:title "Dataset – Sepsis voorspelling validatieset"@nl ;
        dct:description "Gestandaardiseerde validatieset voor een federated learning project over sepsis voorspelling. Deze dataset wordt door alle deelnemende ziekenhuizen gebruikt om lokaal getrainde modellen te evalueren op dezelfde testcases. Bevat 500 ICU-opnames met laboratoriumwaarden, vitale parameters en sepsis-uitkomsten. De dataset is representatief samengesteld uit data van alle deelnemers en blijft ongewijzigd gedurende het project voor vergelijkbaarheid van resultaten."@nl ;

        # Vaste versie voor het project
        dcat:version "1.0"^^xsd:string ;
        dct:issued "2024-09-01"^^xsd:date ;

        # Statische dataset: geen updates tijdens projectduur
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/NEVER> ;

        # Gepseudonimiseerd, alleen beschikbaar voor projectpartners
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;
        healthdcatap:healthTheme <https://healthdcat-ap.eu/vocab/health-theme/BLOOD_INFECTIONS> ;

        # Vaste samenstelling voor reproduceerbare evaluatie
        healthdcatap:numberOfUniqueIndividuals "500"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "12000"^^xsd:nonNegativeInteger ; # 24 uur × 500 patiënten
        healthdcatap:populationCoverage "Volwassen IC-patiënten met verdenking op sepsis. Balans tussen positieve en negatieve cases (50/50). Data afkomstig uit 8 deelnemende ziekenhuizen voor representativiteit."@nl ;
        healthdcatap:minTypicalAge "18"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "90"^^xsd:nonNegativeInteger ;

        # Historische periode waaruit data is geselecteerd
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2022-01-01"^^xsd:date ;
            dcat:endDate "2023-12-31"^^xsd:date
        ] ;

        # Geharmoniseerde coderingen voor cross-site gebruik
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q502480> ; # LOINC

        # Conform OMOP-CDM voor interoperabiliteit
        dct:conformsTo <https://ohdsi.github.io/CommonDataModel/cdm54.html> ;

        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dpv:hasPersonalData dpv:PseudonymizedData ;

        dcat:distribution <https://example.org/distribution/sepsis-validation-parquet> .

    # Distributie: eenmalige download voor deelnemers
    <https://example.org/distribution/sepsis-validation-parquet> a dcat:Distribution ;
        dct:title "Distributie – Validatieset (Parquet)"@nl ;
        dct:description "Validatieset in OMOP-CDM formaat (Parquet). Beschikbaar voor alle datastations in het consortium."@nl ;
        dcat:accessURL <https://example.org/access-request/sepsis-validation> ;
        dcat:downloadURL <https://example.org/downloads/sepsis-fl-project/validation-set-v1.0.parquet> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> ;
        dcat:byteSize "8388608"^^xsd:nonNegativeInteger .
    ```

## 3.3.6. Relatie met het vijflagenmodel

De metadata-standaarden die in dit document worden beschreven, sluiten aan bij het vijflagenmodel voor data stations:

- **Laag 3 (het datastation)**: De `dcat:Catalog` en `dcat:Dataset` beschrijvingen vormen de basis voor de catalogusfunctie van het datastation. Het datastation moet haar catalogus publiceren in HealthDCAT-AP formaat.
- **Laag 4 (orchestratie)**: De `dcat:DataService` beschrijvingen maken het mogelijk voor federatieve query-engines en catalogus browsers om automatisch de mogelijkheden van een datastation te ontdekken.
- **Laag 5 (gebruik)**: De metadata over toegangsrechten, doelbinding en kwaliteit ondersteunt onderzoekers bij het selecteren van geschikte datasets voor hun onderzoeksvraag.
