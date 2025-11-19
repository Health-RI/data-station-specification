# Inleiding

## Op weg naar de EHDS
Op 26 maart 2025 is de verordening betreffende de European Health Data Space (EHDS) in werking getreden. De belangrijkste mijlpalen op weg naar de volledige uitvoering zijn:

- **maart 2027**: vaststelling landelijke uitvoeringswetten met gedetailleerde regels en praktische uitwerking van de verordening, inclusief de benoeming van de nationale Health Data Access Body (HDAB) als orgaan voor toezicht op en mogelijk maken van secundair gebruik.
- **maart 2029**: de verordening zal van toepassing zijn voor de eerste prioritaire categorieen van gezondheidsgegevens (patientendossiers, electronische recepten en aflevering) in alle EU landen voor primair gebruik. De HDAB is operationeel en secundair gebruik is mogelijk voor de meeste gegevenscategorieën.
- **maart 2031**: de tweede groep prioritaire categorieën gezondheidsgegevens (medische beelden, laboresultaten en verslagen ziekenhuisontslag) is beschikbaar voor primair gebruik. De regels voor secundair gebruik worden ook van toepassing voor de overige gegevenscategorieën (bv. genomische gegevens).
- **maart 2035**: derde landen en internationale organisaties kunnen zich aansluiten bij HealthData@EU voor het secundaire gebruik.

Dit document richt zich op de uitwerking een de EHDS specifiek voor secundair gebruik, zoals hieronder is weergegeven.

![](ehds-simpel.png)

???+ abstract "De belangrijkste concepten rondom secundair gebruik"
    De belangrijkste concepten rondom secundair gebruik zijn gedefinieerd in de nieuwe Europease wetgeving, met name de EHDS (hoofdstuk IV, artikel 50 t/m 81) en de Data Governance Act (DGA).

    === "**Beveiligde verwerkingsomgeving (BVO)**"
        Een beveiligde omgeving waarin gezondheidsgegevens verwerkt kunnen worden voor bijvoorbeeld wetenschappelijk onderzoek. Dit kan een centrale BVO zijn, zoals bijvoorbeeld de [CBS Microdata omgeving](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen), een gefedereerde BVO of een hybride combinatie daarvan. Dit focus van deze specificatie is dat data stations als hoeksteen kunnen fungeren voor een netwerk van BVOs.
    
    === "**Data gebruiker**" 
        Een persoon of organisatie die toegang heeft gekregen tot elektronische gezondheidsgegevens voor secundair gebruik. Bijvoorbeeld een onderzoeker, een beleidsmederwerker of een ontwikkelaar van commerciële producten.

    === "**Data houder**"
        Een data houder is een persoon of organisatie (publiek of privaat) die gezondheidsdata beheert. Veel organisaties vallen hieronder. Het gaat niet alleen om ziekenhuizen, maar bijvoorbeeld ook iedereen die producten of diensten ontwikkelt die bestemd zijn voor de zorgsector of gezondheidszorg, of ontwikkelaars van wellnessapps, of wetenschappelijk onderzoekers die zich bezighouden met de zorgsector of gezondheidszorg.

    === "**Secundair gebruik**"
        Het gebruik van elektronische gezondheidsgegevens voor andere doeleinden dan die waarvoor ze verzameld zijn. Het gebruiken van gezondheidsgegevens, die zijn vastgelegd voor de behandeling van een patiënt, voor wetenschappelijk onderzoek, is een voorbeeld van secundair gebruik.

## Waarom dit specificatie document

Ten tijde van het schrijven van dit document zijn een aantal belangrijke richtlijnen in wording ten aanzien van de uitwerking en implementatie van EHDS voor secundair gebruik, met name:

