# 5.3. Standards and open source components

The following standards are used or are currently being used for composable data stations, aimed at making available clinical data that are routinely recorded. However, this specification is **not limited to supporting these standards or open source application components**. This list is an initial starting point and is not intended as a comprehensive overview.

**Standard** | **Purpose**
:--|:--
[Apache Arrow](https://arrow.apache.org/) | **Apache Arrow** defines a language-independent columnar memory format for flat and nested data, organised for efficient analytic operations on modern hardware such as CPUs and GPUs. The Arrow memory format also supports zero-copy reads for lightning-fast data access without serialisation overhead.
[Arrow Database Connectivity (ADBC)](https://arrow.apache.org/adbc/current/index.html) | **ADBC** is a set of APIs and libraries for Arrow-native access to databases. Execute queries and receive results in Arrow format, eliminating extra data copies.
[Apache Parquet](https://parquet.apache.org/) | **Apache Parquet** is an open source, column-oriented data file format designed for efficient data storage and retrieval. It provides high-performance compression and encoding schemes to handle complex data in bulk and is supported in many programming languages and analytics tools.
[DuckLake](https://ducklake.select/) | **DuckLake** is an open-source specification for implementing the catalogue function with a relational database.
[Lance](https://lancedb.github.io/lance/) | **Lance** is a modern columnar data format optimised for machine learning and AI applications. It efficiently handles diverse multimodal data types while providing high-performance querying and versioning capabilities.
[Substrait](https://substrait.io/) | **Substrait** is a format for describing compute operations on structured data. It is designed for interoperability across different languages and systems.
[SQL-on-FHIR](https://build.fhir.org/ig/FHIR/sql-on-fhir-v2/) | **SQL-on-FHIR** is a specification that makes large-scale analysis of FHIR data accessible to a wider audience and portable between systems. The central goal of this project is to make FHIR data work well with the best available analytic tools, regardless of the technology stack.
[CSVW](https://csvw.org/) | **CSVW** (CSV on the Web) is a standard for describing CSV files with metadata, making them more interoperable and machine-readable.

## Information standards

**Standard** | **Purpose**
:--|:--
[FHIR to OMOP](https://build.fhir.org/ig/HL7/fhir-omop-ig/)| **FHIR to OMOP** is a FHIR implementation guide that describes how healthcare data can be transformed from FHIR to OMOP. It aims to bridge the gap between these widely used standards in healthcare and research. The standard defines mappings between FHIR resources and OMOP data tables, focusing on the most commonly used EHR data.
[FHIRconnect](https://sevkohler.github.io/FHIRconnect-spec/build/site/FHIRconnect/v1.0.0/index.html) | **FHIRconnect** is a mapping specification for bidirectional mappings between openEHR and FHIR. The goal is to create a mapping language that communities can use to transform data between these standards. YAML is used to express the mappings.

## Open source application components

**Component** | **Purpose**
:--|:--
[DuckDB](https://duckdb.org) | **DuckDB** is an in-memory, embeddable, column-oriented database management system designed for analytical workloads. It is simple to use because it requires no external dependencies and data can be stored in a persistent, single-file database. It offers a flexible extension mechanism that allows defining new data types, file formats and SQL syntax.
[Polars](https://pola.rs) | **Polars** is an open-source library for data manipulation, known as one of the fastest data processing solutions on a single machine. It features a well-structured, typed API that is both expressive and easy to use.
[LadybugDB](https://ladybugdb.com/) | **LadybugDB** is an embedded property graph database that supports the Cypher query language. It is optimised for handling complex join-heavy analytical workloads on very large graphs.
[LanceDB](https://lancedb.com/) | **LanceDB** is an open-source multimodal lakehouse that can be used as a vector database and memory for large-scale Generative AI and search applications, and as a data management platform for large-scale AI workflows: model fine-tuning and training, feature engineering and exploratory data analytics over petabyte-size Lance datasets.

## Commercial application components

**Component** | **Purpose**
:--|:--
[openFHIR](https://open-fhir.com/documentation/1.2.6/overview.html) | **OpenFHIR** is an engine designed to process and transform healthcare data between FHIR and openEHR, based on the FHIR Connect specification.
