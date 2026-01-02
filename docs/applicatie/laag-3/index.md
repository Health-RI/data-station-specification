# Laag 3 van de zandloper

De derde laag van het zandlopermodel bestaat uit een netwerk van knooppunten met een datastation. Een datastation is een abstract begrip voor het systeem dat ervoor zorgt dat data beschikbaar kan worden gesteld voor secundair gebruik. De term datastation wordt zowel gebruikt binnen primair als secundair gebruik, maar de functie en de eisen verschillen.

## Verschillen tussen datastations voor primair en secundair gebruik

Bij primair gebruik is de functie van het datastation niet het beschikbaar stellen van data, maar het toegankelijk maken van een patiëntendossier voor de afnemer van de data, die de data beschikbaar maakt voor de eindgebruiker: de zorgverlener. Om dit onderscheid duidelijk te maken, spreken we bij primair gebruik over het toegankelijk maken van data. Het datastation bewaakt hierbij de toegang tot het patiëntendossier op basis van afgesproken en wettelijke toegangsregels. 

Bij secundair gebruik worden datasets, waarin meerdere patiëntendossiers zijn opgenomen, beschikbaar gesteld aan datagebruikers. In dit geval maakt het datastation de data niet alleen toegankelijk op basis van toegangsregels, maar stelt het deze ook beschikbaar voor het algoritme van de datagebruiker. Dit conform de eisen die gelden voor het beschikbaar stellen van data voor secundair gebruik, waaronder pseudonimisering. De toepassing van de datagebruiker wordt met andere woorden op het datastation uitgevoerd. Bij primair gebruik is dat nooit het geval. 

Daarnaast kan het datastation voorzien in het transport van data, bijvoorbeeld in situaties van datapooling, waarbij data wordt samengebracht in een beveiligde verwerkingsomgeving van de HDAB of van een betrouwbare datahouder. Omdat bij secundair gebruik wordt gewerkt met grote datasets, zijn voor het transport andere standaarden nodig dan bij primair gebruik.

In de bovenstaande tekst zijn patiëntendossiers als voorbeeld gebruikt. Het secundair gebruik is uiteraard breder en omvat meer dan alleen patiëntendossiers. Ook dat is een verschil met het primair gebruik van data. 

## Een datastation per dataleverancier

Een belangrijk uitgangspunt is dat de data onder de verwerkingsverantwoordelijkheid van de dataleverancier blijft. Deze dataleverancier is een datahouder die op grond van de EHDS verplicht is data beschikbaar te stellen en niet is uitgezonderd op basis van artikel 50. Iedere dataleverancier beschikt daarom in principe over een eigen datastation.

Uitgangspunt is dat dataleveranciers een proces doorlopen om deelnemer te worden aan de dataspace en een deelnemersovereenkomst ondertekenen waarin zij zich verbinden aan de afspraken van de dataspace voor secundair gebruik. De HDAB is verantwoordelijk voor zowel het maken als het handhaven van de afspraken.

!!! info "Afsprakenstelsels en dataspaces"

    In de tekst wordt zowel de term afsprakenstelsel als dataspace gebruikt. Een dataspace definiëren we als een afsprakenstelsel voor databeschikbaarheid, het maakt een betrouwbare gegenvensuitwisseling mogelijk tussen deelnemers. Afsprakenstelsels kunnen met andere woorden over vele onderwerpen gaan, dataspaces beperken het onderwerp tot gegevensuitwisseling en databeschikbaarheid. 

## Model met dienstverleners

In de praktijk zijn dataleveranciers niet altijd in staat om zelfstandig een datastation te implementeren. Zij beschikken daarvoor vaak niet over de benodigde mensen, processen en technische mogelijkheden. Dit geldt overigens ook regelmatig voor datagebruikers.

Om dit op te vangen, gaat de architectuur uit van een zogenoemd four-corner model. Hierbij treden dienstverleners namens dataleveranciers en datagebruikers op en sluiten zij deze partijen aan op de dataspace voor secundair gebruik. Door deze aansluiting worden dataleveranciers en datagebruikers middels een knooppunt opgenomen in het netwerk van deelnemers. Bij het primaire gebruik van data vervullen organisaties vaak beide rollen: dataleverancier en datagebruiker. Bij secundair gebruik zijn deze rollen vaker gescheiden, omdat onderzoekers en overheidsinstanties bijvoorbeeld uitsluitend als datagebruiker optreden en geen dataleverancier zijn.

Het four-corner model wordt toegepast in vrijwel alle moderne afsprakenstelsels. Met alle deelnemers worden afspraken gemaakt over hun rol, taken en verantwoordelijkheden binnen het stelsel. 

![](datastation-4corner.drawio.svg)

///caption
**Figuur 1.** Four-corner model, met dienstverleners voor dataleveranciers en gebruikers.
///

Niet iedere zorgaanbieder hoeft zelf een dienstverlener te contracteren. In het huidige landschap zien we dat veel zorgaanbieders samenwerken binnen regionale samenwerkingsorganisaties om gezamenlijk een dienstverlener te contracteren voor de aansluiting op een dataspace. Ook binnen deze constructie blijft het uitgangspunt gehandhaafd dat iedere dataleverancier beschikt over een eigen datastation. De dienstverlener host deze voor de dataleverancier.

In het four-corner model kan een dienstverlener knooppunten hosten voor zowel dataleveranciers als voor datagebruikers. Voor dataleveranciers richt de dienstverlener een datastation in; voor datagebruikers een processing hub. 

![](datastation-netwerk.drawio.svg)

///caption
**Figuur 2.** Netwerk van datastations en processing hub
///

Binnen het secundaire gebruik is de inrichting van een processing hub voorbehouden aan de HDAB en aan betrouwbare datahouders. Vanuit elke processing hub kan zowel een goedgekeurd dataverzoek als (federatief) een algoritme worden uitgevoerd op basis van een datavergunning. In het bovenstaande figuur is alleen de processing hub van de HDAB weergegeven. In werkelijkheid kunnen er meerdere processing hubs bestaan, een hub per betrouwbare datahouder.