- [TEHDAS2](https://tehdas.eu/public-consultations/): gedetailleerde richtlijnen en technische specificiaties in 11 documenten
- [Data Spaces Support Centre Blueprint](https://dssc.eu/space/BVE2/1071251457/Data+Spaces+Blueprint+v2.0+-+Home): industrie-overstijgende richtlijnen voor inrichting van data spaces.

Deze ontwikkelingen geven een steeds duidelijker beeld hoe een landelijke gezondheidsdata-infrastructuur voor onderzoek, beleid en innovatie eruit zou kunnen c.q. moeten zien. Tegelijkertijd constateren we een lancune ten aanzien van het hanteren van principes als 'privacy-by-design' en 'data visiting'. In de inleiding van de EHDS wordt in overweging 80 gesteld dat:

> _Gezien de gevoeligheid van gezondheidsgegevens moeten waar mogelijk beginselen als “privacy door ontwerp” en “privacy door standaardinstellingen” en het concept “breng de vragen naar de gegevens in plaats van die gegevens te verplaatsen” in acht worden genomen._

Het concept van de _data visiting_, ook wel bekend als _federated computing_ of Personal Health Train (PHT), wordt nergens in de EHDS nader toegelicht of beschreven[^1]. TEHDAS2 [_M7.4 Draft technical, functional and security specifications of Secure Processing Environments_](./appendix/tehdas2-spe.md) (hoofdstuk 6) gaat hier op in en maakt een aanzet voor de definitie van federated computing.

???+ abstract "Definities federated computing in TEHDAS2"
    
    === "**Gefedereerde berekening<br>(_federated computing_)**"
        Gedecentraliseerde berekening van data waarbij de berekeningen op lokale, gedistribueerde BVOs worden uitgevoerd in plaats van centrale verwerking in één BVO. Een dergelijke aanpak wordt aanbevolen in overweging 80 ten behoeve van _privacy preserving computation_. Gefedereerde berekening maakt het mogelijk om de data dichter bij hun originele locatie te houden waarbij alleen geaggregeerde resultaten of model parameters worden gedeeld, en daarmee privacy en veiligheid verhogen.
    
    === "**Gefedereerde analyse<br>(_federated analysis_)**" 
        Een specifieke vorm van gefedereerde verwerking waarbij statistieken lokaal worden berekend op verschillende, gedistrueerde BVOs. Deze methode is geschikt voor o.a. vergelijkende analyses, multi-centra onderzoek en andere vormen van collaboratieve statistische analyse. Alleen geaggregeerde resultaten of samenvattende statistieken worden uit de lokale BVOs geexporteerd, met bijbehorende waarborgen dat geen persoonsgegevens uit de BVO worden onttrokken.

    === "**Gefedereerd leren<br>(_federated learning_)**"
        Een specifieke vorm van gefedereerde berekening waarbij modellen worden getraind en gevalideerd op gedistribueerde BVOs. De ruwe data wordt niet gedeeld tussen de BVOs. In plaats daarvan worden alleen de model updates gedeeld om daarmee betere data privacy en beveiliging te bereiken. Omdat het moeilijk is om de anonimiteit van tussentijdse resultaten te beoordelen, is het essentieel dat gefedereerd leren gebeurd in een vertrouwd netwerk van BVOs.

    TEHDAS2 maakt onderscheid tussen twee scenarios, namelijk gefedereerde analyse (a) en gefedereerd leren (b).

    ![](federation-scenarios.png)

Dit document beschrijft een nadere uitwerking van wat in TEHDAS2 **federatieve BVO** wordt genoemd. Wij denken dat federatieve BVOs een belangrijke bijdrage kunnen leveren aan het effectief, efficient èn veilig implementeren van de EHDS. We zien federatieve BVOs als een aanvulling op c.q. alternatief voor centrale BVOs, zoals bijvoorbeeld de CBS Microdata omgeving of the _Trusted Research Environments_ zoals in [EOSC-ENTRUST](https://eosc-entrust.eu/) verband wordt geimplementeerd. De specificatie van een federatieve BVO zal worden ingebracht in de verdere uitwerking en implementatie van de EHDS in Nederland.


## Data stations als hoeksteen voor federatieve BVOs

Het concept van **data stations** staat centraal in de uitwerking van BVOs. Echter, het concept kent verschillende verschijningsvormen. Het originele concept van PHT omschrijft data stations in de context van federated learning[@choudhure2025advancing], wat vervolgens is generealiseerd om andere vormen van gefedereerde berekeningen te omvatten[@boninodasilvasantos2022personal]. De FAIR principes zijn uitgewerkt in het concept van [FAIR data point](https://specs.fairdatapoint.org/fdp-specs-v1.2.html), zijnde een data station gevuld met FAIR metadata wat is bedoeld als een gefedereerde oplossing voor een data catalogus. Het [Programma KIK-V](https://www.kik-v.nl/starten-met-kik-v) van het Zorginstituut heeft het concept van data stations geoperationaliseerd voor geautomatiseerde informatie-uitwisseling voor de VVT sector, wat een vorm is van gefedereerde analyse.


- het originele concept van  en is nog onvoldoende uniform gedfVerschillende projecten en initiatieven hebben Onze motivatie om dat te doen, waarbij de  een functionele specificatie van een __federatieve__ gezondheidsdata-infrastructuur voor onderzoek, beleid en innovatie, het zogenaamde secundair gebruik van data. Federatief in deze context wil zeggen dat het concept van __data stations__ centraal staat. Wat een data station precies omvat, welke functionaliteit het heeft en hoe het op landelijke schaal geimplementeerd kan worden, zijn de vragen waarop deze specificatie een antwoord geeft. Daarmee wil deze specificatie een bijdrage leveren aan de implementatie van de European Health Data Space (EHDS).

Het kerndoel van deze specificatie is om:

- Een overzicht te geven van de architectuur van een federatieve gezondheidsdata-infrastructuur, gebaseerd op data stations
- Beschrijven van de functionele specificaties van data stations en andere de andere componenten van een dergelijke infrastructuur
- Beschrijven van de werkprocessen die ten grondslag liggen aan secundair gebruik van data
- Beschrijven van referentie implementaties als leidraad voor verder ontwikkeling en adoptie van deze specificatie

## Proces voor de ontwikkeling en vaststelling van deze specificatie.

De eerste versie van deze specificatie is opgesteld in opdracht van Health-RI, als onderdeel van haar kerntaak om een hergebruik van gezondheidsgegevens mogelijk te maken. Verschillende experts en ervaringsdeskundigen zijn vanaf het begin betrokken in het schrijven en uitwerken van dit document. Het is de bedoeling dat specificatie begin 2026 ter consultatie wordt voorgelegd aan het werkveld via nog een nader te kiezen proces.

Vragen, reacties en feedback op dit document zijn van harte welkom. Gebruik hiervoor het commentaar veld hieronder.

## Attributie

Deze specificatie is opgesteld in opdracht van Health-RI door:

- [Daniel Kapitan](https://linkedin.com/in/dkapitan)
- [René Hietkamp](https://www.linkedin.com/in/renehietkamp/)

Daarnaast hebben de volgende personen een bijdrage geleverd aan de eerste versie:

- [Maarten Kollenstart](https://www.linkedin.com/in/maarten-kollenstart-a08429146/) (TNO): review algehele architectuur van data spaces, _verifiable credentials_
- [Tim Hendriks](https://www.maastrichtuniversity.nl/nl/tjn-hendriks) (Universiteit Maastricht): federated learning, beschrijving PLUGIN/vantage6 implementatie
- [Madou Derksen](https://www.linkedin.com/in/madou-derksen/) (Dutch Hospital Data): beschrijving PLUGIN/vantage6 implementatie
- [Rik Sonderkamp](https://www.linkedin.com/in/rik-sonderkamp/) (Visma Connect, in opdracht van Zorginstituut Nederland): beschrijving KIK-V implementatie


**:material-creative-commons: Dit werk is gelicenseerd onder een [Creative Commons Naamsvermelding 4.0 Internationaal licentie](https://creativecommons.org/licenses/by/4.0/).**

[^1]: Het woord _federated_ komt slecht twee keer voor in de EHDS verordening.