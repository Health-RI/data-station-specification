---
title: Discussion
---

# 7. Discussion

This chapter addresses the two central research questions of this specification document:

> Can a clear functional and technical specification be given of a hybrid SPE based on data stations and a processing hub, consistent with existing reference architectures?

> In what way could data stations be standardised to achieve maximum interoperability of hybrid SPEs?

The preceding chapters have shown that a data station is not a standalone system, but a cornerstone of a broader infrastructure for secondary use. The discussion focuses on four interconnected themes that require further elaboration.

**Central versus decentralised** (§7.1) shows that a hybrid architecture is the most viable solution: federated processing where the use case permits, combined with the ability to forward data to a central SPE. However, the formal status of a data station as a decentralised SPE under the EHDS is still insufficiently elaborated, and a certified _trust_ mechanism for automated permit verification in a federated network is yet to be established.

**Primary versus secondary use** (§7.2) demonstrates that the similarities between data stations for primary and secondary use are substantial — comparable design principles, ownership within the data holder's domain, support for multiple information models — but that the legal bases for access control, required latency, and the need for local compute capacity differ fundamentally. The adapter function capable of serving both clinical FHIR data and analytical formats from the same abstracted data layer is a critical building block in this regard.

**Health data permits versus requests** (§7.3) describes how the EHDS distinguishes between permits and requests, with the HDAB as the central issuing authority. For a decentralised network of data stations, this means that the authorisation mechanism must be able to translate the HDAB's digital permit into local access rights — a technical challenge for which no universal standard yet exists. The role of _trusted data holders_ offers perspective here: organisations such as DHD, Zorginstituut, IKNL and Vektis can act as trusted intermediaries.

**Relation to dataspace initiatives** (§7.4) shows that EHDS and generic data spaces (IDSA, Eclipse Dataspace, Gaia-X) share architectural principles — federation, data sovereignty, metadata-driven design — but diverge on crucial points: the EHDS authorisation model is centralised and legally binding, while generic data spaces rely on peer-to-peer negotiation. Full interoperability is unlikely; convergence at the layers of metadata standards (DCAT/HealthDCAT-AP), identity and authentication (eIDAS, Digital Identity Wallets) and generic source system interfaces offers the most realistic path forward.

**Proposed development agenda** (§7.5) consolidates the main outstanding items: output control for deep learning models, _smart contracts_ as an additional safeguard for automated permit verification, and the extension of data stations with medical imaging provisions (PACS, DICOM service, compute service).

The overarching conclusion is that unity of technology is already largely achievable — the main TEHDAS2 requirements are already realised in KIK-V and PLUGIN — but that unity of language (semantic interoperability) will take longer. The composable data stack provides the most pragmatic foundation for this: standardised support for data transformations, with existing and new mappings in SSSOM + SEMAPV as building blocks for increasing semantic exchangeability.
