# Infrastructure

The PLUGIN infrastructure consists of central and decentralised components that together form the federated platform. As the orchestration and communication layer between the central and decentralised components, PLUGIN uses vantage6. Vantage6 is an open-source Python application for setting up a federated network and executing containerised tasks on decentralised data stations. The central vantage6 server coordinates the communication and execution of tasks, while the vantage6 nodes at the data stations are responsible for receiving and executing those tasks.

## Central components

At the heart of the PLUGIN infrastructure is a central vantage6 server. This server makes it possible to set up tasks via a web interface or client for the data stations. The central vantage6 server consists of the following components:

- The central vantage6 server application, running within a Docker container.
- A database (PostgreSQL) for storing metadata of users, organisations, tasks, etc.
- A UI (web interface) for managing users, organisations, data stations and tasks.
- Optionally, large file storage (blob storage) for storing task results for efficient transfer.

The central vantage6 server's primary purpose is the authentication, authorisation and coordination of tasks towards the decentralised data stations.

In addition to the central server, one or more central Docker registries are required for storing the algorithm containers that are executed on the data stations. Access to these is configured at the data stations, but via a central algorithm registry, access to specific algorithm containers can also be managed centrally.

## Decentralised components

The decentralised components within a PLUGIN infrastructure consist of the previously mentioned components in the application layer and can be summarised as the vantage6 node, PLUGIN-Lake and algorithm containers.

!!! abstract "Decentralised components"

    === "Vantage6 Node"

        The vantage6 node is the gateway to the federated network and the local orchestration layer within the data station. The node queries the central vantage6 server and receives tasks to be executed as containerised applications. The vantage6 node then establishes a temporary network between the available data sources and the algorithm container. After execution of the task, the results are sent back via the node to the central vantage6 server and the algorithm container is cleaned up.

    === "PLUGIN-Lake"

        PLUGIN-Lake sits between the available data sources and the vantage6 node. PLUGIN-Lake ensures uniform access to the data sources and any data transformations required to provide the data to the algorithm container in the desired format.

    === "Algorithm container"

        An algorithm container contains the task-specific code required to perform a certain task. The node retrieves the container from the central Docker Registry and launches it within a temporary network. The algorithm container can then only communicate with the data sources and services within a data station that have been made available via the vantage6 node.

## Infrastructure requirements for data station

To participate in the PLUGIN platform, requirements are imposed on the data station within a participating organisation. Each participating organisation must make its own machine (physical or virtual) available on which the decentralised components of the PLUGIN platform can run.

!!! abstract "Data station requirements"

    === "System requirements"

        To ensure the stability and performance of the platform, the following minimum system requirements apply to the data station:

        - **Linux operating system**: Due to the intensive use of container technology (Docker or Kubernetes), a Linux operating system is required.
        - **CPU 16 cores, x86/x64 CPU**: A multi-core CPU is required for executing algorithms.
        - **RAM 64 GB**: Sufficient RAM is necessary when working with large datasets or data-intensive algorithms.
        - **SSD 360 GB**: Storage of (meta)data
        - *Optional: **NVIDIA GPU (≥ 16 GB VRAM)**: An NVIDIA-compatible GPU is required when making a data station available for the development of AI models.

    === "Network requirements"

        To be able to participate in the PLUGIN infrastructure, the data station must be able to communicate with the central vantage6 server. The following network requirements apply:

        - **100 Mbit/s ethernet**
        - **Port 443/TCP open for outbound traffic**

        The following endpoints must be reachable from the data station:

        - Address of the central vantage6 server(s) to which the data station connects
        - Vantage6 Docker registry
        - Docker registries of algorithm containers
        - *Any access to repositories for software and dependency updates*

    === "Software requirements"

        - **Docker**: Docker is required to run the vantage6 node and algorithm containers.
        - **Python 3.10**: Required for setting up a vantage6 node
        - **vantage6**: Python package that makes vantage6 available as a Command Line Interface (CLI)

        The remaining applications are installed as containerised applications. Docker Compose, Kubernetes and optionally Linux native tools are used to manage these.

## Access to data

To be able to guarantee interoperability within the PLUGIN platform, it is necessary for data to be made available to algorithm containers in a standardised manner. To achieve this, PLUGIN chooses FHIR as the information standard for clinical data.

Although vantage6 offers the ability to access data sources directly from the algorithm container, PLUGIN opts for an intermediate layer: PLUGIN-Lake. PLUGIN-Lake ensures uniform access to the data sources and any data transformations required to provide the data to the algorithm container in the desired format.

Data sources can be unlocked within a data station, and therefore PLUGIN-Lake, in various ways. We distinguish between the following sources:

- Local files (CSV, JSON, XML, etc.) available on the data station
- APIs providing access to the data (e.g. REST APIs)

Via PLUGIN-Lake (or vantage6 node), the various data sources can be unlocked and made available to the algorithm container in the desired format (e.g. as FHIR resources in nd-json format).

Some examples of data sources that can be unlocked within PLUGIN-Lake:

- A FHIR server (e.g. HAPI or Firely)
- A relational database (e.g. SQL Server or PostgreSQL)
- Object storage (e.g. Azure Blob Storage or AWS S3)
- Local files on the server itself or a network share


<!-- ## Making data available
To enable federated applications, it is important that every participant makes their clinical data available to the platform in the same way. In addition to the syntactic and semantic interoperability mentioned earlier, it is necessary to agree on technical standards. If, for example, FHIR is chosen as the information standard, the technical interface can be implemented in various ways:


1. Via a FHIR server and the associated [REST API](https://hl7.org/fhir/http.html), such as [HAPI](https://hapifhir.io/hapi-fhir/) or [Firely](https://fire.ly/products/firely-server/) Server. For efficient data transfer, the [bulk data API](https://hl7.org/fhir/uv/bulkdata/) and [nd-json](https://hl7.org/fhir/nd-json.html) could be used.
2. Via a relational database, such as [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2022) or [PostgreSQL](https://www.postgresql.org), where FHIR resources are stored either i) in tabular form (with each attribute of a resource in a separate column), or as a document (in a column of type JSON-B).
3. Via a data lake / blob storage, where resources are stored as [nd-json](https://hl7.org/fhir/nd-json.html) files and accessed via an (in-process) database management system (such as [DuckDB](https://duckdb.org)).

Undoubtedly other options are possible as well.

The first option has the advantage that other applications within the hospital can use the same server, for example for Clinical Decision Support. The second option aligns well with the technology stack already available in many hospitals and is already applied by LUMC, ErasmusMC and UMCUtrecht. The third option is probably (financially) the most advantageous, as only data storage is required; a database or application server is not necessary. -->
