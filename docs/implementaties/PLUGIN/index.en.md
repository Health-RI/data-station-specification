# PLUGIN Healthcare

The **Pl**atform for **U**tilisation and Reu**s**e of Cl**i**nical Data i**n** the Netherlands (PLUGIN) aims to unlock clinical data in the Electronic Patient Records (EPRs) of Dutch hospitals in a secure, scalable and sustainable manner. PLUGIN originated as an initiative of [Dutch Hospital Data](https://www.dhd.nl/), [Integraal Kankercentrum Nederland](https://iknl.nl/) and [Expertisecentrum Zorgalgoritmen](https://zorgalgoritmen.nl/). The basic infrastructure uses [vantage6](https://vantage6.ai/) and makes it possible to make medical data available in a decentralised manner for both general data exchange and federated learning and analysis.

With use cases [AI-assisted coding](https://www.dhd.nl/producten-diensten/registratie-data/ondersteuning-bij-medische-codering/ai-ondersteund-coderen) and [populating and enriching the NKR](https://www.icthealth.nl/nieuws/veilig-en-efficient-data-delen-dankzij-het-plugin-initiatief), it has been demonstrated that the infrastructure can be deployed at scale for the three types of federated data processing.

The PLUGIN infrastructure implements various components as shown in the diagram and table below, which are explained on the following pages.

![](./plugin-overzicht.drawio.en.svg)

!!! note "List of components"

    | Component | Function |
    |:----|:---------|
    | PLUGIN-Analytics | Component for federated analysis |
    | PLUGIN-ML | Component for federated learning |
    | PLUGIN-Hub | Component enabling federated data submissions (data pooling) |
    | vantage6 server | Central processing hub on which users, organisations, collaborations, tasks and results are managed and orchestrated |
    | vantage6 UI | Web application through which users can interact with the server |
    | vantage6 API | Programmatic control of the server, including Python client and R client |
    | Docker registry | Containers authorised to run decentrally on the data stations |
    | Algorithm store | Metadata of the (algorithm) containers, including support for the approval process |
    | vantage6 node | Decentralised component of the processing hub that executes local computations |
    | algorithm container | Temporary local copy of the algorithm being executed, created and removed by the vantage6 node |
    | PLUGIN-Lake | Lakehouse for serverless storage and ETL transformations on the data station |


??? info "External documentation"

    - [PLUGIN programme website](https://plugin.healthcare/)
    - [Installation guide AI-assisted coding](https://installatiegids-aioc.dhd.nl/)
    - [vantage6 user documentation](https://docs.vantage6.ai/en/main/)
    - [vantage6 journal paper](https://vantage6.ai/documents/7/moncada-torres2020vantage6_57GU4Gt.pdf)
    - [vantage6 software management plan](https://vantage6.ai/documents/27/vantage6-software-management-plan-v1.0.pdf)
