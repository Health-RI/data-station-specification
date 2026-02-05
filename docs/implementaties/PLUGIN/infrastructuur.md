# Infrastructuur

De PLUGIN infrastructuur bestaat uit centrale en decentrale componenten die gezamelijk het federatieve platform vormen. Als orkestratie en communicatie laag tussen de centrale en decentrale maakt PLUGIN gebruik van vantage6. Vantage6 is een open-source python applicatie voor het opzetten van een federatief netwerk en het uitvoeren van gecontainerizeerde opdrachten op decentrale data stations. De centrale vantage6 server coördineert de communicatie en uitvoering van opdrachten, terwijl de vantage6 nodes op de data stations verantwoordelijk zijn voor het ontvangen en uitvoeren van opdrachten.

## Centrale componenten

In het hart van de PLUGIN infrastructuur bevindt zich een centrale vantage6 server. Deze server maakt het mogelijk om opdrachten via een webinterface of client klaar te zetten voor de data stations. De centrale vantage6 server bestaat uit de volgende onderdelen:

- De centrale vantage6 server applicatie, die draait binnen een Docker container.
- Een database (PostgreSQL) voor het opslaan van metadata over gebruikers, organisaties, opdrachten, etc.
- Een UI (webinterface) voor het beheren van gebruikers, organisaties, data stations en opdrachten.
- Eventueel een large file storage (blob storage) voor het opslaan van opdracht resultaten voor efficiente overdracht.

De centrale vantage6 server heeft als hoofddoel de authenticatie, autorisatie en coördinatie van opdrachten naar de decentrale data stations.

Naast de centrale server is er een of meerdere centrale Docker registries nodig voor het opslaan van de algoritme containers die worden uitgevoerd op de data stations. De toegang tot deze wordt ingesteld bij de data stations maar via een centrale algoritme registry kan ook centraal de toegang tot bepaalde algoritme containers worden geregeld.

## Decentrale componenten

De decentrale componenten binnen een PLUGIN infrastructuur bestaan uit de eerder genoemde componenten in het applicatielaag en kunnen worden samengevat in de vantage6 node, PLUGIN-Lake en algoritme containers.

### Vantage6 Node

De vantage6 node is de poort naar het federatieve netwerk en de locale orkestratie laag binnen het datastation. De node bevraagt de centrale vantage6 server en ontvangt opdrachten die uitgevoerd moeten worden als gecontainerizeerde applicaties. De vantage6 node zet vervolgens een tijdelijk netwerk op tussen de beschikbare data bronnen en de algoritme container. Na uitvoering van de opdracht, worden de resultaten via de node teruggestuurd naar de centrale vantage6 server en de algoritme container opgeruimd.

### PLUGIN-Lake

PLUGIN-Lake staat tussen de beschikbare data bronnen en de vantage6 node in. PLUGIN-Lake zorgt voor een uniforme toegang tot de data bronnen en eventuele data transformaties die nodig zijn om de data op de gewenste wijze aan te bieden aan de algoritme container.

### Algoritme container

Een algoritme container bevat de opdracht specifieke code die nodig is om een bepaalde taak uit te voeren. De node haalt de container op uit de centrale Docker Registry en start de container op binnen een tijdelijk netwerk. De algoritme container kan vervolgens alleen communiceren met de data bronnen en services binnen een datastation die beschikbaar zijn gesteld via de vantage6 node.

## Server eisen voor datastation

Om deel te kunnen nemen aan het PLUGIN platform worden systeemeisen gesteld aan het datastation binnen een deelnemende organisatie. Elke deelnemende organisatie dient een eigen machine (fysiek of virtueel) beschikbaar te stellen waarop de decentrale componenten van het PLUGIN platform kunnen draaien.

## Systeemeisen

Om te stabiliteit en performance van het platform te waarborgen, stellen we de volgende minimale systeemeisen aan het datastation:

- **Linux besturingssysteem**: Door het intensieve gebruik van container technologie (Docker of kubernetes) is een Linux besturingssysteem vereist.
- **CPU 16 cores, x86/x64 CPU**: Voor het uitvoeren van de algoritmen is een multi-core CPU vereist.
- **RAM 64 GB**: Bij het werken met veel data of data intensieve algoritmes is voldoende RAM noodzakelijk.
- **SSD 360 GB**: Opslag van (meta)data
- *Optioneel: **NVIDIA GPU (≥ 16 GB VRAM)**: Bij het beschikbaar stellen van een datastation voor de ontwikkeling van AI-modellen is een nvidia compatibele GPU vereist.

## Netwerk eisen

Om te kunnen deelnemen aan de PLUGIN infrastructuur, is het noodzakelijk dat het datastation kan communiceren met de centrale vantage6 server. De volgende netwerk eisen worden gesteld:

