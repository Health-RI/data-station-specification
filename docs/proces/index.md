# 2 Perspectief: proces
## Het proces van secundair gebruik van data _system of interest_
Het _system of interest_ van deze specificatie is het proces en de daarbij benodige infomratie, applicaties en infrastructuur voor secundair gebruik van zorggegevens. Een dergelijk systeem bestaat uit verschillende elementen, zoals in figuur 3 is weergegeven.

![](health-ri-flowchart.jpg)

///caption
**Figuur 1.** Schematisch overzicht van het proces van secundair gebruik van data. Bron: Health-RI.
///

## Het proces van secundair gebruik vanuit het perspectief van de data gebruiker

In de draft documentatie van TEHDAS2 zijn de belangrijkste processtappen voor secundair gebruik benoemd. Deze hebben we gerelateerd aan bovenstaand diagram en zullen we in het als leidraad gebruiken in de uitwerking van de architectuur aan de hand van use-cases.

### Data zoeken en vinden (_data discovery_)
Voordat de gebruiker de gegevens kan gebruiken, moet worden nagegaan of de benodigde gegevens beschikbaar zijn in het benodigde formaat voor het secundaire gebruiksdoel. Datasets die beschikbaar zijn in de EU zijn te vinden in een catalogus van gezondheidsgevens op https://qa.data.health.europa.eu/. Zodra de data zijn gevonden, kan de data gebruiker beginnen met het aanvragen van de gegevens.

### Data aanvragen (_data access_)
Het aanvragen van toegang tot data is feitelijk een aanvraag tot verwerking door de data gebruiker van gegevens die door een gegevenshouder zijn verstrekt, in overeenstemming met specifieke technische, juridische of organisatorische vereisten, zonder noodzakelijkerwijs de overdracht of het downloaden van dergelijke gegevens te impliceren. (Verordening inzake Gegevensgovernance (DGA), Artikel 2(8), (9) en (13)). Op basis van de aanvraag wordt een vergunning verleend voor toegang tot de gegevens of een verzoek om data wordt goedgekeurd.

### Data klaarzetten voor verwerking (_data preparation_)
Gedurende deze fase leveren de gegevenshouders de benodigde gegevens aan de HDAB (Gezondheidsgegevens Toegangsorgaan), die de gegevens voorbereidt voor secundair gebruik. Hierbij worden technieken toegepast voor pseudonimisering, anonimisering, generalisatie, onderdrukking en randomisering van persoonsgegevens. Het beginsel van dataminimalisatie (conform de AVG/GDPR) moet worden gerespecteerd om de privacy te waarborgen.

### Data analyseren (_use of data_)
In deze fase voert de gebruiker analyses uit op basis van de ontvangen gegevens voor het doel dat is gedefinieerd in de aanvraagfase. Het analyseren van gegevens op persoonsniveau moet gebeuren in een BVO. De looptijd van de vergunning, en daarmee de periode waarbinnen de gegevens mogen worden geanalyseerd, is vastgelegd in de verordening (Art 68(12)).

### Resultaten publiceren (_finalisation_)
Deze laatste fase van het gebruikerstraject betreft de plichten van de gegevensgebruiker met betrekking tot de analyseresultaten die voortvloeien uit het secundaire gebruik van gegevens. De gegevensgebruiker moet de resultaten van het secundaire gebruik van gezondheidsgegevens publiceren binnen 18 maanden na de voltooiing van de gegevensverwerking in een veilige verwerkingsomgeving of na ontvangst van de gevraagde gezondheidsgegevens. De resultaten moeten in een anoniem formaat worden verstrekt. De gegevensgebruiker moet de HDAB (instantie voor toegang tot gezondheidsgegevens) op de hoogte stellen van de resultaten. Bovendien moet de gegevensgebruiker in de output vermelden dat de resultaten zijn verkregen door gebruik te maken van gegevens in het kader van de EHDS (Europese Ruimte voor Gezondheidsgegevens).

## Uitwerking in usecases

Met de usecase-methode wordt een methode bedoeld om de eisen aan een _system of interest_ te beschrijven. De methode begint met het identificeren van de actoren en de bijbehorende usecases. Een actor vertegenwoordigt een persoon, systeem, object of organisatie die interactie heeft met het systeem, zoals een “onderzoeker”, “dataleverancier” of “datastation”. Elke usecase vertegenwoordigt een specifiek stukje waarde van het systeem, uitgedrukt in functionaliteit voor de actor.

Het identificeren van actoren en usecases is geen eenmalige stap. Het gebeurt juist in meerdere iteraties, waarbij het inzicht stap voor stap groeit. Na elke iteratie wordt duidelijker welke waarde het systeem moet leveren voor de belanghebbenden.

Als de usecases zijn geïdentificeerd, worden ze verder beschreven. Een usecase beschrijft één logisch afgerond doel dat een actor wil bereiken, bijvoorbeeld “Zoeken van datasets”, “Aanvragen van gezondheidsdata” of “Bekijken van de status van een aanvraag”. De naam van een usecase is altijd geformuleerd als het functionele resultaat dat de actor wil behalen.

In dit document worden de usecases samengevat om de functionaliteit te beschrijven die nodig is voor de verschillende stappen in het proces voor secundair gebruik van data. Voor een meer gedetailleerde beschrijving van de functionele en technische vereisten verwijzen we naar de documenten van TEHDAS2[^1].

Usecases zijn niet alleen een methode om een systeem te beschrijven, maar ook om deze te ontwerpen, te ontwikkelen en te documenteren. Zodra de eisen voor een usecase duidelijk zijn, kan deze worden gerealiseerd. Het technische ontwerp van de usecase wordt een usecase-realisatie genoemd en bestaat onder andere uit sequentiediagrammen, statusdiagrammen en informatiemodellen. De componenten en andere bouwstenen in dit technische ontwerp worden hergebruikt voor alle usecases van het _system of interest_.


[^1]: TEHDAS2. (2025). Public consultation of the guidelines and technical specifications to enable seamless use of health data across Europe under the upcoming European Health Data Space (EHDS). https://tehdas.eu/public-consultations/





