# 7.1. Centrale versus decentrale BVOs

Dit document geeft een beschrijving van een decentrale BVO, met het [datastation](../applicatie/laag-3/data-station.md) en de [processing hub](../applicatie/laag-4/processing-hub.md) als de meest kenmerkende componenten. Zoals eerder gesteld is de EHDS onvoldoende expliciet over de nut en noodzaak van decentrale architecturen, wat de aanleiding was voor een van de onderzoeksvragen:

> Op welke manier kunnen hybride BVOs, zijnde een synergie tussen centrale en decentrale BVOs, gerealiseerd worden en welke mogelijkheden zijn er om hierin tot standaardisatie te komen?

In het onderstaande wordt ingegaan op deze vraag.

## 7.1.1. De nut en noodzaak van een hybride oplossing

In dit document hebben we beargumenteerd dat een decentrale oplossing voordelen biedt op het gebied van security, privacy en data governance. Tegelijkertijd realiseren wij ons dat er usecases zullen zijn waarbij decentrale processing niet mogelijk is. Denk hierbij aan verticaal gepartitioneerde data of het doorleveren van gegevens aan een landelijke kwaliteitsregistratie.

Wij stellen daarom voor een hybride oplossing waarbij federated processing ingezet kan worden wanneer de usecase het toelaat en daarnaast de datastations data kunnen doorzetten naar een centrale BVO.

## 7.1.2. Formele status van een datastation als decentrale BVO

De EHDS verplicht dat secundair gebruik van gezondheidsdata plaatsvindt binnen een BVO. Gegeven de rol en functionaliteit van een datastation, gaan wij er vanuit dat een datastation formeel onder de definitie van een BVO valt. Het is echter nog onduidelijk hoe de certificering van decentrale BVOs, zijnde de datastations zoals in dit document zijn beschreven, eruit zou kunnen zien. De benadering van de EHDS leunt sterk op regie door een HDAB. Als de HDAB enkel centrale BVOs erkent of faciliteert, vormt dit een directe tegenstrijdigheid met de decentrale opzet voor datastations secundair gebruik, waar data bij de bronhouder blijft.

Om dit punt te adresseren zou een (inter)nationaal certificeringskader komen waarbij de BVOs die gekoppeld zijn aan (of onderdeel zijn van) een decentrale federerated processing infrastructuur worden erkend als een valide EHDS-verwerkingsomgeving.


## 7.1.3. Geautomatiseerde controle van vergunningen en gegevensverzoeken 

De grondslag voor secundair gebruik in de EHDS is gebaseerd op een vergunning of een gegevensverzoek. De HDAB is verantwoordelijk voor de uitgifte van de attestatie dat een datagebruiker beide vormen van secundair gebruik.

In het geval dat een centrale BVO wordt gebruikt om uitvoering te geven aan de vergunning of gegevensverzoek, zullen de autorisatie mechanismen ook in het centrale systeem geimplementeerd moeten worden. Dit zou bijvoorbeeld kunnen met een persoonsgebonden credential waarmee de gebruiker toegang krijgt tot de BVO.

Het autorisatiemechanisme is voor een decentrale BVO complexer: er zal een mechanisme moeten worden geimplementeerd waarbij het datastation kan verifieren of een bepaald algoritme daadwerklijk uitgevoerd mag worden. Binnen KIK-V wordt het NUTS framework gebruikt om de vertrouwensrelaties digitaal vast te leggen binnen het netwerk. Deze oplossingsrichting is generaliseerbaar op termijn dit te combineren met de eIDAS business wallet.

Kijkend naar PLUGIN en het onderliggende vantage6 framework zien wij dat een dergelijk _trust_ mechanisme nog niet is geimplementeerd. Het belagnrijkste autorisatiemechanisme loopt via de container registry waar goedgekeurde algoritmes in zijn opgeslagen. In het geval van federated processing, met een vergunning als grondslag, zal er dus nog een _trust_ mechanisme geimplementeerd moeten worden waarbij de DAAMS het bronsysteem is dat de (digitale) certificaten uitgeeft. Het concept van _smart contracts_ zou hier een technische oplossing voor kunnen bieden.[@short2021execution] Alhoewel dergelijke oplossingen technisch bewezen zijn, is er nog geen uniforme standaard noch is de technologie voldoende volwassen voor grootschalig gebruik.

## 7.1.4. Specificatie van _data visting_ standaarden

De benadering van federated processing conform het principe van _data visiting_ is essentieel om op grote schaal gebruik te kunnen maken van decentrale BVOs. Op dit moment zijn hiervoor verschillende technische oplossingen die nog onvoldoende op elkaar aansluiten. Dit is een van de centrale vragen binnen het [Health-AI project](https://www.clinicaldatascience.nl/health-ai). Afhankelijk van de uitkomsten van dit project - en andere vergelijkbare initiatieven, zullen meer gedetailleerde specificaties en standaarden voor federated processing moeten worden opgesteld.
