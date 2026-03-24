# 3.3. Metadata interoperability

## 3.3.1. Why metadata is essential for data stations

Metadata plays a crucial role in a data station. Without good metadata about the data, researchers and systems do not know what data is available, what its quality is, and under what conditions it may be used. Metadata makes it possible to:

- **Find datasets**: A researcher can search a catalogue for datasets on heart failure in a specific age group.
- **Understand datasets**: The description explains which variables are present, how the data was collected, and what limitations apply.
- **Process datasets automatically**: Systems can assess on the basis of standardised metadata whether a dataset is suitable for a particular analysis.

To achieve interoperability between data stations, it is of great importance that metadata is described in a standardised way. International standards and profiles have been developed for this purpose.

=== "**DCAT**"

    **DCAT** (Data Catalog Vocabulary) is a W3C standard originally designed for describing datasets in data catalogues. It provides a common vocabulary with which organisations can describe their datasets, regardless of the domain. DCAT version 3 (2024) introduces, among other things, the `DatasetSeries` class for describing related datasets.

=== "**DCAT-AP**"

    **DCAT-AP** is a European application profile of DCAT, developed by the European Commission. It refines DCAT with additional mandatory and recommended fields relevant to European government data, such as access rights and applicable legislation. DCAT-AP forms the basis for many national data catalogues.

=== "**HealthDCAT-AP**"

    **HealthDCAT-AP** is an extension of DCAT-AP specifically for the healthcare sector. It adds metadata elements that are essential for health data, such as:

    - Health categories (EHR, images, genomic data)
    - Population characteristics (age range, number of unique individuals)
    - Coding systems (SNOMED CT, ICD-10, LOINC)
    - Retention periods and storage deadlines
    - The responsible Health Data Access Body (HDAB)

=== "**Health-RI metadata schema**"

    The **Health-RI metadata schema** is a Dutch profile based on DCAT-AP and HealthDCAT-AP, with specific adaptations for the Health-RI Data Catalogue. This schema defines which metadata elements are mandatory, recommended or optional for Dutch health data.

## 3.3.2. DCAT classes in a data station

In DCAT, various classes are used to describe the structure of a data catalogue. For data stations, the following classes are most relevant.

**The catalogue: `dcat:Catalog`**

A `dcat:Catalog` represents the data station itself as a collection of datasets and data services. The catalogue acts as the entry point for users and systems wishing to know what data is available. The catalogue not only describes which datasets exist, but also via which services they are accessible. The following properties are essential for a catalogue:

| Property          | Description                              | Example                                              |
| ----------------- | ---------------------------------------- | ---------------------------------------------------- |
| `dct:title`       | Name of the catalogue                    | "Data Catalogue Hospital X"                          |
| `dct:description` | Description of the content               | "Catalogue with clinical datasets for research"      |
| `dct:publisher`   | Organisation publishing the catalogue    | Hospital X                                           |
| `dcat:dataset`    | References to datasets                   | Links to available datasets                          |
| `dcat:service`    | References to data services              | Links to API endpoints                               |

In practice, one organisation may have multiple catalogues. For example, a hospital may have a catalogue for imaging data (MRI, CT, PET) and a separate catalogue for clinical data from the EHR.

**The dataset: `dcat:Dataset`**

A `dcat:Dataset` represents a logical collection of data described and made available as a unit. The granularity of a dataset is not technically prescribed, but is determined by the organisation of the data holder and the way in which researchers want to be able to find and request the data. Datasets can, for example, be organised:

- **By disease**: "COVID-19 admission data 2020-2024"
- **By domain**: "Cardiology patient data"
- **By research project**: "IMPROVE study diabetes cohort"

For datasets in healthcare, the following metadata elements are particularly relevant:

| Category         | HealthDCAT-AP elements                                                                                 | Purpose                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Population**   | `numberOfUniqueIndividuals`, `numberOfRecords`, `populationCoverage`, `minTypicalAge`, `maxTypicalAge` | Insight into size and composition                               |
| **Terminology**  | `hasCodingSystem`                                                                                      | Which coding systems are used (SNOMED, ICD-10, LOINC)           |
| **Legal**        | `accessRights`, `applicableLegislation`                                                                | Access conditions and legislation (EHDS, GDPR)                  |
| **Quality**      | `hasQualityAnnotation`                                                                                 | Reference to quality reporting                                  |
| **Privacy**      | `retentionPeriod`, `hdab`                                                                              | Retention period and responsible authority                      |

