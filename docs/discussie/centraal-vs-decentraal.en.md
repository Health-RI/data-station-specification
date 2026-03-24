# 7.1. Central versus decentralised SPEs

This document provides a description of a decentralised SPE, with the [data station](../applicatie/data-station.md) and the [processing hub](../applicatie/processing-hub.md) as the most characteristic components. As stated earlier, the EHDS is insufficiently explicit about the utility and necessity of decentralised architectures, which gave rise to one of the research questions:

> In what way can hybrid SPEs — being a synergy between central and decentralised SPEs — be realised, and what options are there to achieve standardisation in this regard?

The following addresses this question.

## 7.1.1. The utility and necessity of a hybrid solution

In this document we have argued that a decentralised solution offers advantages in the areas of security, privacy and data governance. At the same time, we recognise that there will be use cases in which decentralised processing is not possible. Examples include vertically partitioned data or the forwarding of data to a national quality registry.

We therefore propose a hybrid solution in which federated processing can be deployed when the use case allows, while data stations can also push data to a central SPE.

## 7.1.2. Formal status of a data station as a decentralised SPE

The EHDS requires that secondary use of health data takes place within an SPE. Given the role and functionality of a data station, we assume that a data station formally falls under the definition of an SPE. However, it remains unclear what certification of decentralised SPEs — being the data stations as described in this document — would look like. The EHDS approach relies heavily on oversight by an HDAB. If the HDAB only recognises or facilitates central SPEs, this creates a direct contradiction with the decentralised setup for secondary use of data stations, where data remains with the source holder.

To address this point, an (inter)national certification framework would be needed in which SPEs connected to (or forming part of) a decentralised federated processing infrastructure are recognised as a valid EHDS processing environment.


## 7.1.3. Automated verification of permits and data requests

The legal basis for secondary use in the EHDS is based on a permit or a data request. The HDAB is responsible for issuing the attestation that a data user holds either form of secondary use authorisation.

In the case where a central SPE is used to execute the permit or data request, the authorisation mechanisms will also need to be implemented in the central system. This could, for example, take the form of a personal credential granting the user access to the SPE.

The authorisation mechanism is more complex for a decentralised SPE: a mechanism must be implemented by which the data station can verify whether a given algorithm is actually permitted to be executed. Within KIK-V, the NUTS framework is used to digitally record trust relationships within the network. This solution direction is generalisable and could in time be combined with the eIDAS business wallet.

Looking at PLUGIN and the underlying vantage6 framework, we observe that such a _trust_ mechanism has not yet been implemented. The primary authorisation mechanism runs via the container registry where approved algorithms are stored. In the case of federated processing with a permit as the legal basis, a _trust_ mechanism must therefore still be implemented whereby the DAAMS is the source system issuing the (digital) certificates. The concept of _smart contracts_ could provide a technical solution here.[@short2021execution] Although such solutions are technically proven, there is as yet no uniform standard, nor is the technology sufficiently mature for large-scale use.

## 7.1.4. Specification of _data visiting_ standards

The approach of federated processing in accordance with the principle of _data visiting_ is essential for large-scale use of decentralised SPEs. At present, various technical solutions exist for this that are insufficiently compatible with one another. This is one of the central questions within the [Health-AI project](https://www.clinicaldatascience.nl/health-ai). Depending on the outcomes of this project — and other comparable initiatives — more detailed specifications and standards for federated processing will need to be established.
