# Standaarden

[TO DO: vertalen naar het Nederlands]

The following are the standards that have been used or are in the process of being used for composable data stations. However, this specification is **not limited to supporting these standards or open source application components**.

## Infrastructure standards

**Standard** | **Purpose**
:--|:--
[Apache Arrow](https://arrow.apache.org/) | **Apache Arrow** defines a language-independent columnar memory format for flat and nested data, organized for efficient analytic operations on modern hardware like CPUs and GPUs. The Arrow memory format also supports zero-copy reads for lightning-fast data access without serialization overhead.
[Arrow Database Connectivity (ADBC)](https://arrow.apache.org/adbc/current/index.html) | **ADBC** is a set of APIs and libraries for Arrow-native access to databases. Execute queries and get back results in Arrow format, eliminating extra data copies.
[Apache Parquet](https://parquet.apache.org/) | **Apache Parquet** is an open source, column-oriented data file format designed for efficient data storage and retrieval. It provides high performance compression and encoding schemes to handle complex data in bulk and is supported in many programming language and analytics tools.
[Lance](https://lancedb.github.io/lance/) | **Lance** is a modern columnar data format optimized for machine learning and AI applications. It efficiently handles diverse multimodal data types while providing high-performance querying and versioning capabilities.
[Substrait](https://substrait.io/) | **Substrait** is a format for describing compute operations on structured data. It is designed for interoperability across different languages and systems.
[SQL-on-FHIR](https://build.fhir.org/ig/FHIR/sql-on-fhir-v2/) | **SQL-on-FHIR** specifies an approach to make large-scale analysis of FHIR data accessible to a larger audience and portable between systems. The central goal of this project is to make FHIR data work well with the best available analytic tools, regardless of the technology stack.

## Information standards

**Standard** | **Purpose**
:--|:--
[FHIR to OMOP](https://build.fhir.org/ig/HL7/fhir-omop-ig/)| **FHIR to OMOP** is a FHIR Implementation guide that provides details on how to transform healthcare data from FHIR to the OMOP Common Data Model. It aims to bridge the gap between these two widely used formats in healthcare and research. The standard defines mappings between FHIR resources and OMOP data tables, focusing on commonly used EHR data.
[FHIRconnect](https://sevkohler.github.io/FHIRconnect-spec/build/site/FHIRconnect/v1.0.0/index.html) | **FHIRconnect** is a mapping specification for bidirectional mapping between openEHR and FHIR. The goal is to create a mapping language that communities can use to transform data between these standards. The markup language used to express the mappings is YAML.


## Open source application components

**Component** | **Purpose**
:--|:--
[DuckDB](https://duckdb.org) | **DuckDB** is an in-memory, embeddable, columnar database management system designed for analytical workloads. It is simple to use becasue it requires no external dependencies and data can be stored in a persistent, single-file database. It offers a flexible extension mechanism that allows defining new data types, file formats and SQL syntax.
[Polars](https://pola.rs) | **Polars** is an open-source library for data manipulation, known for being one of the fastest data processing solutions on a single machine. It features a well-structured, typed API that is both expressive and easy to use.
[Kuzu](https://docs.kuzudb.com/) | **Kuzu** is an embedded property graph database that supports the Cypher query language. It is optimized for handling complex join-heavy analytical workloads on very large graphs.
[LanceDB](https://lancedb.com/) | **LanceDB** is an open-source multimodal lakehouse that can be used as a vector database and memory for large-scale Generative AI and Search applications, and as a data management platform for large-scale AI workflows: model fine-tuning and training, feature engineering and explorative data analytics over petabyte-size Lance datasets.



## Commercial application components

**Component** | **Purpose**
:--|:--
[openFHIR](https://open-fhir.com/documentation/1.2.6/overview.html) | **OpenFHIR** is a engine designed to process and transform healthcare data using between FHIR and openEHR, based on the FHIR Connect specification.


