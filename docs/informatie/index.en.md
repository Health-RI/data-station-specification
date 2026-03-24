#  3. Perspective: information
## Semantic and syntactic interoperability

To be able to meaningfully reuse health data, the form (syntax) and meaning (semantics) must be comparable and interchangeable. These two forms of interoperability are essential prerequisites. To understand how computers "communicate" with one another, we can compare this with how people communicate.

=== "**Syntactic interoperability (the envelope & the grammar)**"

    Syntactic interoperability is about the **form** and **structure** of the message, such as a letter. Syntactic interoperability means that the recipient can physically open the letter, recognises it as a letter, and can read the characters (for example the Latin alphabet). In the world of computing, this means that two systems can technically open each other's files and recognise the structure (e.g. "here is the name", "there is the date").
    
    !!! info "Analogy"
    
        I send you a grammatically perfect sentence: *"The blerf scrobts the grakker."* The recipient can read the sentence (syntax is correct), but has no idea what the sender means by it.

=== "**Semantic interoperability (the meaning)**"

    Semantic interoperability is about the **content** and **understanding**. Once the letter has been opened, we want to understand what it says. We need to speak the same language and use the same definitions. If I write "bank", the recipient needs to know whether I mean a piece of furniture or a financial institution.
    
    !!! info "Analogy"
    
        To understand *"The blerf scrobts the grakker"*, we need a dictionary that explains what a 'blerf' is. Semantic interoperability ensures that the computer does not merely see "180" but understands that this is a "blood pressure" in "mmHg".


## Information models for syntactic interoperability
To exchange data technically, we need standards that define the **structure**. Healthcare uses many different information models, but in recent years the sector has been converging on openEHR, OMOP and FHIR as the leading information models.[@tsafnat2024converge] Although they also contain meaning (semantics), their main function is to serve as the "container" for the data.



=== "FHIR"

    Fast Healthcare Interoperability Resources (FHIR) focuses primarily on exchanging data, for example between a hospital and an app on your phone. It uses information building blocks for this purpose: there is a card for 'Patient', a card for 'Medication', etc. It is very flexible and modern, comparable to how web pages work. The syntax of FHIR prescribes what digital messages should look like. FHIR is popular because it uses the same technical standards as the Internet, making it easy for application developers to work with.
    
=== "openEHR"

    openEHR is primarily aimed at the long-term and very detailed recording of medical records, independent of vendors. openEHR also works with the concept of information building blocks, but does so in a more advanced way than FHIR or OMOP. For example, not only elementary building blocks are defined, but composite medical concepts can be defined using so-called archetypes. In terms of syntactic interoperability, openEHR focuses primarily on the structure for **storage**. Where FHIR focuses on *sending* the letter, openEHR focuses on how you *archive* the record in the filing cabinet so that it is still readable in 20 years.

=== "OMOP"

    The Observational Medical Outcomes Partnership (OMOP) standard:
    * *Goal:* Large-scale scientific research and data analysis across multiple hospitals or countries.
    * *How it works:* OMOP forces data from all manner of different systems into one universal table format (the Common Data Model). It converts all data into a standard language so that researchers can ask a single question ("How many people developed influenza after drug X?") to hundreds of different databases.
    * *Syntactic role:* It standardises the database structure for **analysis**.


## _Knowledge organisation systems_ for semantic interoperability

Semantic interoperability aims to enable different computer systems to exchange data with an unambiguous, shared meaning. Unlike syntactic interoperability, which focuses on the format of data exchange, semantic interoperability ensures that the meaning of the data is preserved and consistently understood across different systems. To achieve semantic interoperability, a _knowledge organisation system_ (KOS) is required that consists of several components.

