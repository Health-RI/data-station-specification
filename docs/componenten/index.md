---
title: Architectuur componenten
---

## Gefedereerde gegevensverwerking in gelaagde, decentrale netwerken

Dit document richt zich op de uitwerking van wat in TEHDAS2 een **federatieve BVO** wordt genoemd (_federated SPE_). De EHDS is in essentie federatief ontworpen: we willen uiteindelijk gezondheidsgegevens uit heel Europa kunnen aanwenden voor secundair gebruik. Tegelijkertijd willen we dat gezondheidsgegevens zoveel mogelijk binnen de landsgrenzen blijven. Om dit mogelijk te maken is **ten minste een architectuur nodig voor gefedereerde gegevensverwerking tussen landen**. Hierin is voorzien dat landelijke knooppunten gezamenlijk analyses kunnen uitvoeren, onder regie van een centraal knooppunt op Europees niveau. Deze aanpak is uitgewerkt in [TEHDAS2 M7.4](../appendix/tehdas2-spe.md) hoofdstuk 5 (_SPE federation_ p. 42) en hoofdstuk 6 (_Implementing federated computing_ p. 50). In dit document passen wij dezelfde ontwerpprincipes toe om **binnen een land een LDN voor decentrale, gefedereerde gegevensverwerking** mogelijk te maken.

Gefedereerde gegevensverwerking gaat uit van een netwerk van data stations die met elkaar verbonden zijn. De manier waarop deze data stations zijn verbonden (de zogenaamde netwerk topologie) is bepalend voor de architectuur van de federatieve BVO. We kennen grofweg drie netwerk topologieën[@baran1964distributed]: centraal, decentraal en gedistribueerd.

![](../assets/type-of-networks.png)

///caption
Soorten netwerken: a) centraal, b) decentraal, c) distribueerd.
///

Gefedereerd gegevensverwerking kan met een centraal netwerk (ook wel een _hub-and-spoke netwerk_ genoemd) of met een distribueerd netwerk (ook wel _peer-to-peer_ genoemd).[@rieke2020future]


![](../assets/fl-types.png)

///caption
Gefedereerde gegevensverwerking met een a) centrale aggregatie server, en b) _peer-to-peer_ netwerk.
///

De meest gebruikte vorm van gefedereerde gegevensverwerking gaat uit van een centrale server die de data stations aanstuurd. Het concept een _Federated Database System (FDBS)_ is 1985 beschreven en wordt al jaren gebruikt voor het uitvoeren van gefedereerde queries over meerdere databases.[@heimbigner1985federated] Het concept van gefedereerd leren zoals in 2017 door Google is geintroduceerd[@mcmahan2017communication] maakt ook gebruik van een centrale server.

In de beschrijving van data stations gaan we dus uit van een centrale server, waarop de data gebruiker inlogt om toegang te krijgen tot de federatieve BVO gebruikt. Federatieve BVOs met een _peer-to-peer_ netwerk zijn expliciet niet in scope van de architectuur zoals hier beschreven is.

Daarmaast moet het de context van de EHDS mogelijk zijn om te werken met _federations of federations_. De federatieve BVO die we voor ogen hebben kent een gelaagdheid van knooppunten. Denk bijvoorbeeld aan een zorginstelling die participeert in een regionale federatieve BVO, waarbij vervolgens verschillende regionale knooppunten opgaan in een landelijke federatief netwerk. Daarbovenop kunnen landelijke knooppunten onderdeel uitmaken van een Europese federatie. In de uitwerking van de architectuur gaan we daarom uit van een _decentraal netwerk_ dat een gelaagdheid kent van meerdere federatieve BVOs.

## De componenten van een federatieve BVO

In de uitwerking van de architectuur voor een federatieve BVO staan **het data station** en de **federated processing hub (FPH)** centraal. Deze twee componenten realiseren gezamenlijk de functionaliteit die nodig is in een federatieve BVO. In relatie tot het FAIR zandloper model, is het data station onderdeel van laag 3, terwijl de FPH onderdeel is van laag 4. Onderstaand tabel geeft aan hoe het geheel van componenten is geplaatst in het vijf-lagen model.

Conceptueel plaatsen we de verschillende vormen van gefedereerde gegevensbewerking in laag 5. Voortbouwend op TEHDAS2 maken we onderscheid tussen drie (arche)typen:

1. **Gefedereerde analyse**: statistieken worden lokaal berekend in een netwerk van data stations. Alleen geaggregeerde resultaten of samenvattende statistieken worden uit de data stations geexporteerd, met bijbehorende waarborgen dat geen persoonsgegevens worden onttrokken. Gefedereerde analyse is in principe hetzelfde als een _Federated Database System_. Gefedereerde analyse is bij uitstek geschikt om gegevensverzoeken in de zin van [EHDS artikel 69](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=OJ:L_202500327&qid=1764922416982#art_69) uit te voeren. [KIK-V](../implementaties/KIK-V/index.md) zien wij als een referentie implementatie voor gefedereerde analyse.
2. **Gefedereerd leren**: modellen worden getraind en gevalideerd op de data stations zonder dat de ruwe data wordt gedeeld tussen data station. In plaats daarvan worden alleen de model updates gedeeld met de FPH om daarmee betere data privacy en beveiliging te bereiken. [PLUGIN](../implementaties/PLUGIN/index.md) zien wij als een referentie implementatie voor gefedereerd leren.
3. **Data pooling**: de data stations kunnen worden gebruikt om data (tijdelijk) naar een andere SPE of daartoe bevoegd systeem te sturen. De [EOSC-ENTRUST Blueprint](https://zenodo.org/records/14362388) geeft een detaileerde architectuctuur hoe data stations kunnen integreren met _Trusted Research Environment_. Het mechanisme van data pooling kan ook gebruikt worden om in data aan te leveren naar kwaliteitsregistraties.

In dit hoofdstuk beschrijven we de componenten van een federatieve BVO, zijnde de driee soorten toepassingen in laag 5, de Federated Processing Hub en het data station. Daarbij gaan we ook expliciet in op de verschillende [TEHDAS2 vereisten](../appendix/tehdas2-requirements.md) die zijn geformuleerd. Voor de andere, meer generieke componenten, gaan we uit van de beschrijving in TEHDAS2 en voeren we een kortere _fit-gap_ analyse uit in hoeverre deze componenten passen in een federatieve BVO. Onderstaand tabel geeft een overzicht van alle componenten binnen het FAIR zandloper vijf-lagen model.

| Laag | Systemen |
|:----:|:---------|
| **5** | **> [Gefedereerde analyse](./laag-5/federatieve-analyse.md)**<br>**> [Gefedereerd leren](./laag-5/federatief-leren.md)**<br>**> [Data pooling](./laag-5/data-pooling.md)** |
| **4** | > [Data Access Application Mgnt System](./laag-4/daams.md)<br>> [Catalogus gezondheidsgegevens](./laag-4/catalogus.md)<br>**> [Federated processing hub](./laag-4/fph.md)** |
| **3** | **> [Data station](./laag-3/data-station.md)** |
| **2** | > Data ontsluitingssysteem |
| **1** | > bronsystemen |

///caption
Overzicht van kerncomponenten in de architectuur van een federatieve BVO. De componenten die in deze architectuur centraal staan zijn vetgedrukt.
///



