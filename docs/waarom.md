# 1.1. Waarom dit specificatie document

## 1.1.1. Te weinig aandacht voor federatieve oplossingen en het concept van _data visiting_
Ten tijde van het schrijven van dit document zijn een aantal belangrijke richtlijnen in de maak betreffende de uitwerking en implementatie van de EHDS voor secundair gebruik, met name:

- [TEHDAS2](https://tehdas.eu/public-consultations/): gedetailleerde richtlijnen en technische specificiaties in 11 documenten.[^1]
- [Data Spaces Support Center Blueprint](https://dssc.eu/space/BVE2/1071251457/Data+Spaces+Blueprint+v2.0+-+Home): industrie-overstijgende richtlijnen voor inrichting van data spaces.
- [Uitgangspunten LDN](https://open.overheid.nl/documenten/52acfd51-3585-416d-979b-ab6deaba79d9/file): brede uitgangspunten geformuleerd door VWS, waaronder _privacy-by-design_, hoge mate van open source werken en opslag van data bij de bron.

Deze ontwikkelingen geven een steeds duidelijker beeld van hoe een landelijke gezondheidsdata-infrastructuur voor onderzoek, beleid en innovatie eruit zou kunnen c.q. moeten zien. Tegelijkertijd constateren we een lacune ten aanzien van het hanteren van principes als _privacy-by-design_ en _data visiting_. In de inleiding van de EHDS wordt in overweging 80 gesteld dat:

> _Gezien de gevoeligheid van gezondheidsgegevens moeten waar mogelijk beginselen als “privacy door ontwerp” en “privacy door standaardinstellingen” en het concept “breng de vragen naar de gegevens in plaats van die gegevens te verplaatsen” in acht worden genomen._

Het concept van _data visiting_, ook wel bekend als _federated computing_ of _Personal Health Train_ (PHT), wordt nergens in de EHDS nader toegelicht[^2]. TEHDAS2 [_M7.4 Draft technical, functional and security specifications of Secure Processing Environments_](./appendix/tehdas2-spe.md) (hoofdstuk 6) gaat hier op in en maakt een aanzet voor de definitie van federated computing.

???+ abstract "Definities federated computing in TEHDAS2"
    
    === "**Gefedereerde berekening<br>(_federated computing_)**"
        Gedecentraliseerde berekening van data waarbij de berekeningen op lokale, gedistribueerde BVOs worden uitgevoerd in plaats van centrale verwerking in één BVO. Een dergelijke aanpak wordt aanbevolen in overweging 80 ten behoeve van _privacy preserving computation_. Gefedereerde berekening maakt het mogelijk om de data dichter bij hun originele locatie te houden waarbij alleen geaggregeerde resultaten of model parameters worden gedeeld, en daarmee privacy en veiligheid verhogen.
    
    === "**Gefedereerde analyse<br>(_federated analysis_)**" 
        Een specifieke vorm van gefedereerde verwerking waarbij statistieken lokaal worden berekend op verschillende, gedistrueerde BVOs. Deze methode is geschikt voor o.a. vergelijkende analyses, multi-centra onderzoek en andere vormen van collaboratieve statistische analyse. Alleen geaggregeerde resultaten of samenvattende statistieken worden uit de lokale BVOs geexporteerd, met bijbehorende waarborgen dat geen persoonsgegevens uit de BVO worden onttrokken.

    === "**Gefedereerd leren<br>(_federated learning_)**"
        Een specifieke vorm van gefedereerde berekening waarbij modellen worden getraind en gevalideerd op gedistribueerde BVOs. De ruwe data wordt niet gedeeld tussen de BVOs. In plaats daarvan worden alleen de model updates gedeeld om daarmee betere data privacy en beveiliging te bereiken. Omdat het moeilijk is om de anonimiteit van tussentijdse resultaten te beoordelen, is het essentieel dat gefedereerd leren gebeurd in een vertrouwd netwerk van BVOs.

    TEHDAS2 maakt onderscheid tussen twee scenarios, namelijk gefedereerde analyse (a) en gefedereerd leren (b).

    ![](federation-scenarios.png)


## 1.1.2. Een specificatie van een decentraal netwerk van BVOs
Centrale BVOs, zoals bijvoorbeeld de CBS Microdata omgeving of de _Trusted Research Environments_ zoals in [EOSC-ENTRUST](https://eosc-entrust.eu/) verband worden geïmplementeerd, zijn op dit moment de meest gangbare vorm van BVOs. Dit document beschrijft een architectuur van een **decentraal netwerk van BVOs**[^3] dat verschillende vormen van federated computing (federated learning en federated analytics) ondersteund als ook gegevens aanlevering naar een centrale TRE (data pooling). Datastations zijn een essentieel onderdeel en fungeren als hoeksteen voor dit decentrale netwerk van BVOs. Wij denken dat een dergelijk decentraal netwerk een belangrijke bijdrage kan leveren aan het effectief, efficiënt èn veilig implementeren van de EHDS en zien deze als een aanvulling op c.q. alternatief voor centrale BVOs. 

[^1]: Deze gedetailleerde functionele en techniscke specificaties van health data spaces c.q. BVOs zijn nog in consultatie-fase en moeten nog door de Europese Commissie vastgesteld. Voor primair gebruik is dit uiterlijk maart 2027, voor secundair gebruik (de scope van TEHDAS2) maart 2029.
[^2]: Het woord _federated_ komt slecht twee keer voor in de EHDS verordening.
[^3]: In TEHDAS2 wordt dit een federatieve BVO wordt genoemd. Wij gebruiken liever de termen centraal, decentraal en hybride, wat in de inleiding van het [Applicatie](./applicatie/index.md) nader wordt toegelicht.