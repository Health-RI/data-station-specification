A shift towards federated data systems as a design paradigm

The ambition for a seamlessly connected digital healthcare ecosystem, capable of leveraging vast quantities of patient data remains illusive. Designing and implementing health data platforms is notoriously difficult, given the heterogeneity and complexity of such systems. To address these issues, federated data systems are gaining traction as an overarching design paradigm in which data to remains securely at its source and computations are performed in a decentralized, distributed fashion.

Recent technological inventions offer important new enablers to implement federated data systems, most notably:

Significant increase in single-node computing capabilities, whereby it is now possible to process up to 1 TB of tabular data on a single machine node thereby enabling increasingly large volumes of data to be processed in a decentralized, federated system [@raasveldt2019duckdb; @nahrstedt2024empirical];

Maturity of federated analytics and specifically federated learning as a means of performing analysis whilst 'hiding' the data from third parties, including training of deep learning models through aggregation of weights [@wang2025survey; @rieke2020future; @teo2024federated];

Privacy-enhancing technologies (PETs) such as secure multi-party computation (MPC) that are now sufficiently mature to be used on an industrial scale, enabling computations to be done under encryption (in-the-blind) thereby significantly improving security across a network of participants [@un2023pet-guide; @royalsociety2023privacy];

The composable data stack as a solution design that allows for unbundling of the venerable relational database into loosely coupled components, thereby making it easier and more practical to implement federated data systems using cloud-based components with microservices and thus opening up a transition path towards more modular and robust architectures [@pedreira2023composable; @composable].

The architectural shift from centralized to federated data systems is not merely a technical evolution. Modern approaches to data governance are undergoing a similar paradigm shift towards federated solutions. Federated data systems are inherently more aligned with contemporary data governance frameworks, including the Data Governance Act (DGA), the European Health Data Space (EHDS) and the concept of data solidarity [@prainsack2023beyond]. Within the context of large corporations, the concept of a data mesh is increasingly being adopted as well, which in essence is a federation of data producers and consumers within a commercial enterprise. From the perspective of sovereignty and solidarity, we believe that a commons-based, federated approach has distinct benefits in moving towards a more equitable, open digital infrastructure [@krewer2024digital].

However, this ongoing paradigm shift towards is not without challenges. The notion of what constitutes a federated data system needs to be defined in more detail if we are to see the forest for the trees between different meanings of the same word. For example, 'federation' can refer to any of the following concepts:

Data federation in de context of distributed databases addresses the problem of uniformly accessing multiple, possibly heterogeneous data sources, by mapping them into a unified schema, such as an RDF(S)/OWL ontology or a relational schema, and by supporting the execution of queries, like SPARQL or SQL queries, over that unified schema [@gu2022systematic];

Federation within the context of a Personal Health Train (PHT) refers to the concept where data processing is brought to the (personal health) data rather than the other way around, allowing (private) data accessed to be controlled, and to observe ethical and legal concerns [@beyan2020distributed; @choudhury2020personal; @boninodasilvasantos2022personal; @zhang2023secure; @choudhury2025advancing], and is just one of many solutions designs that are collectively grouped as federated analytics [@wang2025survey];

Federation in Trusted Research Environment (TRE) pertains to a mechanism for data sharing in a temporary staging environment within a network of research organizations through federations services such as localization and access [@eosc-entrust];

Federation in the context of data spaces, as described in the DSSC Blueprint 2.0, pertains to the support the interplay of participants in a data space, operating in accordance to the policies and rules specified in the Rulebook by the data space authority.

What then, is a viable development path out of this creative chaos?