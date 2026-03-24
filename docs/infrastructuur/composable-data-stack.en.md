# 5.2. A data station with the composable data stack

## 5.2.1. The principles of the composable data stack

As established earlier, the data station's task is to converge data holder-specific data into reliable and accessible information. Each data station operates in a unique organisational context with its own systems, compliance requirements and technical capabilities. Via a lakehouse architecture, a data station retains the flexibility to make diverse data available and processable, while a generic minimum standard is enforced through metadata management and open standards. The standardised metadata layer provides the necessary central coordination without curtailing local autonomy. This metadata layer functions as the common language forming the basis for federated collaboration and interoperability.

!!! abstract "Core principles of the composable data stack"
    
    The foundation of a composable architecture rests on three pillars:

    1. **Modularity:** Components (building blocks) can be replaced or scaled independently of one another.
    2. **Interoperability:** Thanks to open standards (such as Apache Arrow and Parquet), different systems can work together without costly conversions.
    3. **Decoupling:** Physical storage (_storage_), data processing (_compute_) and schema information (_catalog_) are strictly separated from one another.

Decoupling of functions is one of the most important design principles of the data station. At the time of writing these specifications, the data engineering community offers proven technical components that can be used.

=== "Storage"

    In traditional systems, data is often stored in a proprietary, closed format that can only be read by the associated database engine. In the Composable Data Stack, the storage layer is agnosticised.

    * **Open file formats:** Data is stored in standardised column-oriented formats such as **Apache Parquet**. This makes the data accessible to a wide range of tools without requiring the data to be moved or transformed.
    * **Lakehouses:** By using object storage (such as S3 or Azure Blob) as a central source, the storage layer acts as a 'single source of truth' that can grow independently of compute capacity.

=== "Compute"

    By decoupling from storage, the compute layer becomes replaceable. This enables organisations to use different specialised engines on the same dataset.

    * **Engine-agnostic processing:** An organisation can run SQL queries with one engine (e.g. DuckDB or Trino), while a data scientist simultaneously trains machine learning models with another tool (e.g. PyTorch), directly on the same data.
    * **Efficient data exchange:** To ensure speed between different compute engines, **Apache Arrow** acts as the *lingua franca* for in-memory data. This minimises the overhead of serialisation and deserialisation (the conversion of data formats).

=== "Catalog"

    The connecting factor in a decentralised stack is the metadata layer. Without central metadata, fragmentation arises.

    * **Table formats:** Technologies such as **Apache Iceberg** or Delta Lake add an abstraction layer on top of raw files. They manage metadata about which files belong to which table, support transactions (ACID) and enable time-travel through data.
    * **Catalogue:** The catalogue functions as the inventory of the entire stack. It tracks where data resides, who owns it and what its structure (schema) is. This is essential for discoverability and governance, comparable to the FAIR principles (Findable, Accessible, Interoperable, Reusable).

    !!! warning "Catalog vs. metadata"

        The catalogue in the composable data stack refers to the information schema of the data. Open standards such as Apache Iceberg and DuckLake will be used for this purpose. This catalogue is different from the metadata catalogue based on DCAT, which is described as a generic function within the national network.

## 5.2.2. Declarative ETL data processing pipelines

Another essential aspect of the composable data stack is working with so-called declarative ETL processing pipelines. In traditional data engineering (imperative ETL), the focus is on *how* data is moved and transformed via complex scripts. The shift to a **declarative approach** is fundamentally different: the focus shifts to *what* the end result should be. This forms the basis for reliably scaling data ecosystems and delivering high-quality data products within decentralised networks and data spaces.

=== "Declarative ETL"
    
    A declarative pipeline (based on principles of the *Modern Data Stack* and *Functional Data Engineering*) describes the desired end state of the data, rather than the specific steps to get there.

    * **Definition over execution:** Instead of a sequence of scripts (e.g. "step A, then step B"), the developer defines the logic of the transformation (e.g. via SQL or YAML). The underlying system (such as dbt, Dagster or Spark Declarative Pipelines) determines the optimal sequence, dependencies and required compute. This approach makes it possible to implement the new information standards described in [chapter 3](../informatie/index.md) efficiently within data stations.
    * **Idempotence and reproducibility:** Because the outcome is defined, a pipeline can be run repeatedly with the same input without unexpected side effects. This is crucial for error correction and historical recomputation of data.
    * **Self-healing and lineage:** The system understands the relationships between datasets automatically. If a source file changes, the declarative stack knows exactly which derived tables need to be updated.

=== "Data products"

    The move to declarative pipelines makes it possible to view data no longer as a by-product of a process, but as a fully-fledged **data product**. A data product is an autonomous, readable and directly usable unit of information.

    * **Quality guarantees (SLAs):** A data product contains not only the raw data, but also metadata about quality, provenance (lineage) and currency.
    * **Ownership:** By defining logic declaratively, it is easier to assign responsibility to the domain experts who understand the data best.
    * **Consumption-oriented:** A data product is designed for the end user (e.g. a researcher or analyst) and is directly accessible via standard interfaces (such as APIs or open table formats) without requiring in-depth knowledge of the source code.

    In practice, a single ETL processing pipeline may therefore produce multiple data products that are made available for secondary use.

=== "Integration in data spaces"

    In a **Data Space** (a federated network in which organisations securely exchange data), data products are the central objects of transaction. Declarative pipelines are the 'factory' that reliably produces these products.

    * **Interoperability:** In a data space, different parties must be able to understand each other's data. Declarative definitions enforce the use of shared schemas and semantic standards, which is essential for automatic integration.
    * **Sovereignty and governance:** Because the transformation logic is transparent and documented (as code), policy rules for access and privacy (e.g. anonymisation) can be directly integrated into the pipeline definition.
    * **Scalability in federations:** When every participant in a data space offers their data as a standardised data product (produced via declarative methods), a scalable network emerges. New sources can easily be onboarded without requiring changes to the central architecture.
