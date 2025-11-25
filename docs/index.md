# Inleiding

## Op weg naar de EHDS
Op 26 maart 2025 is de verordening betreffende de European Health Data Space (EHDS) in werking getreden. De belangrijkste mijlpalen op weg naar de volledige uitvoering zijn:

- **maart 2027**: vaststelling landelijke uitvoeringswetten met gedetailleerde regels en praktische uitwerking van de verordening, inclusief de benoeming van de nationale Health Data Access Body (HDAB) als orgaan voor toezicht op en mogelijk maken van secundair gebruik.
- **maart 2029**: de verordening zal van toepassing zijn voor de eerste prioritaire categorieën van gezondheidsgegevens (patientendossiers, elektronische recepten en aflevering) in alle EU landen voor primair gebruik. De HDAB is operationeel en secundair gebruik is mogelijk voor de meeste gegevenscategorieën.
- **maart 2031**: de tweede groep prioritaire categorieën gezondheidsgegevens (medische beelden, laboratoriumuitslagen en ontslagverslagen) is beschikbaar voor primair gebruik. De regels voor secundair gebruik worden ook van toepassing voor de overige gegevenscategorieën (bv. genomische gegevens).
- **maart 2035**: derde landen en internationale organisaties kunnen zich aansluiten bij HealthData@EU voor het secundaire gebruik.

Dit document richt zich op de uitwerking een de EHDS specifiek voor secundair gebruik, zoals hieronder is weergegeven.

![](ehds-simpel.png)

///caption
**Figuur 1.** Vereenvoudigde weergave van secundair gebruik van data in de context van de EHDS.
///

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





## Proces voor de ontwikkeling en vaststelling van deze specificatie

De eerste versie van deze specificatie is opgesteld in opdracht van Health-RI, als onderdeel van haar kerntaak om hergebruik van gezondheidsgegevens mogelijk te maken. Verschillende experts en ervaringsdeskundigen zijn vanaf het begin betrokken bij het schrijven en uitwerken van dit document. Het is de bedoeling dat de specificatie begin 2026 ter consultatie wordt voorgelegd aan het werkveld via een nog nader te kiezen proces.

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

