# 4.5. Federated analysis

Federated analysis is identical to the concept of _Federated Database Systems_ as first described in the 1980s.[@heimbigner1985federated] In this approach, queries are executed in a decentralised manner on the data stations. The results of these queries are then sent to an aggregation server that combines the results and possibly aggregates them further. In the context of the EHDS, this aggregation server ideally also performs _statistical disclosure control_[@elliot2018future], which monitors that the final result meets pre-defined anonymity requirements. The following provides an overview of the different forms of federated analysis systems, the most common implementations and a look at future developments.


## 4.5.1. Different forms of federated analysis systems

Federated analysis systems can be classified by looking at the degree of data heterogeneity and the number of query interfaces offered, leading to the following simplified classification.

!!! abstract "Simplified classification of federated analysis systems"

    |   | **Homogeneous data** | **Heterogeneous data** |
    |---|:------------------|:--------------------|
    | **Single interface** | **Federated Database System:** Uses homogeneous datastores and a single standard query interface. This often uses a *mediator-wrapper* architecture for data integration. |  **Multistore System:** Integrates heterogeneous datastores (such as a combination of RDBMS, NoSQL and Distributed File Systems) via a single query interface. |
    | **Multiple interfaces** | **Polyglot System:** Uses homogeneous datastores but offers multiple query interfaces, adding semantic richness. | **Polystore System:** The most complex form, in which heterogeneous datastores are exposed via multiple query interfaces. Examples include BigDAWG and Apache Drill. |


    In addition, systems can be classified based on their coupling:

    - **Loosely Coupled:** Autonomous local datastores accessed via a common or local language.
    - **Tightly Coupled:** Systems that use one language to query both structured and unstructured data, often focused on performance and self-tuning.
    - **Hybrid Systems:** A combination of both approaches.

The functionality and user experience of a federated analysis system is primarily determined by the query interface(s) offered.

!!! abstract "Most common query interfaces"

    === "SQL"

        SQL (Structured Query Language, originally SEQUEL) is an ANSI/ISO standard language for a relational database management system (DBMS). It is a standardised language that can be used for tasks such as querying and modifying data in a relational database. SQL can be used with virtually all modern relational database products.
    
    === "NoSQL"

        "No SQL" or 'Not Only SQL' is based on a document database, in which data is stored in JSON format. MongoDB is an example of this. There is currently no open standard for NoSQL.

    === "Graph Query Language"

        Graph Query Language (GQL) is a new standard for querying Labeled Property Graphs. GQL is derived from Cypher, the query language of neo4j, which is one of the most widely used labeled property graph engines. GQL was established as a standard in ISO/IEC 39075 in April 2024.

    === "SPARQL"

        SPARQL (SPARQL Protocol And RDF Query Language) is a query interface for triple stores and RDF-based data. With this query language it is possible to retrieve information for applications on the semantic web. It is a W3C standard; version 1.1 was established in 2009.

    In recent years, technologies have been developed that automatically translate between these different query interfaces. One example is [Ontop](https://ontop-vkg.org/), which makes it possible to query relational databases with SPARQL.



## 4.5.2. Most common implementations

Federated database systems have been used by organisations for quite some time. By way of illustration, we sketch the most widely used implementations.

!!! abstract "Most widely used federated database systems"

    === "Federated Database System"

        Virtually all mature database systems support federated analysis. For example, PostgreSQL, one of the most widely used open source relational database systems, has the [_foreign data wrapper_ extension](https://www.postgresql.org/docs/current/postgres-fdw.html) which allows federated queries to be executed across a network of PostgreSQL databases. In the case of MongoDB, the most widely used open source document database, federated queries are supported via [Atlas](https://www.mongodb.com/docs/atlas/data-federation/query/query-federated-database/).

    === "Multistore system"

        Many mature database platforms offer functionality to query different database formats via a single query interface. One example is Microsoft PolyBase, which allows relational data, document data and data on cloud storage to be queried with T-SQL (Microsoft SQL Server's SQL dialect).

    === "Polyglot system"

        Spark SQL was one of the first federated polyglot systems. With this open source technology, different relational data can be queried with either a SQL interface (Spark SQL) or a dataframe interface (Spark DataFrames). Since then, many data analysis platforms have become polyglot. The Python data stack has also become fully polyglot: users can freely switch between a SQL or a dataframe interface with open source libraries such as DuckDB, polars and Ibis.

    === "Polystore system"

        TO DO: are there really no polystore systems that are widely used yet?

The current generation of federated systems (such as BigDAWG, CloudMdsQL and Myria) focuses on integrating relational data with various NoSQL and file formats.

* 
**Query languages:** The standard is predominantly SQL-like (such as HiveQL, SparkSQL) to facilitate integration, although some systems support native query languages or functional languages to exploit specific properties of underlying databases.


* 
**Schema management:** Most multistores use a *Global-as-View (GAV)* or *Local-as-View (LAV)* approach to define global schemas across the local sources.


* 
**Optimisation:** Query optimisation takes place via cost models or heuristics, applying techniques from distributed databases, such as *bind joins* and pushing selections to the source (pushdown).



## 4.5.3. Future developments and challenges

To develop data stations further towards fully fledged federated analysis platforms, various technological challenges must still be overcome:

- **Semantic mapping:** Automatically translating queries into the local dialect of a storage system and integrating results remains a challenge.
- **Distributed transactions:** Managing transactions across heterogeneous systems, especially when NoSQL stores (which often do not support ACID) are involved, requires new standards.
- **Complex analytics & linear algebra:** The shift from simple aggregations (COUNT, SUM) to predictive models (machine learning) requires the integration of linear algebra within the database system. Current systems often need to inefficiently convert data between storage and algebraic computation packages; a closer, less costly integration is necessary.
- **Data placement and shuffle:** Systems need to become more intelligent in moving data and intermediate results (shuffling) to the _engine_ that has the best model to answer a specific query.
- **Benchmarks:** There is a need for standards and benchmarks (such as PolyBench) to objectively evaluate the performance of complex polystores and federated combinations.