**The dataset series: `dcat:DatasetSeries`**

The `dcat:DatasetSeries` class is intended for describing collections of related datasets that are published separately but are logically connected. This is particularly suitable for:

- **Periodic cohorts**: Annually published extractions from the same patient population
- **Versions of research datasets**: Successive versions of a cohort after corrections or extensions
- **Longitudinal data**: Measurement moments in a follow-up study

The series defines common metadata for the data (such as access rights and coding systems), while individual datasets retain their specific characteristics (such as the number of records and the temporal coverage).

**The distribution: `dcat:Distribution`**

A `dcat:Distribution` describes a concrete realisation of a dataset: how the data can actually be obtained or accessed. One dataset can have multiple distributions:

| Distribution type       | Description                                 | Typical use                              |
| ----------------------- | ------------------------------------------- | ---------------------------------------- |
| **Bulk export**         | One-time download of the complete dataset   | Research in a central SPE                |
| **API access**          | Programmatic access via a service           | Federated analysis                       |
| **Synthetic sample**    | Representative test data                    | Development and validation of algorithms |
| **View/subset**         | Predefined selection                        | Specific research purpose                |

The distribution specifies technical details such as the file format (`dcat:mediaType`), the access URL (`dcat:accessURL`), and optionally a reference to the underlying data service.

**The data service: `dcat:DataService`**

A `dcat:DataService` describes an operational service that provides access to datasets. Where a distribution represents a static snapshot or downloadable file, a data service provides dynamic access to the underlying data. The service can execute real-time queries, retrieve current data, or even perform computations without the data leaving the data station. Different types of data services are possible, for example:

| Data service type       | Example                          | Description                                 |
| ----------------------- | -------------------------------- | ------------------------------------------- |
| **FHIR API**            | `https://fhir.example.org/`      | REST API in accordance with HL7 FHIR standard |
| **OMOP query service**  | SQL interface for OMOP-CDM       | Standardised queries on OMOP database       |
| **DICOM WADO-RS**       | Web access for medical images    | Retrieval of images via web protocol        |
| **Federated endpoint**  | KIK-V or PLUGIN node             | Receipt and execution of algorithms         |

For automatic processing by systems, it is essential that the data service makes clear _how_ it can be accessed. This is done via:

- `dcat:endpointURL`: The base address of the service
- `dcat:endpointDescription`: Link to the technical documentation (e.g. OpenAPI specification or FHIR CapabilityStatement)
- `dct:conformsTo`: The standard to which the service conforms

## 3.3.3. Static versus dynamic data sources

An important distinction when modelling data sources is the difference between _static_ and _dynamic_ data sources. This distinction has direct consequences for how metadata is managed and how version control is applied.

**Static data sources: cohorts and extractions**

Static data sources are datasets that were defined and extracted at a specific point in time. The data does not change after extraction, which ensures reproducibility of research results. This type of data source is common in research projects where a fixed population and observation period are defined. Typical examples of static data sources are:

- **Research cohorts**: A predefined group of patients for a specific study
- **Periodic snapshots**: Annual or quarterly extractions from a source system
- **Anonymised datasets**: One-time generated datasets for open research

For static data sources, explicit version control is essential:

| Property        | Use                           | Example                                   |
| --------------- | ----------------------------- | ----------------------------------------- |
| `dcat:version`  | Version number of the dataset | "2024.1"                                  |
| `dct:issued`    | Publication date              | "2024-03-15"                              |
| `dct:modified`  | Date of last modification     | "2024-03-20"                              |
| `dcat:inSeries` | Link to a series              | Link to the overarching DatasetSeries     |
| `dcat:prev`     | Reference to previous version | Link to previous dataset                  |

The DatasetSeries class is particularly useful for static data sources when:

1. New versions of the same type of data are published periodically
2. Researchers need to be able to select specific versions
3. There is common metadata that can be defined at series level

