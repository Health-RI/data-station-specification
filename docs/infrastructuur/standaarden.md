# Standaarden en open source applicatie componenten

De volgende standaarden zijn gebruikt of worden momenteel gebruikt voor composable data stations. Deze specificatie is echter **niet beperkt tot ondersteuning van deze standaarden of open source applicatiecomponenten**.

## Infrastructuur standaarden

**Standaard** | **Doel**
:--|:--
[Apache Arrow](https://arrow.apache.org/) | **Apache Arrow** definieert een taalonafhankelijk kolom-georiënteerd geheugenformaat voor platte en geneste data, georganiseerd voor efficiënte analytische operaties op moderne hardware zoals CPU's en GPU's. Het Arrow geheugenformaat ondersteunt ook zero-copy reads voor bliksemsnelle datatoegang zonder serialisatie-overhead.
[Arrow Database Connectivity (ADBC)](https://arrow.apache.org/adbc/current/index.html) | **ADBC** is een set API's en bibliotheken voor Arrow-native toegang tot databases. Voer queries uit en ontvang resultaten in Arrow-formaat, waarbij extra data-kopieën worden geëlimineerd.
[Apache Parquet](https://parquet.apache.org/) | **Apache Parquet** is een open source, kolom-georiënteerd data-bestandsformaat ontworpen voor efficiënte data-opslag en -ophaling. Het biedt hoogwaardige compressie- en coderingsschema's om complexe data in bulk te verwerken en wordt ondersteund in een groot aantal programmeertalen en analysetools.
[Lance](https://lancedb.github.io/lance/) | **Lance** is een modern kolom-georiënteerd dataformaat geoptimaliseerd voor machine learning en AI-applicaties. Het verwerkt efficiënt diverse multimodale datatypes en biedt hoogwaardige query- en versiebeheermogelijkheden.
[Substrait](https://substrait.io/) | **Substrait** is een formaat voor het beschrijven van rekenoperaties op gestructureerde data. Het is ontworpen voor interoperabiliteit tussen verschillende talen en systemen.
[SQL-on-FHIR](https://build.fhir.org/ig/FHIR/sql-on-fhir-v2/) | **SQL-on-FHIR** is een specificatie welke grootschalige analyse van FHIR-data toegankelijk maakt voor een breder publiek, en deze overdraagbaar maakt tussen systemen. Het hoofddoel van dit project is om FHIR-data goed te laten werken met de beste beschikbare analysetools, ongeacht de technologie-stack.

## Informatie standaarden

**Standard** | **Purpose**
:--|:--
[FHIR to OMOP](https://build.fhir.org/ig/HL7/fhir-omop-ig/)| **FHIR to OMOP** is een FHIR implementatiegids waarin beschreven wordt hoe zorgdata getransformeerd kan worden van FHIR naar OMOP. Ze tracht het gat te dichten tussen deze veelgebruikte standaarden in de zorg en in onderzoek. De standaard definieert mappings tussen FHIR resources en OMOP data tabellen, zich richtend op de meest gebruikte EPD-data.
[FHIRconnect](https://sevkohler.github.io/FHIRconnect-spec/build/site/FHIRconnect/v1.0.0/index.html) | **FHIRconnect** is een mapping specificatie voor bidirectionele mappings tussen openEHR en FHIR. Het doel is een mappinglanguage te maken die gebruikt kan worden door communities om data tussen deze standaarden te transformeren. YAML wordt gebruikt om de mappings uit te drukken.

## Open source applicatiecomponenten

**Component** | **Doel**
:--|:--
[DuckDB](https://duckdb.org) | **DuckDB** is een in-memory, embeddable, kolom-georiënteerd databasebeheersysteem ontworpen voor analytische workloads. Het is eenvoudig te gebruiken omdat het geen externe afhankelijkheden vereist en data kan worden opgeslagen in een persistent single-file database. Het biedt een flexibel extensiemechanisme waarmee nieuwe datatypes, bestandsformaten en SQL-syntax kunnen worden gedefinieerd.
[Polars](https://pola.rs) | **Polars** is een open-source bibliotheek voor datamanipulatie, bekend als een van de snelste dataverwerkingsoplossingen op een enkele machine. Het beschikt over een goed gestructureerde, getypeerde API die zowel expressief als gebruiksvriendelijk is.
[Kuzu](https://docs.kuzudb.com/) | **Kuzu** is een embedded property graph database die de Cypher-querytaal ondersteunt. Het is geoptimaliseerd voor het verwerken van complexe join-intensieve analytische workloads op zeer grote grafen.
[LanceDB](https://lancedb.com/) | **LanceDB** is een open-source multimodaal lakehouse dat kan worden gebruikt als vectordatabase en geheugen voor grootschalige Generative AI- en zoektoepassingen, en als datamanagementplatform voor grootschalige AI-workflows: model fine-tuning en training, feature engineering en verkennende data-analyse over petabyte-grote Lance datasets.

## Commerciële applicatiecomponenten

**Component** | **Doel**
:--|:--
[openFHIR](https://open-fhir.com/documentation/1.2.6/overview.html) | **OpenFHIR** is een engine ontworpen om healthcare data te verwerken en transformeren tussen FHIR en openEHR, gebaseerd op de FHIR Connect-specificatie.
