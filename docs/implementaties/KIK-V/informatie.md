# KIK-V implementatie: informatie

## Ontologie

![](https://www.kik-v.nl/_next/image?url=https%3A%2F%2Fwww.kik-v.nl%2Fsite%2Fbinaries%2Fcontent%2Fgallery%2Fsite-content%2Fcontent-afbeeldingen%2Fplaatje-ontologie-voor-dummies.png&w=2560&q=70)

### Wat is een ontologie

Binnen de KIK-V werkwijze helpt ontologie om eenduidigheid te creëren, zodat iedereen – van zorgaanbieders tot beleidsmakers – dezelfde taal spreekt. Een ontologie is een gestructureerde manier om betekenis te organiseren en machine-leesbaar te maken. Bijvoorbeeld: in de zorg heb je begrippen (in de KIK-V taal concepten genoemd) als ‘cliënt’, ‘behandeling’ en ‘factuur’. Een ontologie legt vast wat deze concepten betekenen en hoe ze met elkaar samenhangen. Een ontologie is daarmee een kennismodel dat mensen en informatiesystemen helpt om gegevens over deze concepten op een uniforme manier te begrijpen en te verwerken.

### Waarom is een ontologie nodig?

In zorgorganisaties wordt veel informatie vastgelegd, maar dit gebeurt niet altijd op dezelfde manier. De ene organisatie spreekt over een ‘patiënt’, terwijl de andere ‘cliënt’ zegt. Dit kan verwarrend zijn als verschillende partijen gegevens willen uitwisselen.

De ontologie van KIK-V zorgt ervoor dat iedereen binnen de verpleeghuiszorg dezelfde taal spreekt, zonder dat bestaande gegevens bij de bron aangepast hoeven te worden. Er wordt als het ware een ‘betekenislaag’ over de data gelegd, zodat iedereen dezelfde informatie op dezelfde manier begrijpt. Dit maakt het makkelijker om gegevens uit te wisselen en vragen van bijvoorbeeld de overheid of andere instanties eenduidig te beantwoorden. Een goed voorbeeld uit de KIK-V ontologie: in plaats van het begrip ‘verpleeghuis’, wordt onderscheid gemaakt tussen ‘verpleeghuisorganisatie’ en ‘verpleeghuisgebouw’. Dit maakt het meteen duidelijk of we praten over het bedrijf dat de zorg verleent of over het fysieke gebouw waar mensen wonen.

### Waar wordt de ontologie voor gebruikt?

De ontologie van KIK-V wordt gebruikt om informatie-uitwisseling in de Nederlandse verpleeghuiszorgsector makkelijker en eenduidiger te maken. Het bestaat uit verschillende onderdelen, bijvoorbeeld voor:

- Organisatiestructuur
- Financiën
- Zorgverlening
- Personeel

Al deze informatie is openbaar en gratis te bekijken en te downloaden via het [publicatieplatform van KIK-V](https://kik-v-publicatieplatform.nl/). Zo kunnen aanbieders in de verpleeghuiszorg en informatie-vragende partijen die met KIK-V werken deze informatie inzien en gebruiken om makkelijker samen te werken en gegevens te delen.


## Data beschikbaar maken

Het [KIK-V stappenplan](https://www.kik-v.nl/starten-met-kik-v) beschrijft hoe aan het begin van de implementatie een analyse wordt gemaakt van de beschikbare informatie en de aanpak om dit beschikbaar te maken. De analyse bestaat:

- **Inventarisatie bronsystemen**: bronsystemen zoals HRM, financiële programma’s en het ECD worden in kaart gebracht.
- **Inrichting bronsystemen**: beoordeel of de benodigde gegevens voor het beantwoorden van de vragen in de bronsystemen aanwezig zijn. Gegevens die ontbreken, onvolledig zijn of verkeerd geregistreerd zijn uit de bronsystemen worden aangeduid als 'niet beschikbare gegevens'.

Met de zogenaamde **referentieontwerpen** kan worden bepaald in hoeverre de **modelgegevensset**, het totaal aan gegevens wat gebruikt kan worden binnen de KIK-V werkwijze, geautomatiseerd kan worden samengesteld.

### Referentieontwerpen

Referentieontwerpen vormen een belangrijk onderdeel van de implementatie-ondersteuning vanuit KIK-V. In de referentieontwerpen zijn voor veel voorkomende applicaties uitgewerkt hoe de benodigde gegevens beschikbaar kunnen worden gesteld voor het berekenen van indicatoren. Samen met de leveranciers van de meest voorkomende systemen zijn de referentieontwerpen ontwikkeld. Met de referentieontwerpen kan bepaald worden in hoeverre de modelgegevensset geautomatiseerd kan worden samengesteld vanuit de systemen. Ook biedt het inzicht in de aanpassingen die gedaan kunnen worden om de overige gegevens uit de systemen te halen.

Per december 2025 zijn voor [10 bronsystemen](https://www.kik-v.nl/onderwerpen/r/referentieontwerpen) referentieontwerpen opgesteld, zodat datahouders zo min mogelijk zelf de mapping van het informatiemodel van het bronsysteem naar de KIK-V ontologie hoeven te maken.

### Modelgegevenset

De afsprakenset maakt voor het definiëren van de gegevens, die aanbieders toepassen in het formuleren van de antwoorden op informatievragen omschreven in het uitwisselprofiel, gebruik van de modelgegevensset. De modelgegevensset is het resultaat van het matchingsproces, een afstemming tussen informatiebehoefte en beschikbare gegevens bij de zorgaanbieder. In de modelgegevensset zijn tevens de definities opgenomen van de gehanteerde gegevens.

De modelgegevensset wordt gebruikt om bij de gegevensuitwisseling invulling te kunnen geven aan (de concepten uit) de informatievragen van afnemers (datagebruikers). De set bevat de semantiek van de gegevens die zorgaanbieders beschikbaar stellen voor het beantwoorden van de vragen. De semantiek is voor alle aanbieders en afnemers uniform in een Ontologie (methode om de betekenis van concepten binnen een specifieke context te beschrijven) vastgelegd.

Datahouders kunnen, al dan niet in overleg met hun softwareleveranciers, zelf bepalen hoe zij vanuit de brondata tot de juiste afbeelding van de gegevens op de ontologie (voor de gebruikte modelgegevensset) komen. Datahouders zijn zelf verantwoordelijk voor de wijze waarop zij dit doen. Dit geeft hen de ruimte om de koppeling tussen bronsystemen en de modelgegevensset op eigen wijze in te vullen. De uitkomst hiervan is de aanbieder-gegevensset.

### Uitwisselprofiel

Een uitwisselprofiel beschrijft welke vragen worden gesteld door een informatie-vragende partij. Dit is een specifieke vragenlijst per partij en per onderwerp. In elk profiel staat omschreven hoe er wordt omgegaan met de aangeleverde antwoorden, waarvoor dit wordt gebruikt en hoe de terugkoppeling naar de zorgaanbieder verloopt. Er zijn verschillende [uitwisselprofielen](https://kik-v-publicatieplatform.nl/uitwisselprofielen) gedefineerd. Om een indruk te geven hierbij een uitwisselprofiel waarin het gemiddeld aantal personeelsleden wordt berekend.

???+ abstract "Voorbeeld uitwisselprofiel"

    #### Definities

    * Een persoon telt naar rato mee voor de periode dat hij/zij personeelslid is in het kwartaal.
    * Bijvoorbeeld, tijdens een kwartaal telt een persoon die gedurende de helft van het kwartaal over een werkovereenkomst beschikte (en dus personeelslid was), als 0,5 mee in de berekening van de indicator. 
    * Zowel personeel in loondienst (PIL) als personeel niet in loondienst (PNIL) telt mee; stagaires en vrijwilligers tellen niet mee.
    * Opgenomen in de [Algemene Uitgangspunten](https://kik-v-publicatieplatform.nl/documentatie/Algemene%20uitgangspunten/_) zijn: 
    vestiging, meetperiode, zorgverlener en de "Relaties tussen werkovereenkomsten, rollen en groepen". 


    #### Toelichting

    * De inputparameter voor deze indicator is een jaar (jjjj), kwartaal (Qx) en het zorgkantoor. De vestigingen worden getoond op de zorgkantoor-regio van het zorgkantoor; dit betekent dat voor sommige zorgaanbieders een deel van haar vestigingen worden getoond.

    #### Voorbeeld

    Onderstaande tabel beschrijft een voorbeeld van de manier waarop een medewerker meetelt in elk van de categorieen. Deze medewerker beschikte de helft van een kwartaal over een werkovereenkomst. De eerste helft (een kwart van het kwartaal) was de medewerker specialist ouderen geneeskunde (een functie als zorgverlener), de tweede helft manager (een functie als niet-zorgverlener).  

    | Indeling |  Zorg  | Niet-zorg | Totaal |
    |----------------|--------|-----------|--------|
    | Totaal organisatie |  0,25  | 0,25      | 0,5    |
    | Vestiging       |  0,25  | 0,25      | 0,5    |


    #### Berekening

    1. Selecteer alle arbeids-<sup>5</sup>, inhuur-<sup>6</sup> en oproep<sup>7</sup>-overeenkomsten (allen subset van werkovereenkomst<sup>1</sup>) die overlap hadden met dat kwartaal. Dit betekent dat de begindatum van de werkovereenkomst<sup>1</sup> ligt voor of op de einddatum van het kwartaal en de einddatum ligt niet voor de start van het kwartaal
    2. Selecteer voor deze werk-overeenkomst<sup>1</sup> alle werkovereenkomst-afspraken<sup>2</sup> die overlap hebben met het kwartaal.
    3. Bepaal voor deze werkovereenkomst-afspraken<sup>2</sup> of de functie<sup>4</sup> een zorgverlener-functie<sup>3</sup> is. 
    4. Bepaal voor deze werkovereenkomst-afspraken<sup>2</sup> de vestiging<sup>8</sup> en de persoon<sup>9</sup>.
    5. Bereken per persoon<sup>9</sup> het aantal dagen dat de werkovereenkomst-afspraken overlap hadden met het kwartaal.
    6. Sommeer de aantallen van stap 5 per vestiging<sup>8</sup>, voor totaal, zorg<sup>3</sup> en niet-zorg, en deel door het aantal dagen in het kwartaal.
    7. Haal voor alle vestigingen<sup>8</sup> het vestigingsnummer<sup>11/sup> op. Dit is de input voor de rijen van de eerste kolom, indeling. 
    8. Filter de vestigingen<sup>8</sup> op de zorgkantoor-regio<sup>15</sup>. Haal hiervoor voor alle vestigingen<sup>10</sup> het lokaliseerbaar gebied<sup>12</sup>, de 6 cijferige postcode op. Leidt de eerste vier cijfers af van stap 6, de afgeleide postcode wordt gebruikt om een postcodegebied<sup>13</sup> op te zoeken. Het postcodegebied<sup>13</sup> maakt deel uit van een administratief gebied<sup>14</sup>, de zorgkantoorregio<sup>15</sup>. 

    | Indeling |  Zorg  | Niet_zorg | Totaal |
    |----------------|--------|-----------|--------|
    | Totaal organisatie | Stap 6 | Stap 6    | Stap 6 |
    | Vestiging 1      | Stap 7 | Stap 7    | Stap 7 |
    | Vestiging 2      | Stap 7 | Stap 7    | Stap 7 |
    | Vestiging *n*      | Stap 7 | Stap 7    | Stap 7 |

    #### Begrippen en ontologie

    * <sup>1</sup>. [werkovereenkomst](http://purl.org/ozo/onz-pers#WerkOvereenkomst)
    * <sup>2</sup>. [werkovereenkomst-afspraak](http://purl.org/ozo/onz-pers#WerkOvereenkomstAfspraak)
    * <sup>3</sup>. [zorgverlener functie](http://purl.org/ozo/onz-pers#Zorgverlener%20(functie))
    * <sup>4</sup>. [functie](http://purl.org/ozo/onz-g#OccupationalPositionRole)
    * <sup>5</sup>. [arbeidsovereenkomst](http://purl.org/ozo/onz-pers#ArbeidsOvereenkomst)
    * <sup>6</sup>. [inhuurovereenkomst](http://purl.org/ozo/onz-pers#InhuurOvereenkomst)
    * <sup>7</sup>. [oproepovereenkomst](http://purl.org/ozo/onz-pers#OproepOvereenkomst)
    * <sup>8</sup>. [vestiging](http://purl.org/ozo/onz-org#Vestiging)
    * <sup>9</sup>. [Persoon](http://purl.org/ozo/onz-g#Human) 
    * <sup>11</sup>. [vestigingsnummer](http://purl.org/ozo/onz-org#Vestigingsnummer)
    * <sup>12</sup>. [lokaliseerbaar gebied]( http://purl.org/ozo/onz-g#LocalizableArea)
    * <sup>13</sup>. [postcodegebied](http://purl.org/ozo/onz-g#PostcodeArea)
    * <sup>14</sup>. [administratief gebied](http://purl.org/ozo/onz-g#AdministrativeRegion)
    * <sup>15</sup>. [zorgkantoor-regio](http://purl.org/ozo/onz-org#ZorgkantoorRegio)