**Dynamic data sources: active databases**

Dynamic data sources are databases that are continuously updated, such as EHR systems, OMOP-CDM databases or XNAT environments. It is not meaningful here to create a new version with every data change.

For dynamic data sources, we recommend the following approach:

| Aspect                     | Recommendation                                                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **The database as a whole** | Describe as `dcat:Dataset` with `dcat:accrualPeriodicity` to indicate the update frequency                                |
| **Version control**        | Use `dcat:version` only for _structural_ changes (e.g. upgrade from OMOP CDM v5.3 to v5.4)                                |
| **Temporal coverage**      | Use `dct:temporal` with only a start date (no end date) to indicate that the data is actively growing                     |
| **Statistics**             | Periodically update population statistics (`numberOfRecords`, `numberOfUniqueIndividuals`) with the corresponding `dct:modified` |
| **Schema documentation**   | Describe via `dcat:Distribution` with reference to schema documentation                                                   |

??? example "Practical example: versioning strategy"

    A hospital has an OMOP-CDM database that is updated daily with new patient data. The metadata is managed as follows:

    - **Schema version**: `dcat:version` = "OMOP CDM v5.4" – changes only when the data model is upgraded
    - **Update frequency**: `dcat:accrualPeriodicity` = DAILY – indicates that data is added daily
    - **Statistics**: `numberOfRecords` and `numberOfUniqueIndividuals` are updated monthly, with `dct:modified` on the update date
    - **Temporal coverage**: `dct:temporal` with start date 2018-01-01 and no end date

    The Research Data Alliance has published [data versioning use cases](https://doi.org/10.15497/RDA00041) and [versioning recommendations](https://doi.org/10.5281/zenodo.13743875) that can be taken into account in the final choice and implementation of the versioning strategy.

## 3.3.4. Metadata for primary versus secondary use

When describing metadata, it is important to distinguish between primary and secondary use of data. This distinction influences which metadata elements receive emphasis.

**Primary use: focus on the service**

For primary use (direct care delivery), source systems remain leading. In DCAT, the focus is primarily on describing _what_ is available and _how_ it can be consulted. Since a dataset is not created for every individual patient, the emphasis is on describing the source system and the associated data service.

The `dcat:DataService` plays a central role here. It is important that the service is well described, so that a requesting system (for example another EHR or a care application) can correctly request and use the data.

**Secondary use: focus on content and context**

For secondary use (research, policy, innovation), the emphasis shifts to the _content_ and _quality_ of the data, as well as the context in which the data was collected. HealthDCAT-AP enables explicit modelling of these aspects:

| Aspect                    | HealthDCAT-AP elements                                               |
| ------------------------- | -------------------------------------------------------------------- |
| **Access rights**         | `NON_PUBLIC`, `RESTRICTED`, `PUBLIC`                                 |
| **Legislation**           | References to EHDS, GDPR, national laws                              |
| **Purpose binding**       | `dpv:hasPurpose` (e.g. academic research, public health)             |
| **Legal basis**           | `dpv:hasLegalBasis` (e.g. public interest, consent)                  |
| **Quality**               | Reference to quality reports via `dqv:hasQualityAnnotation`          |
| **HDAB**                  | `healthdcatap:hdab` – the responsible Health Data Access Body        |

**Endpoint descriptions for automatic processing**

When a catalogue browser or federated query engine wants to automatically determine the capabilities of a data service, it must be known what type of specification the `dcat:endpointDescription` contains. A FHIR CapabilityStatement has, for example, a different structure from an OpenAPI specification, and systems need to know how to interpret these. By making the type of specification explicit with `dct:conformsTo`, a system can make the right choice and discover the available capabilities.

???+ success "Combining endpointDescription with conformsTo"

    Always combine `dcat:endpointDescription` with `dct:conformsTo` to make the type of specification explicit:

    ```turtle
    <https://example.org/service/fhir-api> a dcat:DataService ;
        dcat:endpointURL <https://fhir.example.org/> ;
        dcat:endpointDescription <https://fhir.example.org/metadata> ;
        # Explicitly indicate that this is a FHIR CapabilityStatement
        dct:conformsTo <http://hl7.org/fhir/StructureDefinition/CapabilityStatement> .

    <https://example.org/service/rest-api> a dcat:DataService ;
        dcat:endpointURL <https://api.example.org/> ;
        dcat:endpointDescription <https://api.example.org/openapi.json> ;
        # Explicitly indicate that this is an OpenAPI specification
        dct:conformsTo <https://spec.openapis.org/oas/v3.1.0> .
    ```

## 3.3.5. Examples of metadata for a data station

The following examples illustrate how different types of data sources in a data station can be described with DCAT and HealthDCAT-AP. Each example demonstrates specific aspects of the standard.

??? example "Example 1: FHIR system (dynamic data source)"

    A FHIR system in a hospital can be exposed in various ways. In this example, a COVID-19 dataset is described that grows dynamically as new admissions are registered.

    **Characteristics of this example:**

    - Dynamic dataset with daily updates
    - Secondary use with restricted access
    - Complete HealthDCAT-AP metadata including population characteristics and coding systems
    - Quality reporting linked via DQV

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix dqv: <http://www.w3.org/ns/dqv#> .
    @prefix oa: <http://www.w3.org/ns/oa#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    # The catalogue: represents the data station
    <https://example.org/catalog/fhir> a dcat:Catalog ;
        dct:title "Catalogue – FHIR (example)"@en ;
        dct:description "Catalogue with FHIR-based datasets from Hospital X."@en ;
        dcat:dataset <https://example.org/dataset/fhir-covid-admissions> ;
        dcat:service <https://example.org/service/fhir-api> .

    # The dataset: COVID-19 admission data
    <https://example.org/dataset/fhir-covid-admissions> a dcat:Dataset ;
        dct:title "Dataset – COVID-19 admissions (FHIR, secondary use)"@en ;
        dct:description "Dynamic dataset with COVID-19 admission data from the EHR system of Hospital X. Contains demographic data, admission information, diagnoses and treatments."@en ;

        # Dynamic dataset: update frequency instead of version per change
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/DAILY> ;

        # Access rights and applicable legislation
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,  # EHDS Regulation
            <http://data.europa.eu/eli/reg/2016/679/oj> ; # GDPR

        # Health category and responsible HDAB
        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;

        # Population characteristics (periodically updated)
        healthdcatap:numberOfUniqueIndividuals "85000"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "430000"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Admissions of adult patients with confirmed COVID-19 diagnosis at Hospital X."@en ;
        healthdcatap:minTypicalAge "18"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "95"^^xsd:nonNegativeInteger ;

        # Temporal coverage: growing dataset without end date
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2020-03-01"^^xsd:date
        ] ;

        # Coding systems used for semantic interoperability
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q45127>,   # ICD-10
            <https://www.wikidata.org/wiki/Q1753883>, # SNOMED CT
            <https://www.wikidata.org/wiki/Q502480> ; # LOINC

        # Purpose binding and legal basis (Data Privacy Vocabulary)
        dpv:hasPurpose dpv:AcademicResearch, dpv:PublicHealth ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dpv:hasPersonalData dpv:HealthData ;

        # Retention period
        healthdcatap:retentionPeriod [
            a dct:PeriodOfTime ;
            dcat:startDate "2020-03-01"^^xsd:date ;
            dcat:endDate "2030-03-01"^^xsd:date
        ] ;

        # Quality reporting
        dqv:hasQualityAnnotation <https://example.org/qualitycertificate/fhir-covid-dq-report> ;

        dcat:distribution <https://example.org/distribution/fhir-covid-bulk> .

    # Quality report
    <https://example.org/qualitycertificate/fhir-covid-dq-report> a dqv:QualityCertificate ;
        dct:title "Quality report – COVID-19 admissions (FHIR)"@en ;
        oa:hasTarget <https://example.org/dataset/fhir-covid-admissions> ;
        oa:hasBody <https://example.org/docs/quality/fhir-covid-admissions-quality-report.pdf> .

    # Distribution: how the data can be obtained
    <https://example.org/distribution/fhir-covid-bulk> a dcat:Distribution ;
        dct:title "Distribution – FHIR bulk export (via request)"@en ;
        dct:description "Bulk export of FHIR resources. Access via formal request procedure."@en ;
        dcat:accessURL <https://example.org/access-request/fhir-covid-admissions> ;
        dcat:accessService <https://example.org/service/fhir-api> .

    # Data service: the FHIR API
    <https://example.org/service/fhir-api> a dcat:DataService ;
        dct:title "Data service – FHIR API Hospital X"@en ;
        dct:description "HL7 FHIR R4 API for structured patient data."@en ;
        dct:conformsTo <http://hl7.org/fhir/R4> ;
        dcat:endpointURL <https://fhir.hospitalx.nl/> ;
        dcat:endpointDescription <https://fhir.hospitalx.nl/metadata> ;
        dcat:servesDataset <https://example.org/dataset/fhir-covid-admissions> .
    ```

??? example "Example 2: XNAT environment with DICOM images (dynamic data source)"

    An XNAT environment contains medical images that are regularly supplemented. This example shows how imaging data is described, including derived products such as segmentations.

    **Characteristics of this example:**

    - Imaging-specific metadata
    - Multiple distributions for the same dataset (original images and derived segmentations)
    - Endpoint description with reference to OpenAPI specification

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
        dct:title "Catalogue – Imaging data (XNAT)"@en ;
        dct:description "Catalogue with DICOM collections from the XNAT environment of the radiology research centre."@en ;
        dcat:dataset <https://example.org/dataset/dicom-neuro-mri> .

    <https://example.org/dataset/dicom-neuro-mri> a dcat:Dataset ;
        dct:title "Dataset – Neurology MRI collection"@en ;
        dct:description "Dynamic collection of neurological MRI scans for research into neurodegenerative conditions. Contains T1, T2 and FLAIR sequences."@en ;

        # Weekly additions of new scans
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/WEEKLY> ;

        # Non-public access
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        # Imaging-specific health category
        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;
        healthdcatap:healthTheme <https://healthdcat-ap.eu/vocab/health-theme/NONCOMMUNICABLE_DISEASES> ;

        # Population characteristics
        healthdcatap:numberOfUniqueIndividuals "1200"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "4800"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Patients with neurological indication; selection based on study/protocol."@en ;

        # Conformity to DICOM standard
        dct:conformsTo <https://www.wikidata.org/wiki/Q81095> ;

        # Retention period
        healthdcatap:retentionPeriod [
            a dct:PeriodOfTime ;
            dcat:startDate "2024-01-01"^^xsd:date ;
            dcat:endDate "2029-01-01"^^xsd:date
        ] ;

        # Quality certificate
        dqv:hasQualityAnnotation <https://example.org/qualitycertificate/xnat-neuro-mri-qc> ;

        # Two distributions: original images and derived products
        dcat:distribution
            <https://example.org/distribution/xnat-dicom-bulk>,
            <https://example.org/distribution/xnat-derived-segmentation> .

    <https://example.org/qualitycertificate/xnat-neuro-mri-qc> a dqv:QualityCertificate ;
        dct:title "Quality certificate – Neurology MRI"@en ;
        oa:hasTarget <https://example.org/dataset/dicom-neuro-mri> ;
        oa:hasBody <https://example.org/docs/quality/xnat-neuro-mri-qc.pdf> .

    # Distribution for original DICOM images
    <https://example.org/distribution/xnat-dicom-bulk> a dcat:Distribution ;
        dct:title "Distribution – DICOM bulk set"@en ;
        dct:description "Original DICOM files with complete metadata headers."@en ;
        dcat:accessURL <https://example.org/access-request/dicom-neuro-mri> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/dicom> ;
        dcat:accessService <https://example.org/service/xnat> .

    # Distribution for derived segmentations
    <https://example.org/distribution/xnat-derived-segmentation> a dcat:Distribution ;
        dct:title "Distribution – Derived segmentations"@en ;
        dct:description "Automatically generated brain structure segmentations (FreeSurfer)."@en ;
        dcat:accessURL <https://example.org/access-request/dicom-neuro-mri/derived> ;
        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dcat:accessService <https://example.org/service/xnat> .

    # The XNAT data service with OpenAPI documentation
    <https://example.org/service/xnat> a dcat:DataService ;
        dct:title "Data service – XNAT REST API"@en ;
        dct:description "XNAT REST API for programmatic access to the image collection."@en ;
        dcat:endpointURL <https://xnat.hospitalx.nl/> ;
        dcat:endpointDescription <https://xnat.hospitalx.nl/xapi/openapi.json> ;
        dct:conformsTo <https://spec.openapis.org/oas/v3.0.0> ;
        dcat:servesDataset <https://example.org/dataset/dicom-neuro-mri> .
    ```

