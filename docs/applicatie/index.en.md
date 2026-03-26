# Perspective: application
## Application components for data operations in layered, decentralised networks

This document focuses on the elaboration of a hybrid SPE based on the principles of data visiting. The proposed architecture has many similarities with what TEHDAS2 calls a federated SPE (_federated SPE_). The EHDS is essentially designed in a federated way: we ultimately want to be able to use health data from across Europe for secondary use. At the same time, we want health data to be copied as little as possible, because this compromises control over and security of the data. Being able to perform computations at the location of the data is therefore an important functional requirement. To make this possible, **at minimum an architecture is needed for decentralised data processing between countries**. This architecture provides for national nodes that can jointly perform analyses, under the coordination of a central node at European level. This approach is elaborated in [TEHDAS2 M7.4](../appendix/tehdas2-spe.md) chapter 5 (_SPE federation_ p. 42) and chapter 6 (_Implementing federated computing_ p. 50). In this document we apply the same design principles to enable **a network of data stations for decentralised information processing within a country**.

Decentralised data processing is based on a network of data stations that are interconnected. The way in which these data stations are connected (the so-called network topology) is decisive for the architecture of the federated SPE. We broadly distinguish three network topologies[@baran1964distributed]: centralised, decentralised and distributed.

![](../assets/type-of-networks.png)

///caption
Types of networks: a) centralised, b) decentralised, c) distributed.
///

Federated SPEs have two archetypes:[@rieke2020future]

1. Data stations are connected to a single central server, in other words a federated SPE with a centralised network (also known as a _hub-and-spoke_ network).
2. Data stations are interconnected via a distributed network (also known as _peer-to-peer_).


![](../assets/fl-types.png)

///caption
Federated data processing with a) a central aggregation server, and b) a _peer-to-peer_ network.
///

The most commonly used form of federated data processing is based on a central server that coordinates the data stations. The concept of a _Federated Database System (FDBS)_ was described in 1985 and has been used for years to perform federated analysis (_queries_) across multiple databases.[@heimbigner1985federated] The concept of federated learning as introduced by Google in 2017[@mcmahan2017communication] also uses a central server.

In the description of data stations, we therefore assume a central server on which the data user logs in to gain submit computing jobs to the network of data stations. Federated SPEs with a _peer-to-peer_ network are explicitly out of scope for the architecture described here.

In addition, in the context of the EHDS it must be possible to work with _federations of federations_. The hybdrid SPE we have in mind has a layered structure of nodes. Think, for example, of a healthcare institution participating in a regional collaboration, with different regional nodes then forming part of a national federated network. On top of that, national nodes may form part of a European federation. In the elaboration of the architecture, we therefore assume a _decentralised network_ that has a layered structure of multiple networks of SPEs (network type b in the illustration above).

## The components of a decentralised network of SPEs

In the elaboration of the architecture for a decentralised network of SPEs, **the data station** and the **processing hub** are central. These two application components together realise the functionality needed in a decentralised SPE. In relation to the [FAIR hourglass model](../data-stations-als-hoeksteen.md), the data station is part of layer 3, while the processing hub is part of layer 4. Conceptually, we place the different forms of federated data processing in layer 5. Building on TEHDAS2, we distinguish between three (arche)types:

1. **Federated analysis**: statistics are computed locally in a network of data stations. Only aggregated results or summary statistics are exported from the data stations, with corresponding safeguards to ensure that no personal data is extracted. Federated analysis is in principle the same as a _Federated Database System_. Federated analysis is particularly suitable for executing data requests in the sense of [EHDS article 69](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327&qid=1764922416982#art_69). We regard [KIK-V](../implementaties/KIK-V/index.md) as a reference implementation for federated analysis.
2. **Federated learning**: models are trained and validated on the data stations without sharing the raw data between the data stations. Instead, only the model updates are shared with the processing hub to achieve better data privacy and security. We regard [PLUGIN](../implementaties/PLUGIN/index.md) as a reference implementation for federated learning.
3. **Data pooling**: the data stations can be used to (temporarily) send data to another SPE or an authorised system, which is also known as data exchange. The [EOSC-ENTRUST Blueprint](https://zenodo.org/records/14362388) provides a detailed architecture of how data stations can integrate with such _Trusted Research Environments_. The data pooling mechanism can also be used to deliver data to quality registries. Strictly speaking, data pooling is not a form of federated processing, but more of a hybrid SPE. Because there are so many overlaps and possible applications, it has been included in the scope of this document. It is also one of the reason why we prefer to speak of a hybrid archtiecture/SPE instead of a pure federated SPE.

In this chapter we describe the application components of a hybrid SPE, namely the three types of applications in layer 5, the Processing Hub and the data station. We also explicitly address the various [TEHDAS2 requirements](../appendix/tehdas2-requirements.md) that have been formulated. For the other, more generic components, we follow the description in TEHDAS2 and conduct a shorter _fit-gap_ analysis of the extent to which these components fit within a hybrid SPE. The table below provides an overview of the key application components within the FAIR hourglass five-layer model.

| Layer | Systems |
|:----:|:---------|
| **5** | **> [Federated analysis](./federatieve-analyse.md)**<br>**> [Federated learning](./federatief-leren.md)**<br>**> [Data pooling](./data-pooling.md)** |
| **4** | > [Data Access Application Management System](./daams.md)<br>> [Health data catalogue](./catalogus.md)<br>**> [Processing hub](./processing-hub.md)** |
| **3** | **> [Data station](./data-station.md)** |
| **2** | > Data exposure system |
| **1** | > Source systems |

///caption
Overview of core components in the architecture of a federated SPE. The components that are central to this architecture are in bold.
///


