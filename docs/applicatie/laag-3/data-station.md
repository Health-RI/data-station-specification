# Datastation

In een dataspace voor secundair gebruik is het datastation, naast de processing hub, een essentieel component. Waar de processing hub het component is voor de data-afnemer, is het datastation dat voor de dataleverancier. Beide componenten zijn daarmee elkaars tegenhanger binnen de dataspace-architectuur: voor iedere rol is één kerncomponent gedefinieerd.

Het datastation is een technisch component dat is opgenomen in een knooppunt van de dataspace. Vanuit het datastation stelt de dataleverancier data beschikbaar voor secundair gebruik, onder vooraf vastgestelde voorwaarden. Het datastation ondersteunt functies zoals het ontsluiten van datasets, het toepassen van toegangs- en gebruiksvoorwaarden, het waarborgen van beveiliging en privacy, en het faciliteren van interoperabiliteit met andere knooppunten binnen de dataspace.

Door deze rolverdeling ontstaat een heldere scheiding van verantwoordelijkheden: de dataleverancier behoudt via het datastation controle over de beschikbaarstelling en het gebruik van data, terwijl de data-afnemer via de processing hub de data kan verwerken en analyseren binnen de afgesproken kaders. Samen vormen het datastation en de processing hub de fundamenten voor een betrouwbare, schaalbare en interoperabele dataspace voor secundair gebruik.

!!! info "Definitie van een datastation"

    Een datastation is een door een dienstverlener beheerde omgeving waarin datasets en gegevensdiensten van een dataleverancier worden ontsloten volgens afgesproken standaarden, met expliciete regels voor toegang, autorisatie, logging en gebruik, zodat gegevens betrouwbaar en interoperabel kunnen worden gebruikt en worden uitgewisseld binnen een dataspace.

Het datastation is als systeem betrokken in de processen voor het [klaarzetten](../../proces/klaarzetten.md) van data en het [analyseren](../../proces/analyseren.md) van data. Het moet deze processen ondersteunen met de usecases getoond in onderstaand diagram. Deze worden in de volgende paragrafen verder uitgewerkt.

![](uc-datastation.drawio.svg)

///caption
**Figuur 3.** Usecasediagram van het datastation voor secundair gebruik
///

In de onderstaande paragrafen worden de eisen aan een datastation beschreven.

!!! info "Een dataspace schrijft niet de architectuur van een datastation voor"

    De architectuur van een datastation is de verantwoordelijkheid van de dienstverlener die het datastation aanbiedt. Een dienstverlener moet een datastation autonoom kunnen realiseren en implementeren; iedere deelnemer aan de dataspace opereert immers zelfstandig.

    Om die reden wordt in dit hoofdstuk geen gedetailleerde architectuur uitgewerkt. Vanuit de dataspace is het vooral van belang dat de interoperabiliteit met het datastation is geborgd en dat het vertrouwen en de integriteit van de dataspace als geheel worden gewaarborgd, over alle autonome onderdelen heen. De eisen aan een datastation richten zich daarom alleen op interoperabiliteit en vertrouwen.


## Meld catalogus van datasets aan

Iedere dataleverancier is zelf verantwoordelijk voor het catalogiseren en publiceren van haar datasets. Dit betekent dat de dataleverancier een eigen datasetcatalogus samenstelt en beheert. In dit document spreken we niet af welke datasets in de catalogus moeten worden opgenomen, maar alleen welk formaat wordt gebruikt. De catalogus moet worden opgesteld in [HealthDCAT-AP Release 5](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/).

De catalogus moet toegankelijk zijn via het datastation. In de EHDS is vastgelegd (artikel 77) dat de catalogus die door de Health Data Access Body (HDAB) wordt gepubliceerd openbaar toegankelijk is. In lijn daarmee kan ook de catalogus op het datastation openbaar toegankelijk zijn.

![](datastation-aanmelden.drawio.svg)

///caption
**Figuur 4.** Componenten voor het aanmelden van de catalogus van datasets
///

Zoals in het bovenstaande diagram te zien is, moet een datastation een catalogus aanmelden. Dit is een eenmalig proces, waarna het component van de Nationale Catalogus het datastation samen met de catalogus van de leverancier registreert. Deze registratie is nodig om de catalogus daarna periodiek te kunnen ophalen. Voor het aanmelden van de catalogus zal een koppelvlak worden gedefinieerd.

## Haal periodiek catalogus van datasets op

De Health Data Access Body (HDAB) is met het component voor de Nationale Catalogus volledig autonoom in het bepalen van de frequentie waarmee de Nationale Catalogus wordt bijgewerkt. Dit betekent dat de HDAB kan plannen wanneer de catalogus van een dataleverancier wordt opgehaald, in plaats van dat dit ad hoc door alle leveranciers tegelijk gebeurt.

![](datastation-ophalen.drawio.svg)

///caption
**Figuur 5.** Componenten voor het ophalen van de catalogus van datasets
///

Door deze autonomie ontstaat een efficiënte en gecontroleerde updateprocedure, waardoor piekbelasting of “filevorming” wordt voorkomen wanneer meerdere dataleveranciers tegelijk hun catalogus willen bijwerken. Bovendien draagt deze regeling bij aan de betrouwbaarheid en stabiliteit van de Nationale Catalogus, omdat updates gespreid en voorspelbaar plaatsvinden. Dit biedt zowel de HDAB als de dataleveranciers meer controle over het proces en helpt bij het waarborgen van consistente en actuele informatie in de dataspace.

## Maak data beschikbaar voor secundair gebruik

![](datastation-klaarzetten.drawio.svg)

///caption
**Figuur 6.** Proces voor het klaarzetten van data, met alternatieve scenario's voor het uitvoeren van data pooling en federatie
///

![](datastation-organiseren.drawio.svg)

///caption
**Figuur 7.** Overzicht van het organiseren en klaarzetten van de data voor federatieve analyse
///

## Verwerk algoritme en geef resultaat terug

![](datastation-analyseren.drawio.svg)

///caption
**Figuur 8.** Proces voor het federatief uitvoeren van een algoritme
///



![](datastation-leveren.drawio.svg)

///caption
**Figuur 9.** Overzicht van het uitvoeren van een federatieve analyse en het leveren van de resultaten
///




## Geef antwoord op dataverzoek

![](datastation-dataverzoek.drawio.svg)

///caption
**Figuur 10.** Proces voor het federatief uitvoeren van een dataverzoek
///
