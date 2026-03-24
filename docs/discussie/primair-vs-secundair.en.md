# 7.2. Data stations for primary vs. secondary use

This document provides a description of a decentralised SPE, with the [data station](../applicatie/data-station.md) and the [processing hub](../applicatie/processing-hub.md) as the most characteristic components. In comparison with the Cumuluz target architecture, we see comparable roles for the Cumuluz Data Station and the Cumuluz Integrator respectively. As stated in the introduction, a comparison of the architecture for primary vs. secondary use is one of the central research questions:

> Are there gaps or contradictions in the current EHDS approach to secondary use that obstruct the use of decentralised SPEs, particularly also in relation to data stations for primary use? If so, what solution directions exist?

The following addresses these questions.

## 7.2.1. Difference in legal basis for authorised access

When we compare the Cumuluz target architecture with this document, we see that both architectures strive for a "register once, use multiple times" approach. However, there is an essential difference in the legal basis:

- **Primary use:** based on the treatment relationship and patient consent.
- **Secondary use:** based on a permit issued by an HDAB.

In the design of a Cumuluz Data Station, it is clearly specified how access to the data station is granted via a central consent facility (MITZ).

In the case of secondary use, there are two aspects relevant to authorised access. The first aspect concerns opt-out: when preparing data for a data user (with a permit), it is the data holder's responsibility to exclude data subjects who have invoked their opt-out right. To this end, the data holder can use MITZ as a central consent facility in which an up-to-date status is available of persons who have opted out. The second aspect is the authorisation mechanism itself: which calculations may be executed on the data stations. The current state of the art in federated processing includes various authorisation mechanisms. These differ, however, from implementation to implementation and there is as yet no universal standard. It is conceptually possible to work in time with _verifiable credentials_ linked to the permit issued by the HDAB/DAAMS, but no working implementations of this exist yet.

## 7.2.2. Comparison of primary and secondary data station

???+ success "Similarities between primary and secondary data stations"
    | ID    | Description |
    |:-----:|:------------|
    | DS-O1 | Comparable, if not identical, design principles and non-functional requirements. |
    | DS-02 | A data station falls within the domain of the data holder. |
    | DS-O3 | A data station assumes conformance, whereby multiple information models are supported including functionality to perform transformations between these models. |
         
???+ warning "Differences between primary and secondary data stations"
    | ID    | Description |
    |:------:|:------------|
    | DS-V1 | Primary use focuses exclusively on clinical data. Secondary use also encompasses operational and logistical data. |
    | DS-V2 | Localisation of data in the primary process is based on unique identifiers for persons, while in the secondary process the data catalogue is used. |
    | DS-V3 | Access control at a data station is performed at the individual level. At a secondary data station, access control is configured at the level of the calculation being performed. |
    | DS-V4 | Primary use is optimised for fast (_latency_ less than 1 second) querying of data for a single person, while secondary use assumes bulk querying with a greater latency. |
    | DS-V5 | Storage of data is optional at a primary data station; at a secondary data station it is a requirement to support _data visiting_. |
    | DS-V6 | A primary data station has no provision for executing calculations locally. For a secondary data station, this is a requirement to support _data visiting_. |

## Comparison of Integrator (primary) and Processing Hub (secondary)

???+ success "Similarities of the central integration component in layer 4"
    | ID    | Description |
    |:-----:|:------------|
    | L4-O1 | Comparable, if not identical, design principles and non-functional requirements. |
    | L4-O2 | Data users (systems or persons) gain access to data via a single central entry point; a _hub-and-spoke_ network topology is used. |
    | L4-03 | Configuration of layer 4 is based on the [_four corner model_](https://health-ri.github.io/data-spaces-archimate/?view=id-65fda4e829df4a489df5644ffbbdb0e6): multiple service providers are anticipated in the national network. |

???+ warning "Differences in the central integration component in layer 4"
    | ID    | Description |
    |:-----:|:------------|
    | L4-V1 | The legal basis and role of the data user in the primary process differs for primary (treatment relationship) and secondary use (permit or data request). |
    | L4-V2 | The Processing Hub fulfils an important function for output control / _statistical disclosure control_. This is not applicable in primary use. |

The tables above give an overview of the differences and similarities between data stations for primary and secondary use, as well as for the central integration component in layer 4.


### Harmonised API for Permits and Authorisation
The National Agreement Framework (LAS) should be extended with a specific "EHDS connector". This API should enable a decentralised Data Station to directly translate a digital permit from the HDAB into local access rights in the SPE, comparable to how the Generic Authorisation Function works for primary use.


* **Dual-purpose Adapter Functions:**
The "Adapter" role in the CumuluZ architecture should be developed into a dual-purpose component capable of serving both FHIR (primary) and analytical formats (secondary) from the same abstracted data layer. This ensures that data integrity between patient care and research is maintained.


* **Unambiguous Governance on Data Access Committees (DAC):**
The process for granting access should be streamlined, with the local DAC of a hospital and the national HDAB collaborating via a federated model. This prevents duplicate administrative burdens and ensures that the source holder retains control, in line with architecture principle C2.


## Parking lot

- [EHRxF FHIR profile](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/)