??? example "Example 3: OMOP-CDM database (dynamic data source)"

    An OMOP-CDM database forms a standardised representation of clinical data. This example shows how a diabetes cohort within an OMOP database is described.

    **Characteristics of this example:**

    - Schema versioning (OMOP CDM version)
    - Multiple distributions with different forms of access
    - Reference to specific OMOP concept codes

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/omop> a dcat:Catalog ;
        dct:title "Catalogue – OMOP-CDM Hospital X"@en ;
        dct:description "Catalogue with OMOP-CDM based datasets for observational research."@en ;
        dcat:dataset <https://example.org/dataset/omop-diabetes> .

    <https://example.org/dataset/omop-diabetes> a dcat:Dataset ;
        dct:title "Dataset – Type 2 diabetes cohort (OMOP-CDM)"@en ;
        dct:description "Dynamic dataset with data from patients with type 2 diabetes in OMOP-CDM format. Includes medication, lab results, consultations and comorbidities."@en ;

        # Daily ETL updates
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/DAILY> ;

        # Schema version: changes only when CDM is upgraded
        dcat:version "OMOP CDM v5.4"^^xsd:string ;

        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;

        # Population characteristics
        healthdcatap:numberOfUniqueIndividuals "25000"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "375000"^^xsd:nonNegativeInteger ;
        healthdcatap:populationCoverage "Adults with type 2 diabetes; inclusion based on OMOP concept sets for diabetes diagnosis and/or medication."@en ;
        healthdcatap:minTypicalAge "40"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "70"^^xsd:nonNegativeInteger ;

        # Coding systems in the OMOP-CDM
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q1753883>,  # SNOMED CT
            <https://www.wikidata.org/wiki/Q45127>,    # ICD-10
            <https://www.wikidata.org/wiki/Q502480> ;  # LOINC

        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:Consent, dpv:PublicInterest ;
        dpv:hasPersonalData dpv:HealthData ;

        # Reference to specific codes in the coding systems
        healthdcatap:hasCodeValues
            <https://icd.who.int/browse10/2019/en#/E11>, # Type 2 diabetes mellitus (ICD-10)
            <https://loinc.org/LA10552-0>,               # Diabetes Type 2 (LOINC)
            <http://purl.bioontology.org/ontology/SNOMEDCT/372567009> ; # Metformin (SNOMED CT)

        # Temporal coverage: actively growing database
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2018-01-01"^^xsd:date
        ] ;

        dcat:distribution
            <https://example.org/distribution/omop-diabetes-sqlview>,
            <https://example.org/distribution/omop-diabetes-export> .

    # SQL view for federated access
    <https://example.org/distribution/omop-diabetes-sqlview> a dcat:Distribution ;
        dct:title "Distribution – SQL view (federated)"@en ;
        dct:description "Secure SQL view for federated queries within an authorised environment."@en ;
        dcat:accessURL <https://example.org/access-request/omop-diabetes/sql> ;
        dcat:accessService <https://example.org/service/omop-sql> .

    # Export for central analysis
    <https://example.org/distribution/omop-diabetes-export> a dcat:Distribution ;
        dct:title "Distribution – Data export (central)"@en ;
        dct:description "Pseudonymised export for processing in a central SPE."@en ;
        dcat:accessURL <https://example.org/access-request/omop-diabetes/export> ;
        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dcat:accessService <https://example.org/service/omop-sql> .

    <https://example.org/service/omop-sql> a dcat:DataService ;
        dct:title "Data service – OMOP Query Service"@en ;
        dct:description "SQL interface for standardised queries on the OMOP-CDM database."@en ;
        dcat:endpointURL <https://data.hospitalx.nl/omop/query> ;
        dcat:servesDataset <https://example.org/dataset/omop-diabetes> .
    ```

??? example "Example 4: Research cohort as DatasetSeries (static data source)"

    For research cohorts that are published periodically, `dcat:DatasetSeries` is particularly suitable. This example shows an annually published heart failure cohort with multiple versions.

    **Characteristics of this example:**

    - Common metadata at series level
    - Individual versions with specific population statistics
    - Relationships between versions via `dcat:prev`, `dcat:first`, `dcat:last`

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/research> a dcat:Catalog ;
        dct:title "Catalogue – Research cohorts"@en ;
        dct:description "Catalogue with predefined research cohorts for secondary use."@en ;
        dcat:dataset <https://example.org/dataset-series/heart-failure-cohort> .

    # The DatasetSeries: common metadata for all versions
    <https://example.org/dataset-series/heart-failure-cohort> a dcat:DatasetSeries ;
        dct:title "Cohort series – Heart failure patients"@en ;
        dct:description "Annually published cohort of patients with heart failure, extracted from the EHR system. Each version contains a snapshot of patients meeting the inclusion criteria up to and including the previous year."@en ;

        # Periodic publication
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

        # Navigation through the series
        dcat:first <https://example.org/dataset/heart-failure-cohort-2023> ;
        dcat:last <https://example.org/dataset/heart-failure-cohort-2025> ;

        dcat:seriesMember
            <https://example.org/dataset/heart-failure-cohort-2023>,
            <https://example.org/dataset/heart-failure-cohort-2024>,
            <https://example.org/dataset/heart-failure-cohort-2025> .

    # Version 2023: first publication
    <https://example.org/dataset/heart-failure-cohort-2023> a dcat:Dataset ;
        dct:title "Cohort – Heart failure 2023"@en ;
        dct:description "First version of the heart failure cohort, containing patients up to and including 2022."@en ;
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

    # Version 2024: extended cohort
    <https://example.org/dataset/heart-failure-cohort-2024> a dcat:Dataset ;
        dct:title "Cohort – Heart failure 2024"@en ;
        dct:description "Second version of the heart failure cohort, extended with patients from 2023."@en ;
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

    # Version 2025: most recent version
    <https://example.org/dataset/heart-failure-cohort-2025> a dcat:Dataset ;
        dct:title "Cohort – Heart failure 2025"@en ;
        dct:description "Third version of the heart failure cohort, extended with patients from 2024."@en ;
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

    # Distributions in Parquet format
    <https://example.org/distribution/heart-failure-2023-parquet> a dcat:Distribution ;
        dct:title "Distribution – Heart failure 2023 (Parquet)"@en ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2023> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .

    <https://example.org/distribution/heart-failure-2024-parquet> a dcat:Distribution ;
        dct:title "Distribution – Heart failure 2024 (Parquet)"@en ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2024> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .

    <https://example.org/distribution/heart-failure-2025-parquet> a dcat:Distribution ;
        dct:title "Distribution – Heart failure 2025 (Parquet)"@en ;
        dcat:accessURL <https://example.org/access-request/heart-failure-2025> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> .
    ```

