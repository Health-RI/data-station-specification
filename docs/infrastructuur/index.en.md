# 5. Perspective: infrastructure

## Challenges in the design and implementation of a decentralised data infrastructure

**Heterogeneous data and systems**

In a decentralised network, data does not reside in a central location but is distributed across multiple data stations. Each data station has its own data ecosystem with its own context and extraction methods specific to the data holder's domain. Whereas first-generation data warehouses primarily contained tabular data, data holders today manage a heterogeneous mix of different data types and degrees of structure, with a continuous stream of incoming information.

In a decentralised network, the data station is the gateway from an organisation's internal data to the federated network. The data station therefore plays an essential role in converging the organisation's own data towards a standard for reuse. To accommodate this diversity — both between organisations and within the data itself — a data infrastructure must strike a balance between flexibility and operability.

**Late binding for data quality**

To maintain the balance between flexibility and operability, it is important to separate the quality requirements imposed on a dataset into minimum technical quality requirements and contextual quality requirements. An infrastructure must ultimately be able to understand data sufficiently to process it, but the contextual quality requirements of data are often strongly use-case-dependent.

A data infrastructure within a data station is only responsible for the technical "readability" of the data, so that collecting metadata and making data available for further processing is not impeded. This principle of **late binding** means that data is not rejected upfront on substantive grounds, but on "readability" and technical accessibility. Substantive quality requirements can then be applied progressively through selection and ETL processes, preserving semantic interoperability without premature data exclusion.

**Metadata without data exposure**

To be able to provide a reliable central reflection of the data available within a data station at all times, facilitating a reliable metadata catalogue is crucial. It is therefore essential to incorporate monitoring as an integral and automated process so that no discrepancies can arise between the data itself and the available metadata. This metadata can then be made available to central processes, enabling users to access all information needed for use without the data itself having to be exposed.

Given these challenges, this chapter discusses the key principles for implementing data station infrastructure using existing technologies. First, the evolution of data infrastructures is used to explain the various options and concepts. The technical infrastructure specification for a data station is then described in terms of the lakehouse architecture and the _composable data stack_.