- **100 Mbit/s ethernet**
- **Port 443/TCP open voor uitgaand verkeer**

De volgende endpoints moeten bereikbaar zijn vanuit het datastation:

- adres van de centrale vantage6 server(s) waar het datastation op aansluit
- Vantage6 docker registry
- Docker registries van de algoritme containers
- *Eventuele toegang tot repositories voor updates van software en dependencies*

## Software eisen

- **Docker**: Voor het draaien van de vantage6 node en de algoritme containers is Docker vereist.
- **Python 3.10**: Nodig voor het opzetten van een vantage6 node
- **vantage6**: Python package die vantage6 beschikbaar maakt als Command Line Interface (CLI)

De overige applicaties worden geinstalleerd als gecontainerizeerde applicaties. Om deze te beheren wordt er gebruik gemaakt van docker compose, kubernetes en eventueel linux native tools.

## Toegang tot data

Om interoperabiliteit te kunnen waarborgen binnen het PLUGIN platform, is het noodzakelijk dat de data op een gestandaardiseerde wijze beschikbaar wordt gesteld aan de algoritme containers. Om dit te realiseren, kiest PLUGIN voor FHIR als de informatiestandaard voor klinische data.

Alhoewel vantage6 de mogelijkheid biedt om de data bronnen direct te benaderen vanuit de algoritme container, wordt er binnen PLUGIN gekozen voor een tussenlaag: PLUGIN-Lake. PLUGIN-Lake zorgt voor een uniforme toegang tot de data bronnen en eventuele data transformaties die nodig zijn om de data op de gewenste wijze aan te bieden aan de algoritme container.

De data bronnen kunnen op verschillende manieren worden ontsloten binnen een datastation en dus PLUGIN-Lake. We maken hierbij onderscheid tussen de volgende bronnen:

- Lokale bestanden (CSV, JSON, XML, etc) die beschikbaar zijn op het datastation
- API's die toegang bieden tot de data (bijvoorbeeld REST API's)

Via PLUGIN-Lake (of vantage6 node) kunnen de verschillende data bronnen worden ontsloten en beschikbaar worden gesteld aan de algoritme container in het gewenste formaat (bijvoorbeeld als FHIR resources in nd-json formaat).

Enkele voorbeelden van data bronnen die binnen PLUGIN-Lake ontsloten kunnen worden:

- Een FHIR server (bijvoorbeeld HAPI of Firely)
- Een relationele database (bijvoorbeeld SQL Server of PostgreSQL)
- Object storage (bijvoorbeeld Azure Blob Storage of AWS S3)
- Lokale bestanden op de server zelf of een netwerk share


<!-- ## Beschikbaar stellen van data
Om federatieve toepassingen mogelijk te maken, is het belangrijk dat iedere deelnemer zijn/haar klinische data op dezelfde manier aan het platform aanbiedt. Naast eerder genoemde syntactische en semantische interoperabiliteit, is het noodzakelijk op ook technische standaarden af te spreken. Indien bijvoorbeeld wordt gekozen voor FHIR als informatiestandaard, dan kan de technische interface op verschillende manieren worden geimplementeer:


1. Via een FHIR-server en de bijbehorende [REST API](https://hl7.org/fhir/http.html), zoals [HAPI](https://hapifhir.io/hapi-fhir/) of [Firely](https://fire.ly/products/firely-server/) Server. Voor efficiente data-overdracht, zou gebruik gemaakt kunnen worden van de [bulk data API](https://hl7.org/fhir/uv/bulkdata/) en [nd-json](https://hl7.org/fhir/nd-json.html).
2. Via een relationele database, zoals [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2022) of [PostgreSQL](https://www.postgresql.org), waarbij de FHIR resources ofwel i) tabulair worden opgeslagen (met ieder attribuut van een resource in een aparte kolom), ofwel als document (in een kolom van type JSON-B).
3. Via een data lake / blob storage, waarbij de resources als [nd-json](https://hl7.org/fhir/nd-json.html) bestanden worden opgeslagen en worden ontsloten via een (in process) database management systeem (zoals [DuckDB](https://duckdb.org)).

Ongetwijfeld zijn er nog andere opties mogelijk.

De eerste optie heeft als voordeel dat andere applicaties binnen het ziekenhuis gebruik kunnen maken van dezelfde server. Bijvoorbeeld voor Clinical Decision Support. De tweede optie sluit goed aan bij de technology stack die al in veel ziekenhuizen beschikbaar is, en wordt reeds toegepast door het LUMC, ErasmusMC en UMCUtrecht. De derde optie is waarschijnlijk (financieel) het voordeligst, omdat alleen data-opslag nodig is; een database of app server is niet noodzakelijk. -->

