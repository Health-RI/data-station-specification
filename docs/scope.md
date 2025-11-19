# Scope van de specificatie
## De gezondheidsdata-infrastructuur voor secundair gebruik als _system of interest_
Het _system of interest_ van deze specificatie is de gezondheidsdata-infrastructuur voor secundair gebruik. Een dergelijk systeem bestaat uit verschillende elementen, zoals hieronder conceptueel is weergegeven.

![](health-ri-flowchart.jpg)

///caption
**Figuur 1.** Schematisch overzicht van het proces van secundair gebruik van data. Bron: Health-RI.
///

??? abstract "Definities"
    De belangrijkste concepten van de gezondheidsinfrastructuur zijn gedefinieerd in de nieuwe Europease wetgeving, met name de European Health Data Space (EHDS) en de Data Governance Act (DGA).

    === "**Beveiligde verwerkingsomgeving (BVO)**"
        Een beveiligde omgeving waarin gezondheidsgegevens verwerkt kunnen worden voor bijvoorbeeld wetenschappelijk onderzoek. Dit kan een centrale BVO zijn, zoals bijvoorbeeld de [CBS Microdata omgeving](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen), een gefedereerde BVO of een hybride combinatie daarvan. Dit focus van deze specificatie is dat data stations als hoeksteen kunnen fungeren voor een netwerk van BVOs.
    
    === "**Data gebruiker**" 
        Een persoon of organisatie die toegang heeft gekregen tot elektronische gezondheidsgegevens voor secundair gebruik. Bijvoorbeeld een onderzoeker, een beleidsmederwerker of een ontwikkelaar van commerciële producten.

    === "**Data houder**"
        Een data houder is een persoon of organisatie (publiek of privaat) die gezondheidsdata beheert. Veel organisaties vallen hieronder. Het gaat niet alleen om ziekenhuizen, maar bijvoorbeeld ook iedereen die producten of diensten ontwikkelt die bestemd zijn voor de zorgsector of gezondheidszorg, of ontwikkelaars van wellnessapps, of wetenschappelijk onderzoekers die zich bezighouden met de zorgsector of gezondheidszorg.

    === "**Secundair gebruik**"
        Het gebruik van elektronische gezondheidsgegevens voor andere doeleinden dan die waarvoor ze verzameld zijn. Het gebruiken van gezondheidsgegevens, die zijn vastgelegd voor de behandeling van een patiënt, voor wetenschappelijk onderzoek, is een voorbeeld van secundair gebruik.

## Het proces van secundair gebruik vanuit het perspectief van de data gebruiker

In de draft documentatie van TEHDAS2 zijn de belangrijkste processtappen voor secundair gebruik benoemd.

###  Data zoeken en vinden (_data discovery_)
Voordat de gebruiker de gegevens kan gebruiken, moet hij of zij nagaan of de benodigde gegevens beschikbaar zijn en of deze beschikbaar zijn in het noodzakelijke formaat voor het secundaire gebruiksdoel. Datasets die beschikbaar zijn in de EU zijn te vinden in een metadatacatalogus op https://qa.data.health.europa.eu/. Zodra de data zijn gevonden, kan de data gebruiker beginnen met het proces van het aanvragen van de gegevens.

### Data aanvragen (_data access_)
Het aanvragen van toegang tot data is feitelijk een aanvraag tot verwerking door de data gebruiker van gegevens die door een gegevenshouder zijn verstrekt, in overeenstemming met specifieke technische, juridische of organisatorische vereisten, zonder noodzakelijkerwijs de overdracht of het downloaden van dergelijke gegevens te impliceren. (Verordening inzake Gegevensgovernance (DGA), Artikel 2(8), (9) en (13)).

### Data klaarzetten voor verwerking (_data preparation_)
Gedurende deze fase leveren de gegevenshouder(s) de noodzakelijke gegevens aan de HDAB (Gezondheidsgegevens Toegangsorgaan), die begint met het voorbereiden van de gegevens voor secundair gebruik. Er worden technieken voor pseudonimisering, anonimisering, generalisatie, onderdrukking en randomisering van persoonsgegevens toegepast. Het beginsel van dataminimalisatie (conform de AVG/GDPR) moet worden gerespecteerd om de privacy te waarborgen.

### Data analyseren (_use of data_)
In deze fase voert de gebruiker analyses uit op basis van de ontvangen gegevens voor het doel dat is gedefinieerd in de aanvraagfase. Het analyseren van gegevens op persoonsniveau moet gebeuren in een BVO. De duur van deze fase wordt gespecificeerd in de verordening (Art 68(12)).

### Resultaten publiceren (_finalisation_)
Deze laatste fase van het gebruikerstraject betreft de plichten van de gegevensgebruiker met betrekking tot de analyseresultaten die voortvloeien uit het secundaire gebruik van gegevens. De gegevensgebruiker moet de resultaten van het secundaire gebruik van gezondheidsgegevens publiceren binnen 18 maanden na de voltooiing van de gegevensverwerking in een veilige verwerkingsomgeving of na ontvangst van de gevraagde gezondheidsgegevens. De resultaten moeten in een anoniem formaat worden verstrekt. De gegevensgebruiker moet het gezondheidsgegevens toegangsorgaan op de hoogte stellen van de resultaten. Bovendien moet de gegevensgebruiker in de output vermelden dat de resultaten zijn verkregen door gebruik te maken van gegevens in het kader van de EHDS (Europese Ruimte voor Gezondheidsgegevens).

