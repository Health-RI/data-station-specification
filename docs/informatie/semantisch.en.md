# 3.2. Semantic interoperability[^1]

## 3.2.1. The problem of semantic interoperability

Semantic interoperability goes beyond shared data formats or common terminologies — it requires that different systems interpret exchanged data in the same way. Achieving this depends on how well the ontology of each system captures the intended meaning of the concepts it uses. The following diagrams illustrate how systems can differ in their approach to a shared conceptualisation, and how these differences affect their ability to collaborate meaningfully.

![](https://health-ri.github.io/semantic-interoperability/semantic-interoperability/assets/images/semantic-interoperability-systems-all.png)

The diagram above illustrates how three different systems attempt to represent the same conceptualisation — i.e. a shared understanding of the real world — but with different levels of success. Each system uses a different ontology to constrain its internal model, leading to differences in how faithfully they capture the intended meaning.

- System A (left) represents an ideal case. Its ontology closely aligns with the intended semantics (green area), without adding unintended interpretations or excluding valid ones. This is described as a close approximation of the intended models — a highly desirable, though often difficult to achieve, situation for semantic interoperability.

- System B (middle) uses a more permissive ontology. The red dotted area shows unintended models that are logically consistent with System B's formalism but deviate from the intended meaning. Such over-generalisation can lead to **false agreement**: systems that appear interoperable because they use the same vocabulary but actually interpret the terms differently.

- System C (right) makes the opposite mistake. Its ontology is too restrictive: the blue striped area represents valid meanings it does not account for. This can happen when a system's constraints are too narrow or incomplete, leading to the exclusion of necessary interpretations and loss of information.

True semantic interoperability therefore requires more than syntactic or logical alignment. It requires a shared worldview — a convergence on what exists, how it can be described, and which interpretations are valid.


## 3.2.2. How is semantic interoperability achieved?

Achieving semantic interoperability involves several steps:

- **Standardised vocabularies and ontologies:** Using shared terminologies such as SNOMED CT, LOINC, or domain-specific ontologies to ensure consistent understanding of data elements.
- **Metadata and annotations:** Adding semantic layers to data using RDF, OWL or JSON-LD to provide context and meaning.
- **Mappings and alignments:** Creating links between different vocabularies or datasets to facilitate data integration and interoperability.
- **Tools and platforms:** Using interoperability frameworks, APIs and knowledge graphs to support seamless data exchange and understanding.
- **Ontologically grounded languages:** Using modelling languages that help to make the ontological assumptions embedded in data and systems explicit. As Guizzardi argues, it is not enough that representation languages are formally expressive — they must support users in articulating and verifying the actual semantics of their models through ontological commitments. OntoUML is one such language — explicitly grounded in the Unified Foundational Ontology (UFO) — that enables semantically rich, internally consistent and verifiable conceptual modelling.

[^1]: The text on this page is largely derived from the [Semantic Interoperability](https://health-ri.github.io/semantic-interoperability/semantic-interoperability) initiative of Health-RI. Where that initiative focuses on a thorough analysis and solution of the semantic interoperability problem, we take a more pragmatic approach for the data station specification.


## 3.2.3. Implications for data stations

- The HRI project focuses on ontological alignment.
- We take a more pragmatic approach, focusing on mappings between the most widely used thesauri and ontologies.
    - [SSSOM](https://github.com/mapping-commons/sssom) combined with [SEMAPV](https://github.com/mapping-commons/semantic-mapping-vocabulary) provides a basis for doing this in a standardised way.
    - Mappings already exist, for example for conditions and medication.
    - In scaling up data stations, we could collaborate in the Netherlands to make existing mappings available in SSSOM + SEMAPV:
        - DHD Diagnosis and Procedures Thesaurus
        - Z-Index mapping to RxNorm from ErasmusMC
        - Article by Cornet et al. from Z-index to ATC to RxNorm

- An alternative approach uses RDF and graph technology to integrate different datasets, similar to the Swiss SPHN [@gouthamchand2024makinga]. But is it not then easier to temporarily send data to a central SPE and have the user integrate it there?
- For specific domains such as radiomics, achieving semantic interoperability requires very specialised knowledge [@kalendralis2020faircompliant]. There too, it is more pragmatic to do this in a central SPE, until we have a better understanding of how the data (in this case radiology images) can best be made available generically.
