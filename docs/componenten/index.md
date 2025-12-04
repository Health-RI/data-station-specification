---
title: Architectuur in het vijf-lagen model
---

## Systeem actoren per laag

We positioneren systeem actoren uit de use-cases in de lagen.

| Laag | Systemen |
|:----:|:---------|
| 5 | - Gefedereerde analyse<br>- Gefedereerd leren<br>- Data pooling |
| 4 | - DAAMS<br>- Catalogus gezondheidsgegevens<br>- federated analytics portal |
| 3 | - data station |
| 2 | - data ontsluitingssysteem |
| 1 | - bronsystemen |



## Federated processing in decentrale netwerken

We volgen TEHDAS2 en maken onderscheid tussen:

- Gefedereerde analyse.
- Gefedereerd leren

We voegen daar een derde categorie aan toe, namelijk **data pooling**: vanuit een data station centraal ophalen.

Alle drie de toepassingen volgen een zogenaamde *hub-and-spoke* architectuur, dat wil zeggen dat er een centrale server is (waarop de eindgebruiker inlogt en als toegang tot de federatieve BVO gebruikt) van waaruit de federated processing wordt aangestuurd. Uitgaande van het definities van  centrale, decentrale en gedistributeerde netwerken [@baran1964distributed], kijken we dus naar een _decentraal_ systeem van federated processing:

Dit kent gelaagdheid van knooppunten, b.v. vanuit een regionaal knoopunt --> landelijk knooppunt --> international knooppunt

**Distributed federated** processing is expliciet niet in scope van deze architectuur.

![](../assets/type-of-networks.png)

///caption
Soorten netwerken: a) centraal, b) decentraal, c) distribueerd.
///

In dit hoofdstuk beschrijven we de functionele componenten per laag. Daarbij gaan we ook expliciet in op de verschillende [TEHDAS2 vereisten](../appendix/tehdas2-requirements.md) die zijn geformuleerd.