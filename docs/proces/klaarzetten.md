# Data klaarzetten voor verwerking (_data preparation_)

Het klaarzetten van de data begint als een datavergunning is afgegeven of een verzoek om data is goedgekeurd. De HDAB stuurt na het afgeven van de vergunning of goedkeuring een verzoek naar de dataleveranciers om de data klaar te zetten. Het klaarzetten gaat over het leveren van zowel persoonsgegevens als niet-persoonsgegevens. Het klaarzetten van de metadatabeschrijving van datasets voor de catalogus van gezondheidsgegevens is geen onderdeel van dit proces. Dit is onderdeel van het data zoeken en vinden.

**Persoonsgegevens**

Wanneer een gegevensvergunning is afgegeven of een verzoek is goedgekeurd, moeten de gezondheidsgegevens in elektronische vorm beschikbaar worden gesteld. Dit moet binnen drie maanden gebeuren, met de mogelijkheid om deze termijn één keer met nog eens drie maanden te verlengen als daar goede redenen voor zijn (Artikel 60(1) van de EHDS-verordening). De termijn start op het moment dat het HDAB de gegevenshouder informeert over de vergunning of het goedgekeurde verzoek, zoals beschreven in Artikel 63(3).

In het geval van data pooling betekent het beschikbaar stellen dat de gezondheidsgegevens van verschillende dataleveranciers worden samengebracht en gecombineerd tot één dataset, die vervolgens wordt gebruikt voor de data-analyse in een beveiligde verwerkingsomgeving. Wanneer de analyse federatief wordt uitgevoerd, worden de gezondheidsgegevens niet centraal verzameld, maar ter verwerking beschikbaar gesteld binnen het eigen datastation van de dataleverancier.

**Niet-Persoonsgegevens**

Als een organisatie beschikt over niet-persoonlijke elektronische gezondheidsgegevens — zoals geanonimiseerde gegevens waarbij personen niet meer identificeerbaar zijn, synthetische datasets of gegevens die niet over individuen gaan — moeten deze beschikbaar worden gesteld via openbare databanken. Deze databanken moeten voldoen aan normen voor transparantie, goed bestuur en duurzame toegankelijkheid (Artikel 60(5)).

Voor gezondheidsgegevens waarop intellectuele eigendomsrechten rusten of die bedrijfsgeheimen bevatten, geldt uiteraard dat deze niet in een openbare databank worden opgenomen (Artikel 52). Deze gegevens moeten echter wel beschikbaar worden gesteld voor secundair gebruik. 

**Verplichting**

Artikel 50 van de EHDS benoemt een aantal uitzonderingen waarbij datahouders geen gezondheidsgegevens hoeven te leveren. In de usecases gebruiken we daarom bewust de term dataleverancier in plaats van datahouder. Daarmee maken we een duidelijk onderscheid tussen de verantwoordelijkheid van een organisatie die gezondheidsgegevens bezit (datahouder) en die van een partij die deze gegevens moet aanleveren (dataleverancier). 

Een dataleverancier is verplicht om gegevens beschikbaar te stellen aan de HDAB op basis van een vergunning of een goedgekeurd verzoek. Overweging 80 van de EHDS benadrukt echter het principe: “breng de vragen naar de gegevens in plaats van de gegevens te verplaatsen”. Daarom wordt in de processen uitgegaan van een federatief netwerk waarbij data zoveel mogelijk bij de bron blijft. Dit betekent dat ‘beschikbaar stellen’ inhoudt dat waar mogelijk de gegevens bij de bron toegankelijk worden gemaakt voor de datagebruiker, zonder dat deze naar de HDAB worden getransporteerd.

## Overzicht van de usecases

De HDAB gebruikt een systeem voor het ontvangen en verwerken van aanvragen. Binnen het stelsel voor secundair gebruik heet dit systeem het Data Access Application Management System (DAAMS). Vanuit dit systeem verstuurt de HDAB een verzoek om data beschikbaar te stellen naar het datastation van een dataleverancier. het datastation is een systeem dat gebruikt wordt voor het beschikbaar stellen van data voor secundair gebruik.

![](uc-klaarzetten.drawio.svg)

///caption
**Figuur 5.** Overzicht van de usecases voor het klaarzetten van het extract uit de datasets.
///

De usecases uit het diagram zijn in de vervolgparagrafen kort beschreven.

## Maak data beschikbaar

Het uitgangspunt is dat de dataleverancier alle datasets voor de catalogus van gezondheidsgegevens heeft beschreven. Het beschikbaar stellen van gegevens vindt plaats op basis van deze beschreven datasets.

Wanneer een datagebruiker (bijvoorbeeld een onderzoeker) een vergunning aanvraagt, kiest deze zowel de benodigde datasets als een specifiek cohort — een groep mensen met een gemeenschappelijk kenmerk — waarvoor het onderzoek wordt uitgevoerd. Op basis van deze keuzes maakt de dataleverancier een extract van de dataset en stelt dit beschikbaar aan de datagebruiker.

Het verzoek aan de HDAB (Health Data Access Body) moet duidelijk specificeren op welke wijze de gegevens beschikbaar worden gesteld. Er zijn verschillende manieren mogelijk:

1. Gefedereerde analyse: De data blijft bij de datahouder en wordt beschikbaar gesteld voor een gefedereerde analyse.

2. Gefedereerd leren: De data blijft bij de datahouder en wordt beschikbaar gesteld voor het uitvoeren van gefedereerd leren (Federated Learning).

3. Datapooling (Gecombineerde analyse): De data wordt beschikbaar gesteld voor een analyse waarbij de gegevens van verschillende datahouders eerst gecombineerd moeten worden.

In het geval van datapooling moet de data door de verschillende datahouders naar de HDAB worden verzonden, alwaar de combinatie van de datasets beschikbaar wordt gesteld.

Voor een dataverzoek wordt géén extract gemaakt, maar wordt de dataset uitsluitend beschikbaar gesteld voor de ontvangst van het verzoek. Een dataverzoek houdt in dat de datagebruiker een vraag stelt, waarna de datahouder deze in een beveiligde verwerkingsomgeving uitvoert. Vervolgens wordt alleen het antwoord op de vraag teruggestuurd naar de datagebruiker. De dataset zelf wordt hierbij niet beschikbaar gesteld aan de datagebruiker.