??? example "Example 5: Validation set for federated learning (static data source without series)"

    A standardised validation set used by multiple data stations to test federated learning models is a practical example of a static data source without a DatasetSeries.

    **Characteristics of this example:**

    - Central validation set distributed to multiple data stations
    - Dataset must remain stable for comparable evaluation results
    - Compiled once for a specific federated learning project
    - Used for local validation during iterative model training

    ```turtle
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct:  <http://purl.org/dc/terms/> .
    @prefix dcatap: <http://data.europa.eu/r5r/> .
    @prefix dpv: <https://w3id.org/dpv#> .
    @prefix healthdcatap: <https://healthdcat-ap.eu/ns#> .
    @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

    <https://example.org/catalog/federated-learning> a dcat:Catalog ;
        dct:title "Catalogue – Federated learning project"@en ;
        dct:description "Datasets for a federated learning project on sepsis prediction."@en ;
        dcat:dataset <https://example.org/dataset/sepsis-validation-set> .

    # Fixed validation set for federated learning: no series
    <https://example.org/dataset/sepsis-validation-set> a dcat:Dataset ;
        dct:title "Dataset – Sepsis prediction validation set"@en ;
        dct:description "Standardised validation set for a federated learning project on sepsis prediction. This dataset is used by all participating hospitals to evaluate locally trained models on the same test cases. Contains 500 ICU admissions with laboratory values, vital parameters and sepsis outcomes. The dataset has been representatively compiled from data of all participants and remains unchanged throughout the project for comparability of results."@en ;

        # Fixed version for the project
        dcat:version "1.0"^^xsd:string ;
        dct:issued "2024-09-01"^^xsd:date ;

        # Static dataset: no updates during project duration
        dcat:accrualPeriodicity <http://publications.europa.eu/resource/authority/frequency/NEVER> ;

        # Pseudonymised, only available to project partners
        dct:accessRights <http://publications.europa.eu/resource/authority/access-right/RESTRICTED> ;
        dcatap:applicableLegislation
            <http://data.europa.eu/eli/reg/2025/327/oj>,
            <http://data.europa.eu/eli/reg/2016/679/oj> ;

        healthdcatap:healthCategory <https://healthdcat-ap.eu/vocab/health-category/EHRS> ;
        healthdcatap:hdab <https://hdab.nl/> ;
        healthdcatap:healthTheme <https://healthdcat-ap.eu/vocab/health-theme/BLOOD_INFECTIONS> ;

        # Fixed composition for reproducible evaluation
        healthdcatap:numberOfUniqueIndividuals "500"^^xsd:nonNegativeInteger ;
        healthdcatap:numberOfRecords "12000"^^xsd:nonNegativeInteger ; # 24 hours × 500 patients
        healthdcatap:populationCoverage "Adult ICU patients with suspected sepsis. Balance between positive and negative cases (50/50). Data from 8 participating hospitals for representativeness."@en ;
        healthdcatap:minTypicalAge "18"^^xsd:nonNegativeInteger ;
        healthdcatap:maxTypicalAge "90"^^xsd:nonNegativeInteger ;

        # Historical period from which data was selected
        dct:temporal [
            a dct:PeriodOfTime ;
            dcat:startDate "2022-01-01"^^xsd:date ;
            dcat:endDate "2023-12-31"^^xsd:date
        ] ;

        # Harmonised codings for cross-site use
        healthdcatap:hasCodingSystem
            <https://www.wikidata.org/wiki/Q502480> ; # LOINC

        # Conform OMOP-CDM for interoperability
        dct:conformsTo <https://ohdsi.github.io/CommonDataModel/cdm54.html> ;

        dpv:hasPurpose dpv:AcademicResearch ;
        dpv:hasLegalBasis dpv:PublicInterest ;
        dpv:hasPersonalData dpv:PseudonymizedData ;

        dcat:distribution <https://example.org/distribution/sepsis-validation-parquet> .

    # Distribution: one-time download for participants
    <https://example.org/distribution/sepsis-validation-parquet> a dcat:Distribution ;
        dct:title "Distribution – Validation set (Parquet)"@en ;
        dct:description "Validation set in OMOP-CDM format (Parquet). Available to all data stations in the consortium."@en ;
        dcat:accessURL <https://example.org/access-request/sepsis-validation> ;
        dcat:downloadURL <https://example.org/downloads/sepsis-fl-project/validation-set-v1.0.parquet> ;
        dcat:mediaType <https://www.iana.org/assignments/media-types/application/vnd.apache.parquet> ;
        dcat:byteSize "8388608"^^xsd:nonNegativeInteger .
    ```

## 3.3.6. Relationship with the five-layer model

The metadata standards described in this document align with the five-layer model for data stations:

- **Layer 3 (the data station)**: The `dcat:Catalog` and `dcat:Dataset` descriptions form the basis for the catalogue function of the data station. The data station must publish its catalogue in HealthDCAT-AP format.
- **Layer 4 (orchestration)**: The `dcat:DataService` descriptions enable federated query engines and catalogue browsers to automatically discover the capabilities of a data station.
- **Layer 5 (use)**: The metadata on access rights, purpose binding and quality supports researchers in selecting suitable datasets for their research question.
