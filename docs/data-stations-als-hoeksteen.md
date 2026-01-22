# 1.2. Datastations als hoeksteen voor een decentraal netwerk van BVOs

## 1.2.1. Datastations en het zandloper model
Het concept van **datastations** staat centraal in dit document dat een architectuur beschrijft van een landelijk dekkend decentraal netwerk van BVOs ten behoeve van secundair gebruik. Het concept van datastations kent vandaag de dag veel verschillende verschijningsvormen:

- Het originele concept van PHT omschrijft datastations in de context van federated learning[@choudhury2025advancing], wat vervolgens is gegeneraliseerd om andere vormen van gefedereerde berekeningen te omvatten[@boninodasilvasantos2022personal].
- De FAIR principes zijn uitgewerkt in het concept van een [FAIR data point](https://specs.fairdatapoint.org/fdp-specs-v1.2.html), zijnde een datastation gevuld met FAIR metadata dat is bedoeld als een gefedereerde oplossing voor een data catalogus.
- Het [Programma KIK-V](https://www.kik-v.nl/starten-met-kik-v) van het Zorginstituut heeft het concept van datastations geoperationaliseerd voor geautomatiseerde informatie-uitwisseling voor de VVT-sector, wat een vorm is van gefedereerde analyse.
- Datastations in de context van primair gebruik zijn conceptueel hetzelfde als de [Shared Health Record](https://guides.ohie.org/arch-spec/openhie-component-specifications-1/openhie-shared-health-record-shr) component zoals gespecificeerd in de [OpenHIE architectuur](https://guides.ohie.org/arch-spec). RSO Zuid-Limburg werkt aan een primair datastation op basis van openEHR[^1], een oplossingsrichting die ook in Scandinavië[@pohjonen2022norway] en Slovenië[@bajric2023building] wordt gebruikt. Hoewel datastations voor primair gebruik veel overeenkomsten vertonen met datastations voor secundair gebruik, zijn er ook belangrijke verschillen in de technische kenmerken tussen deze systemen. Deze verschillen zitten bijvoorbeeld in snelheid (_latency_) en volume waarmee data in het station kan worden benaderd: voor primair gebruik moeten snel enkelvoudige records kunnen worden opgehaald, terwijl voor secundair gebruik grotere datasets bevraagd kunnen worden en hogere wachttijden acceptabel zijn. 

Ondanks de vele verschijningsvormen zien we meer overeenkomsten dan verschillen in bestaande conceptualisaties en implementaties van datastations. Sterker nog, verschillende studies wijzen op de potentie die datastations bieden om tot betere standaardisatie en interoperabiliteit te komen. Het succes van het internet en andere technologieën met een sterk netwerkeffect, zoals het Linux/Unix operating systeem, heeft ons geleerd dat standaardisatie een groot goed is, maar dat we spaarzaam moeten zijn in het opleggen van standaarden. Dit concept is beschreven met een zandloper als metafoor[@estrin2010health;@beck2019hourglass] (figuur 2) en gaat uit van het principe van maximale vrijheid voor toepassingen aan de bovenkant van de zandloper (het domein van de datagebruiker) èn maximale vrijheid voor de onderliggende basisinfrastructuur aan de onderkant (het domein van de datahouder). Ondanks deze vrijheid kan een hoge mate van interoperabiliteit worden gerealiseerd door het hart van de zandloper (het datastation) in hoge mate te standaardiseren en uniformeren. Schultes (2023)[@schultes2023fair] heeft de principes van het zandloper model gecombineerd met de FAIR principes om tot een vijflagenmodel te komen.

![](fair-hourglass.png)


/// caption
**Figuur 2.** Het zandloper model als denkraam voor data interoperabiliteit. Bron: Schultes (2023).[@schultes2023fair]
///

??? abstract "FAIR principes"

    De internationale FAIR-principes zijn richtlijnen voor de manier van beschrijven, opslag en publicatie van data. FAIR is een acroniem voor:

    - **F**indable - vindbaar 
    - **A**ccessible - toegankelijk
    - **I**nteroperable - uitwisselbaar
    - **R**eusable - herbruikbaar

    Alhoewel de principes oorspronkelijk zijn geformuleerd voor wetenschappelijke data, worden ze ook toegepast voor secundair gebruik van data die routematig wordt vastgelegd in bijvoorbeeld het reguliere zorgproces.

## 1.2.2. De vijf lagen van het zandloper model als denkraam

Het zandloper model gaat uit van vijf lagen die de data moeten laten stromen vanaf het eerste moment dat ze worden vastgelegd door de data houder (laag 1) tot en met het uiteindelijke secundair gebruik door de data gebruiker (laag 5).

### 1.2.2.1. Het FAIRificatie proces in de eerste twee lagen

In **laag 1** wordt de data gecreëerd. Diegene die verantwoordelijk is voor het vastleggen van de data heeft hierin maximale vrijheid. Het vastleggen van de data kan gebeuren door een onderzoeker, die handmatig data verzameld, codeert en vastlegd als een onderzoeksdataset, maar kan ook worden gedaan in het primaire proces van de zorg waarbij allerlei zorgverleners in verschillende zorginformatiesystemen data vastleggen.

In **laag 2** wordt een begin gemaakt met het standaardiseren van de data. Het is een soort trechter waar met gebruik van allerlei databewerkings tools de data en metadata worden omgezet naar gestructureerde formats die machine-leesbaar zijn en gebruik maken van gestandaardiseerde terminologie en informatieschemas.

### 1.2.2.2. Het datastation in het hart van de zandloper

**Laag 3 is het hart van de zandloper** en fungeert als een brug tussen de twee onderste en twee bovenste lagen. In deze laag worden de data en metadata (1) klaargezet voor gebruik en FAIRificatie proces en (2) verbonden aan het netwerk van beveiligde verwerkingsomgevingen. Deze laag is het meest cruciale om interoperabiliteit te realiseren. Daarvoor wordt een set van minimale, open en technologie-neutrale standaarden gedefinieert. Het idee van een datastation sluit aan bij het concept van data producten in de DSSC.


??? abstract "Data product"
    Primair gebruik heeft betrekking op de directe zorgverlening aan een patiënt, terwijl secundair gebruik betrekking heeft op het hergebruik van gegevens voor onder andere onderzoek, beleid en innovatie.
    
    Bepaalde gegevens voor primair gebruik kunnen worden samengebracht in een dataproduct, zoals de patiëntsamenvatting. Deze bevat onder meer de essentiële patiëntgegevens, recepten en verstrekkingen. Een dataproduct wordt hierbij gedefinieerd als een concrete dataset die kan worden gedeeld tussen zorgverleners, systemen en instellingen. Ook voor secundair gebruik kunnen datasets worden samengesteld als dataproduct, bijvoorbeeld in OMOP-formaat.
    
    Elk dataproduct bevat, naast de data zelf, ook metadata. Deze metadata beschrijven onder andere de structuur van de data, de inhoudelijke eisen waaraan de data voldoet, en verwijzingen naar de betekenis van de data (vastgelegd in een ontologie of domeinmodel). Daarnaast legt een dataproduct vast aan welke regels de data gebruiker moet voldoen voor toegang tot de data: hoe het mag worden gebruikt en welke beleidsregels van toepassing zijn voor toegang.

    ![Data product](./assets/data-product.png)


### 1.2.2.3. FAIR orchestratie

In **laag 4** wordt het datastation opgenomen in een netwerk om de data te verwerken en te verbruiken. Denk hierbij aan generieke voorzieningen zoals een catalogus en zoekfunctionaliteit (welke datastations hebben welke data?), het integreren wat data uit verschillende datastations en het uitvoeren van allerlei berekeningen op de data.

In **laag 5** wordt aan de data gebruiker maximale vrijheid gegeven om allerlei diensten af te nemen en/of analyses te doen.

[^1]: Zie deze [webinar](https://www.youtube.com/watch?v=jT5UTLRX5VQ) van 23 januari 2025