| Purpose | Example | KOS component | Healthcare examples |
|:----------|:----------|:---------|:-----------------|
| **Recognising synonyms** | Emmental, as in Emmental cheese | Word lists, synonym lists | Pinkhof compact medical dictionary |
| **Resolving ambiguity** | Emmental (as cheese) is not the same as Emmental (the valley) | _Authority file_ | Medical Subject Headings (MeSH) |
| **Hierarchical relationships** | Emmental is a cow's milk cheese<br>Cow's milk cheese is a cheese<br>Emmental (valley) is part of Switzerland | Taxonomy | ICD10, ATC |
| **Associative relationships** | Emmental cheese is related to cow's milk<br>Emmental cheese is related to Emmental (valley) | Thesaurus | RxNorm, DHD Diagnosis and procedures thesaurus |
| **Classes, properties, restrictions** | Emmental is a class of cow's milk cheese<br>Cow's milk cheese is a subclass of cheese<br>Every cheese has exactly one country of origin<br>Emmental is made from cow's milk | Ontology | SNOMED CT, LOINC Ontology, KIK-V ontology |

??? info "Explanation and examples KOS"

    The different KOS components can be seen as concentric circles, with word lists being the most basic component and ontologies the most extensive. Here are a few examples.

    * **SNOMED CT** is one of the most comprehensive medical ontologies. It contains concepts for diseases, symptoms, operations, body parts, etc. and associative relationships between these concepts that, for example, link a symptom to a condition.
    * **LOINC** is originally a taxonomy intended for laboratory results and measurements. It has recently been integrated with SNOMED to form the [LOINC Ontology](https://loincsnomed.org/).
    * **RxNorm** is an originally American thesaurus for medications, particularly strong in the US and used in international research (such as with OMOP). In Europe, the aim is to use **[IDMP](https://www.iso.org/obp/ui/en/#iso:std:iso:11616:ed-2:v1:en)**, which is a more comprehensive set of standards for uniquely identifying medications and medicinal products. In the Netherlands, for daily care (prescriptions, pharmacy) the **G-Standard** (managed by Z-Index) is more commonly used, but for international research this is often translated to RxNorm.
    * **ICD-10** is a taxonomy that is primarily used for statistics and billing. It groups diseases into categories.

    It is worth noting that all syntactic standards (FHIR, OMOP, openEHR) always make use of multiple KOS components. At a minimum, code lists (taxonomies) must be used; in the most comprehensive case, an ontology is used. For example, SNOMED is almost always used in implementations of OMOP, openEHR and FHIR.

## Metadata standards for discoverability and accessibility

In addition to semantic and syntactic interoperability, it is also essential that datasets are _findable_ and _understandable_. Metadata not only describes what data is available, but also under what conditions it may be used and via which services the data is accessible. International standards are used for metadata interoperability between data stations.

=== "**DCAT**"

    **DCAT** (Data Catalog Vocabulary) is a W3C standard for describing datasets in data catalogues. It provides a common vocabulary with which organisations can describe their datasets, regardless of the domain.

=== "**DCAT-AP**"

    **DCAT-AP** is a European application profile of DCAT, developed by the European Commission. It refines DCAT with additional mandatory and recommended fields relevant to European government data, such as access rights and applicable legislation.

=== "**HealthDCAT-AP**"

    **HealthDCAT-AP** is an extension of DCAT-AP specifically for the healthcare sector. It adds metadata elements that are essential for health data, such as health categories, population characteristics, coding systems, retention periods and the responsible Health Data Access Body (HDAB).

=== "**Health-RI metadata schema**"

    The **Health-RI metadata schema** is a Dutch profile based on DCAT-AP and HealthDCAT-AP, with specific adaptations for the Health-RI Data Catalogue. This schema defines which metadata elements are mandatory, recommended or optional for Dutch health data.

With these metadata standards, data stations can describe their datasets in a structured and interoperable way. Important DCAT classes here are the catalogue (collection of datasets), the dataset itself (logical grouping of data), distributions (concrete forms of access), and data services (operational access points). In addition, account must be taken of the difference between static data sources such as research cohorts and dynamic data sources such as active databases, each with their own approach to version management and metadata maintenance.

---

TEHDAS2 states that SPEs must offer functionality to achieve semantic and syntactic interoperability (see FCR-1 and FCR-2 in the [TEHDAS2 requirements](../appendix/tehdas2-requirements.md)). The following describes how this can be achieved within the data stations.
