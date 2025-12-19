# Laag 3 van de zandloper

De derde laag van het zandlopermodel bestaat uit een netwerk van datastations. Een belangrijk uitgangspunt is dat de data onder de verwerkingsverantwoordelijkheid van de dataleverancier blijft. Deze dataleverancier is een datahouder die op grond van de EHDS verplicht is data beschikbaar te stellen en niet is uitgezonderd op basis van artikel 50. Iedere dataleverancier beschikt daarom in principe over een eigen datastation.

In de praktijk zijn zorgaanbieders echter niet altijd in staat om zelfstandig een datastation te implementeren. Zij beschikken daarvoor vaak niet over de benodigde mensen, processen en technische mogelijkheden. Dit geldt overigens ook regelmatig voor datagebruikers.

Om dit op te vangen, gaat de architectuur uit van een zogenoemd four-corner model. Hierbij treden dienstverleners namens dataleveranciers en datagebruikers op en sluiten zij deze partijen aan op de dataspace voor secundair gebruik. Door deze aansluiting worden dataleveranciers en datagebruikers middels een knooppunt opgenomen in het netwerk van deelnemers. Bij het primaire gebruik van data vervullen organisaties vaak beide rollen: dataleverancier en datagebruiker. Bij secundair gebruik zijn deze rollen vaker gescheiden, omdat onderzoekers en overheidsinstanties bijvoorbeeld uitsluitend als datagebruiker optreden en geen dataleverancier zijn.

Het four-corner model wordt toegepast in vrijwel alle moderne afsprakenstelsels. Met alle deelnemers worden afspraken gemaakt over hun rol, taken en verantwoordelijkheden binnen het stelsel. Uitgangspunt is dat alle partijen een proces doorlopen om deelnemer te worden aan het afsprakenstelsel en een deelnemersovereenkomst ondertekenen waarin zij zich verbinden aan de afspraken van de dataspace voor secundair gebruik.

![](4corner.drawio.svg)

///caption
**Figuur 1.** Four-corner model, met dienstverleners voor dataleveranciers en gebruikers.
///

Niet iedere zorgaanbieder hoeft zelf een dienstverlener te contracteren. In het huidige landschap zien we dat veel zorgaanbieders samenwerken binnen regionale samenwerkingsorganisaties om gezamenlijk een dienstverlener te contracteren voor de aansluiting op een dataspace. Een dataspace definieren we overigens als een afsprakenstelsel voor databeschikbaarheid, het maakt een betrouwbare gegenvensuitwisseling mogelijk tussen deelnemers. Afsprakenstelsels kunnen met andere woorden over vele onderwerpen gaan, dataspaces beperken het onderwerp tot gegevensuitwisseling en databeschikbaarheid.

In het four-corner model kan een dienstverlener knooppunten hosten voor zowel dataleveranciers als voor datagebruikers. Voor dataleveranciers richt de dienstverlener een datastation in; voor datagebruikers een processing hub. Binnen het secundaire gebruik is de inrichting van een processing hub echter voorbehouden aan de Health Data Access Body (HDAB) en aan betrouwbare datahouders. Vanuit iedere processing hub kan zowel een dataverzoek federatief worden uitgevoerd als een algoritme gefedereerd of centraal worden uitgevoerd.

![](datastation-netwerk.drawio.svg)

///caption
**Figuur 2.** Netwerk van datastations en processing hub
///
