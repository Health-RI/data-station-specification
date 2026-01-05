# Datastation

Het datastation is als systeem betrokken in de processen voor het [klaarzetten](../../proces/klaarzetten.md) van data en het [analyseren](../../proces/analyseren.md) van data. Het moet het proces ondersteunen met de functionaliteit getoond in onderstaand diagram.

!!! info "Definitie van een datastation"

    Een datastation is een door een dienstverlener beheerde omgeving waarin datasets en gegevensdiensten van een dataleverancier worden ontsloten volgens afgesproken standaarden, met expliciete regels voor toegang, autorisatie, logging en gebruik, zodat gegevens betrouwbaar en interoperabel kunnen worden gebruikt en worden uitgewisseld binnen een dataspace.

In onderstaande figuur zijn de usecases van een datastation opgenomen. Deze worden in de volgende paragrafen verder uitgewerkt.

![](uc-datastation.drawio.svg)

///caption
**Figuur 3.** Usecasediagram van het datastation voor secundair gebruik
///

De architectuur van een datastation is de verantwoordelijkheid van de dienstverlener die het datastation aanbiedt. Een dienstverlener moet een datastation autonoom kunnen realiseren en implementeren; iedere deelnemer aan de dataspace opereert immers zelfstandig.

Om die reden wordt in dit hoofdstuk geen gedetailleerde architectuur uitgewerkt. Vanuit de dataspace is het vooral van belang dat de interoperabiliteit met het datastation is geborgd en dat het vertrouwen en de integriteit van de dataspace als geheel worden gewaarborgd, over alle autonome onderdelen heen. De eisen aan een datastation richten zich daarom alleen op interoperabiliteit en vertrouwen.

In de onderstaande paragrafen worden de eisen aan een datastation beschreven.

## Meld catalogus van datasets aan

Iedere datalevencier heeft de verantwoordelijkheid om haar datasets te catalogiseren en te publiceren.

![](datastation-aanmelden.drawio.svg)

///caption
**Figuur 4.** Componenten voor het aanmelden van de catalogus van datasets
///

## Haal periodiek catalogus van datasets op

Hierdoor kan de Nationale catalogus plannen wanneer ze een catalogus ophaalt en is er geen filevorming als alle dataleveranciers besluiten om de catalogus te willen updaten

![](datastation-ophalen.drawio.svg)

///caption
**Figuur 5.** Componenten voor het ophalen van de catalogus van datasets
///

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

## Geef antwoord op dataverzoek

![](datastation-dataverzoek.drawio.svg)

///caption
**Figuur 9.** Proces voor het federatief uitvoeren van een dataverzoek
///
