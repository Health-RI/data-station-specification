---
title: Discussie
---

# 7. Discussie

Dit hoofdstuk gaat in op de twee centrale onderzoeksvragen van dit specificatiedocument:

> Kan een eenduidige functionele en technische specificatie gegeven worden van hybride BVO gebaseerd op datastations en een processing hub, die consistent is met bestaande referentie-architecturen?

> Op welke manier zouden datastations gestandaardiseerd kunnen worden om te komen tot maximale interoperabiliteit van hybride BVOs?

De voorgaande hoofdstukken hebben aangetoond dat een datastation geen op zichzelf staand systeem is, maar een hoeksteen van een bredere infrastructuur voor secundair gebruik. De discussie richt zich op vier samenhangende thema's die nog om nadere uitwerking vragen.

**Centraal versus decentraal** (§7.1) laat zien dat een hybride architectuur de meest haalbare oplossing is: federated processing daar waar de usecase het toelaat, gecombineerd met de mogelijkheid om data door te zetten naar een centrale BVO. De formele status van een datastation als decentrale BVO onder de EHDS is echter nog onvoldoende uitgewerkt, en er ontbreekt een gecertificeerd _trust_-mechanisme voor geautomatiseerde controle van vergunningen in een federatief netwerk.

**Primair versus secundair gebruik** (§7.2) toont aan dat de overeenkomsten tussen datastations voor primair en secundair gebruik groot zijn — vergelijkbare ontwerpprincipes, domein van de datahouder, ondersteuning van meerdere informatiemodellen — maar dat de grondslagen voor toegangscontrole, de vereiste latency en de noodzaak van lokale rekenkapaciteit fundamenteel verschillen. De adapter-functie die klinische FHIR-data en analytische formaten vanuit dezelfde datalaag kan bedienen, is daarin een cruciale bouwsteen.

**Health data permits versus requests** (§7.3) beschrijft hoe de EHDS een onderscheid maakt tussen vergunningen (permits) en gegevensverzoeken (requests), met de HDAB als centrale uitgevende instantie. Voor een decentraal netwerk van datastations betekent dit dat het autorisatiemechanisme het digitale permit van de HDAB moet kunnen vertalen naar lokale toegangsrechten — een technisch vraagstuk waarvoor nog geen universele standaard bestaat. De rol van _trusted data holders_ biedt hier perspectief: organisaties zoals DHD, Zorginstituut, IKNL en Vektis kunnen als vertrouwde tussenschakel optreden.

**Relatie tot dataspace-initiatieven** (§7.4) laat zien dat EHDS en generieke data spaces (IDSA, Eclipse Dataspace, Gaia-X) gedeelde architectuurprincipes kennen — federatie, datasouvereiniteit, metadata-gedreven ontwerp — maar op cruciale punten uiteenlopen: het EHDS-autorisatiemodel is centraal en wettelijk verankerd, terwijl generieke data spaces uitgaan van peer-to-peer onderhandeling. Volledige interoperabiliteit is onwaarschijnlijk; convergentie op de lagen van metadata-standaarden (DCAT/HealthDCAT-AP), identiteit en authenticatie (eIDAS, Digital Identity Wallets) en generieke bronsysteeminterfaces biedt de meest realistische weg vooruit.

**Voorstel ontwikkelagenda** (§7.5) bundelt de voornaamste openstaande punten: output-controle voor deep learning-modellen, _smart contracts_ als extra waarborg voor geautomatiseerde vergunningscontrole, en de uitbreiding van datastations met voorzieningen voor medische beelden (PACS, DICOM-service, computatieservice).

De overkoepelende conclusie is dat eenheid van techniek al grotendeels haalbaar is — de grote TEHDAS2-vereisten zijn al gerealiseerd in KIK-V en PLUGIN — maar dat eenheid van taal (semantische interoperabiliteit) meer tijd vraagt. De composable data stack biedt hiervoor de meest pragmatische basis: gestandaardiseerde ondersteuning van datatransformaties, met bestaande en nieuwe mappings in SSSOM + SEMAPV als bouwstenen voor toenemende semantische uitwisselbaarheid.
