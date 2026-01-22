# KIK-V implementatie: process

## Functionele beschrijving vraag- en antwoordspel

![](https://kik-v-publicatieplatform.nl/api/gitblob?repositoryUrl=https%3A%2F%2Fgitlab.com%2Fkik-v%2Fafsprakenset&branchOrTag=3.0.0&path=Documentatie%2Fafspraken_gegevensuitwisseling_datastations%2Ffunctionele_beschrijving_vraag_en_antwoordspel.png)

De wijze waarop afnemers (datagebruikers) en aanbieder (datahouders) het KIK-V vraag- en antwoordspel vormgeven, is (mede) afhankelijk van de mate van digitalisering van de betrokken actoren. De afspraken en specificaties binnen KIK-V beschrijven het vraag- en antwoordspel met gebruik van datastations door zorgaanbieders en de KIK-starter door afnemers. Op basis van de afspraken en specificaties kunnen aanbieders een datastation implementeren voor toepassing van KIK-V en de uitwisseling met de KIK-starter voor afnemers. Afnemers kunnen naar de afspraken en specificaties verwijzen in de uitwisselprofielen.

In feite ondersteund KIK-V dus wat in de EHDS gegevensverzoeken worden genoemd, met gebruik van federated analytics in een decentraal netwerk van datastations.

## Principes

Voor de gegevensuitwisseling tussen KIK-starter en datastations zijn de algemene principes van de Afsprakenset KIK-V van toepassing. Hieruit volgen zaken zoals de toepassing van de Principes Informatiestelsel voor de zorg (P12) en de FAIR-dataprincipes (P10).

Daarbovenop zijn de afspraken opgebouwd aan de hand van de volgende drie principes:

1.  Schaalbaar decentraal model;
2. Zorginfrastructuur-onafhankelijk;
3. Correcte implementatie is eigen verantwoordelijkheid afnemer/aanbieder.

Deze principes worden hieronder nader toegelicht.

### Principe 1. Schaalbaar decentraal model
De potentie van de KIK-V werkwijze voor het meervoudig gebruik van data is groot. Doordat gegevens, inclusief de onderlinge samenhang tussen/betekenis van deze gegevens, gestandaardiseerd in datastations van aanbieders worden vastgelegd, is het mogelijk om met dezelfde gegevens te voorzien in antwoorden op een groot palet aan vragen. De technische uitwisseling met datastations dient te voorzien in dezelfde potentie aan schaalbaarheid. Om die reden is ervoor gekozen om het vraag- en antwoordspel zo in te richten dat zowel afnemers en zorgaanbieders in soort en aantal gemakkelijk deel kunnen nemen aan deze uitwisseling.

Voor het genereren van verifieerbare cryptografische bewijzen wordt de W3C-standaard Verifiable Credentials toegepast. Deze standaard kent drie rollen, namelijk die van issuer (uitgever), holder (houder) en verifier(verificateur). De issuer is een derde partij die autoriteit is over bepaalde informatie. Deze geeft een verklaring uit in de vorm van een verifieerbaar cryptografisch bewijs. De holder ontvangt dit verifieerbare bewijs en is de partij waarover de verklaring gaat. De holder past het technische bewijs toe in het rechtstreekse, decentrale proces met de verifier. Om de informatie in het bewijs te kunnen vertrouwen, controleert de verifier de waarachtigheid van de verklaring van de issuer. Dit doet de verifier tegen een onderliggende gezamenlijke vertrouwensregistratie (verifiable data registry). Issuer, holder en verifier zijn allen technisch aangesloten op deze verifiable data registry.

Zie voor de onderlinge verhoudingen tussen de rollen ook onderstaande afbeelding.

![](https://kik-v-publicatieplatform.nl/api/gitblob?repositoryUrl=https%3A%2F%2Fgitlab.com%2Fkik-v%2Fafsprakenset&branchOrTag=3.0.0&path=Documentatie%2Fafspraken_gegevensuitwisseling_datastations%2Fprincipe_1.png)

### Principe 2. Zorginfrastructuur-onafhankelijk
KIK-V realiseert en beheert geen zorginfrastructuur en maakt hergebruik van veldafspraken hierover. Het KIK-V vraag- en antwoordspel via datastations met de KIK-starter en met gebruik van de standaard Verifiable Credentials moet in principe toe te passen zijn via elke onderliggende zorginfrastructuur.

#### Voorlopige afbakening zorginfrastructuren

Het streven om zorginfrastructuur-onafhankelijk te werken, levert op korte termijn een aantal praktische issues op. In het geval dat (individuele) afnemers en aanbieders afwijkende keuzes maken voor de infrastructuur waarop zij hun koppelvlak baseren, dan komt dit samen als een interoperabiliteitsissue binnen KIK-V. Koppelvlakken uit verschillende infrastructuren begrijpen elkaar namelijk niet zondermeer. Alhoewel KIK-V zorginfrastructuur-onafhankelijk werkt, is voor de korte termijn een afbakening nodig in de toepassing van zorginfrastructuren. Dit om te voorkomen dat interoperabiliteitsissues binnen KIK-V samenkomen. De KIK-V ketenpartijen hebben aan het programma gevraagd om deze afbakening als volgt vorm te geven:

1. Door de implementatie van het KIK-V vraag- en antwoordspel met behulp van de KIK-starter via Nuts uit te werken in specificaties;
2. Door toe te werken naar interoperabiliteitsafspraken tussen Nuts en nID om te komen tot de voor alle partijen meest kostenefficiënte oplossing (nID wordt binnen iWLZ door zorgkantoren toegepast als zorginfrastructuur).

In 2023 is het voornemen geweest om vanuit deze afbakening beide soorten afspraken te beproeven in de pilot gegevensuitwisseling datastations. De pilot heeft uiteindelijk echter niet geleid tot de implementatie van interoperabiliteitsafspraken tussen Nuts en nID. Begin 2023 heeft de Werkgroep Interoperabiliteit Nuts-nID namelijk geadviseerd om op korte termijn niet toe te werken naar interoperabiliteit tussen Nuts en nID. In plaats daarvan is geadviseerd om vanuit Nuts en nID voorlopig parallel aan elkaar toe te werken naar een gedeeld toekomstbeeld o.b.v. soortgelijke standaarden (o.a. Verifiable Credentials, DID’s) en principes (o.a. DIZRA). Eind 2023 lijkt de werkgroep toch een (informele) doorstart te krijgen en wordt tussen Nuts en nID/iWLZ doorgewerkt aan een interoperabliteitsoplossing. Deze oplossing is gebaseerd op een beperkt aantal standaarden en voorziet vooralsnog niet in alle zaken die nodig zijn voor het KIK-V vraag en antwoordspel. Zo is het werken met verifiable credentials bijvoorbeeld nog geen onderdeel van de scope. KIK-V heeft daarom met iWLZ afgesproken om vanaf de zijlijn betrokken te blijven bij de ontwikkelingen en, zodra oplossingen via Nuts beschikbaar komen, te onderzoeken wat de impact is op de huidige Nuts specificaties. In de tussentijd past het programma de met succes in de pilot beproefde Nuts specificaties toe voor gegevensuitwisseling tussen de KIK-starter voor afnemers en de datastations voor aanbieders.

### Principe 3. Correcte implementatie is eigen verantwoordelijkheid afnemer/aanbieder
KIK-V bouwt, net als andere use cases voor gegevensuitwisseling in de zorg, zoveel mogelijk voort op (landelijke) afspraken op het gebied van zorginfrastructuur en informatiebeveiliging. De overtuiging vanuit KIK-V is dat het steeds opnieuw vormgeven van toetsing op deze afspraken binnen de verschillende initiatieven niet de meest schaalbare oplossing in Nederland vormt. KIK-V voorziet daarom niet in aparte toetsing van correcte implementatie van KIK-V overstijgende afspraken (NEN7510/7512/7513, koppelvlakken van zorginfrastructuren, etc.). Waar daar een bredere behoefte voor is, zou toetsing van een correcte implementatie van deze bredere afspraken KIK-V overstijgend kunnen worden vormgegeven. Voor zover het de implementatie van KIK-V betreft, wordt de correcte implementatie van deze afspraken als de eigen verantwoordelijkheid van afnemers en aanbieders gezien. De Beheerorganisatie KIK-V draagt die verantwoordelijkheid voor de KIK-starter KIK-V en het credentialsplatform.

De beheerorganisatie KIK-V voorziet overigens wel in een meldpunt voor problemen bij de gegevensuitwisseling. Dit meldpunt heeft met name als functie om patronen in meldingen te identificeren en deze neer te leggen bij de relevante probleemeigenaar.

