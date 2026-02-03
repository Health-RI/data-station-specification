# 2.1. Data zoeken en vinden (_data discovery_)

Het zoeken en vinden van data is de eerste stap in het hele proces. Een potentiële aanvrager — zoals een onderzoeker of een beleidsdepartement — wil eerst ontdekken welke data over een bepaald onderwerp beschikbaar zijn en onder welke voorwaarden deze kunnen worden gebruikt. Dit zoeken gebeurt via een Nationale catalogus van datasets. Op Europees niveau worden deze nationale catalogi ontsloten via het centrale platform van HealthData@EU (hierna: het centrale platform).

Het publiceren en beheren van een Nationale catalogus van datasets is een taak van de HDAB, zoals vastgelegd in artikel 57(1j) van de EHDS[^1].

!!! info "Datagebruiker versus dataleverancier"

    In de usecases gebruiken we bewust de term dataleverancier in plaats van datahouder. Daarmee maken we een duidelijk onderscheid tussen de verantwoordelijkheid van een organisatie die gezondheidsgegevens bezit (datahouder) en een organisatie die gegevens beschikbaar moet stellen (dataleverancier). Artikel 50 van de EHDS benoemt een aantal uitzonderingen waarbij datahouders geen gezondheidsgegevens hoeven te leveren.

## 2.1.1. Overzicht van de usecases

In het overzicht van de usecases wordt de actor tijd weergegeven om aan te geven dat deze usecase periodiek wordt uitgevoerd. Binnen het systeem van de Nationale catalogus voor datasets worden deze periodes gepland om de catalogus bij de dataleveranciers op te halen. De dataleveranciers hebben hiervoor een datastation ingericht waarop de catalogus is gepubliceerd.

![](uc-vinden.drawio.svg)

///caption
**Figuur 2.** Overzicht van de usecases voor het zoeken en vinden van datasets.
///

De usecases uit het diagram zijn in de vervolgparagrafen kort beschreven.

## 2.1.2. Meld catalogus aan

Dataleveranciers stellen een catalogus op en publiceren deze voor minimaal de datasets die zij beheren en die onder de categorieën van artikel 51 van de EHDS vallen. De leverancier waarborgt vervolgens dat deze catalogus via het datastation toegankelijk is voor alle deelnemers van de dataspace.

De dataleverancier hoeft de catalogus slechts één keer aan te melden. Daarbij geeft zij het adres (URL) op van het datastation waarop de catalogus is gepubliceerd. Deze stap is verplicht overeenkomstig artikel 60 van de EHDS. Minimaal 1x per jaar moet de dataleverancier 

## 2.1.2. Update Nationale catalogus met catalogussen van dataleveranciers

Het systeem controleert periodiek of de catalogus van de dataleverancier is bijgewerkt. Vervolgens wordt de catalogus gedownload en geïntegreerd in de publieke Nationale catalogus van datasets. Alleen de catalogus van een dataleverancier die zich heeft aangemeld, wordt gecontroleerd.

Als beheerder van de Nationale catalogus van datasets zal de HDAB de Nationale catalogus doorsturen naar het centrale platform van HealthData@EU. Dit gebeurt nadat de catalogi van alle aangemelde dataleveranciers zijn verwerkt. Het verzenden van de catalogus verloopt via het Nationale contactpunt.

## 2.1.3. Zoek datasets

Een onderzoeker of andere partij kan in de Nationale of Europese catalogus zoeken naar relevante datasets. In de beschrijving van de datasets moet voldoende informatie beschikbaar zijn om te bepalen welke data gebruikt kan worden voor een van de doelen zoals genoemd in artikel 53 van de EHDS. Het formaat van de catalogus is beschreven in HealthDCAT-AP Release 5.[^2]

!!! info "Welke data wordt gepubliceerd in de catalogus"

    Alle categorieën elektronische gezondheidsgegevens overeenkomstig artikel 51 van de EHDS moeten beschikbaar zijn voor secundair gebruik. Voor gegevens uit elektronische gezondheidsdossiers gaan we zoveel mogelijk uit van databeschikbaarheid in een of meerdere van de drie meest gebruikte klinische informatiemodellen, zijnde FHIR, OMOP en openEHR.[@tsafnat2024converge] Voor gegevens waarin dat niet mogelijk is, zoals administratieve gegevens op het gebied van gezondheidszorg (artikel 51 lid 1e) en gegevens met betrekking tot gezondheidswerkers (artikel 51 lid 1j), gaan we uit van een RDF-formaat overeenkomstig de FAIR-dataprincipes.[^3]


[^1]: European Parliament and Council. (2025). Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2025/327/

[^2]: Chouaiech, M., Derycke, P., Van Nuffelen, B. et al. (2025, September 22). HealthDCAT-AP Release 5. EC DG-SANTE. https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/ 

[^3]: Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. (2016, Maart 15).The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data. https://rdcu.be/eSNTr