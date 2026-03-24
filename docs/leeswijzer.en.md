# 1.3. Research questions and reading guide

## 1.3.1. Core design and research questions

This document elaborates the architecture of a hybrid SPE that can be implemented as part of a nationally covering basic infrastructure for the secondary use of data. The following design and research questions are central to this:

- Can a unambiguous functional and technical specification be given of a hybrid SPE based on data stations and processing hubs, that is consistent with existing reference architectures?
- In what way could data stations be standardised to achieve maximum interoperability between different networks (a data station connected to multiple processing hubs)?
- In what way can data stations be used for data pooling to a central TRE? What options are there for achieving standardisation in this area?
- Are there gaps or contradictions in the current EHDS approach for secondary use that obstruct the use of a hybrid SPE, particularly in relation to data stations for primary use? If so, what solution directions are there?
- What is the maturity of the existing reference implementations relative to the design described above:
    - KIK-V as a reference implementation of data stations for federated analysis;
    - PLUGIN/vantage6 as a reference implementation of data stations for i) federated analysis, ii) federated learning and iii) data pooling.


## 1.3.2. Reading guide

This document is structured as follows. The **Process** section first describes the basic processes of secondary use, from data request to data use and publications, using the [Use Case 3.0](https://www.ivarjacobson.com/files/use-case_3.0_v1.0.pdf) modelling technique. The relevant concepts within the architecture of a data space are explained, in order to provide a clear picture of the context of a data station and the processing hub. Where necessary, reference is made to an [Archimate model of the data space](https://health-ri.github.io/data-spaces-archimate/). The **Information** chapter addresses semantic and syntactic interoperability as a prerequisite for the (re)use of health data. The **Application** section goes into greater detail on the various application components of a hybrid SPE, including the data station and processing hub _per se_. We follow the FAIR hourglass model as the definition of the layers. The specifications from TEHDAS2 are used as a starting point and further elaborated. The **Infrastructure** section then describes the physical technology and standards relevant to realising the application components.

Having explained the architecture from various perspectives, we turn in **Implementations** to existing implementations of data stations and federated processing hubs. By analysing in particular KIK-V and PLUGIN as reference implementations, we aim to critically reflect on the proposed specification of a data station for secondary use. Finally, **Discussion** sets out the key findings in relation to the research questions and makes suggestions for further development in the future.
