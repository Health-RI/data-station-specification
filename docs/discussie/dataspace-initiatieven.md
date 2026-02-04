# 7.4. Relatie tot dataspace initiatieven

Datastations voor secundair gebruik van gezondheidsgegevens binnen de European Health Data Space (EHDS) ontstaan niet in isolatie. Diverse generieke data space initiatieven, zoals onder andere de [International Data Spaces Association (IDSA)](https://internationaldataspaces.org/), de [Eclipse Dataspace Working Group](https://dataspace.eclipse.org/) en [Gaia-X](https://gaia-x.eu/), richten zich eveneens op interoperabele gegevensuitwisseling. Deze pagina verkent wat datastations/EHDS delen met deze generieke frameworks en waar zij verschillen.

Op abstract niveau delen datastations en EHDS tal van architectuurprincipes met generieke data spaces. Federatie, data soevereiniteit, metadata-gedreven ontwerp en authorisatie vormen de gemeenschappelijke basis. Waar de generieke initiatieven en architecturen zich richten op brede toepasbaarheid, is de EHDS specifiek ontworpen voor de eisen van gezondheidsgegevens.

Op detail niveau bestaan echter significante verschillen, die er voor zorgen dat automatische interoperabiliteit niet vanzelf ontstaat. Hieronder worden de belangrijkste overeenkomsten en verschillen besproken.

## 7.4.1. Het autorisatiemodel

Een fundamenteel verschil schuilt in hoe beslissingen over gegevenstoegang worden genomen. In de EHDS speelt de Health Data Access Body (HDAB) een centrale rol: elke EU-lidstaat wijst een HDAB aan die datapermits afgeeft, weigert en monitort. Deze centralisering is bewust. Zij zorgt voor uniforme toetsing van dataaanvragen tegen sectorspecifieke criteria en publiek belang, en biedt handhavingsmacht via digitale health authorities.

Generieke data spaces volgen een ander patroon: peer-to-peer onderhandeling. Autonome participanten onderhandelen rechtstreeks met elkaar over datagebruik. Trust frameworks verzorgen identificatie en de mogelijkheid tot opbouwen van vertrouwen, maar deze zullen geen autorisatie uitvoeren. Datahouders bepalen zelf hun beleid op basis van de informatie die beschikbaar is of zij een dataverzoek honoreren.

Dit verschil is niet triviaal. Het EHDS-model biedt sterkere bescherming tegen misbruik van gevoelige gezondheidsdata en waarborgt dat publieke belangen niet onverantwoord worden opgeofferd aan marktmechanismen. Het generieke model biedt meer flexibiliteit en schaalt gemakkelijker over sectoren.

In de implementatie van generieke data spaces kan er gekozen worden om meer verantwoordelijkheid bij een centrale partij te leggen, maar dit is een ontwerpkeuze die expliciet gemaakt moet worden. Het is niet automatisch onderdeel van de generieke frameworks.

## 7.4.2. Domeinspecificiteit vs. Generieke Aanpak

EHDS en datastations zijn ontworpen voor elektronische gezondheidsgegevens, met al wat daarvan meebrengt. Zij definiëren prioritaire gegevenscategorieën (patiëntendossiers, elektronische recepten, medische beelden) met gefaseerde implementatie. Zij stellen specifieke eisen aan BVOs, meer dan generieke data spaces. Zij maken gebruik van HealthDCAT-AP, een sectorspecifieke extensie op DCAT.

Generieke initiatieven zijn sector-agnostisch en ontworpen voor hergebruik. Dit maakt hen flexibel maar minder gericht. In specifieke data spaces kunnen domeinspecifieke wijzigingen gemaakt worden, maar dit zal ten koste gaan van interoperabiliteit met andere sectoren. Eisen zoals binnen de EHDS aan de BVOs gestelt worden, zullen meer een onderdeel zijn van de regels die de data houders en gebruikers overeenkomen, dan van de onderliggende architectuur.

## 7.4.3. Juridisch en Governance Kader

EHDS is EU-wetgeving, rechtstreeks bindend in alle lidstaten. Wat zorgt voor verplichtingen voor datahouders en handhavingsmacht voor autoriteiten. Dit garandeert een uniform speelveld en zorgt voor een erg strakke governance-structuur, waarbij er weinig ruimte is voor afwijkingen.

De generieke initiatieven zijn veelal vormgegeven als verenigingen en stichtingen, waar partijen aan deel kunnen nemen. Maar ook specifieke implementaties van data spaces zijn vaak gebaseerd op vrijwillige samenwerking en contracten tussen partijen. Dit betekent dat de juridische afdwingbaarheid en governance-structuren kunnen variëren tussen verschillende data spaces.

## 7.4.4. Interoperabiliteit

Op het niveau van interoperabiliteit zijn er zowel overeenkomsten als verschillen. Beide benaderingen maken gebruik van metadata-standaarden zoals DCAT om datasets te beschrijven. Binnen de EHDS zijn er uitbreidingen zoals HealthDCAT-AP om gezondheidsspecifieke metadata te ondersteunen. Dit kan ook in generieke data spaces worden toegepast en vereist minimale inspanning om compatibiliteit te waarborgen. 

Op het gebied van autorisatie, zoals eerder benoemd, zijn grotere verschillen aanwezig. EHDS gebruikt een centraal uitgegeven datapermit model, terwijl generieke data spaces peer-to-peer contractonderhandelingen hanteren. Het vertalen van een EHDS datapermit naar een ODRL policy (gebruikt in generieke data spaces) is mogelijk, maar vereist expliciete mapping en begrip van de onderliggende semantiek. De vertaling van ODRL policies naar EHDS datapermits is complexer, gezien de generiekere insteek van ODRL. Ook zullen systemen ontwikkeld voor EHDS en generieke data spaces verschillende interfaces en workflows hebben voor het aanvragen, uitgeven en handhaven van toegang.

Voor de daadwerkelijke data uitwisseling, ofwel uitwisselen van brondata of het uitvoeren van berekeningen in een BVO, zijn er ook verschillen die niet gemakkelijk te overbruggen zijn. Gezien de afhankelijkheid van de autorisatiemodellen, zullen de protocollen en orchestratie van data uitwisseling verschillen.

## 7.4.5. Co-existentie

Volledig onderling compatibele systemen zijn onwaarschijnlijk. Convergentie op bepaalde lagen is wel mogelijk, zodat zoveel mogelijk dezelfde concepten gebruikt worden. Op deze manier kan de achterliggende organisatie vergelijkbaar opgezet worden, met daaraan gekoppeld verschillende implementaties voor verschillende doeleinden.

Deze convergentie kan gezocht worden op de volgende gebieden:

1. Gebruik van gemeenschappelijke metadata standaarden (DCAT, HealthDCAT-AP) om datasets te beschrijven. Zodat verschillende systemen elkaars metadata kunnen interpreteren en kunnen bepalen of uitwisseling mogelijk is.
2. Gebruik van gemeenschappelijke identificatie en authenticatiemechanismen (bijv. middels eIDAS, EU Digital Identity Wallets en EU Business Wallets) om entiteiten in beide systemen te identificeren.
3. Voorkom lock-in door de interfaces tussen bronsystemen en datastations/data spaces zo generiek mogelijk te houden. Zodat bronsystemen met meerdere architecturen gebruikt kunnen worden.
