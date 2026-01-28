# Infrastructuur

Onderscheid wordt gemaakt tussen *trainingsziekenhuizen* en *inferentieziekenhuizen*. Bij inferentieziekenhuizen wordt wel gebruik gemaakt van het AI-model, maar hier vindt geen training plaats. Deze ziekenhuizen leveren dus geen data waarmee het model wordt ontwikkeld. In dit geval zijn er lichtere systeemeisen voor het datastation.

Het datastation voor PLUGIN is te realiseren als een standaard Linux server. Dit mag ook een VM zijn. Hierop wordt een Vantage6 Node geinstalleerd, een aantal gebruikersaccounts aangemaakt en een standaard folderstructuur ingesteld. Zowel de Node zelf als de daarop uitgevoerde algoritmen zoals de PLUGIN-ML pipeline worden gedraaid binnen Docker.

## Hard- & software

PLUGIN gaat uit van een Linux server als de fysieke machine waarop alle applicatie componenten draaien. Dit mag ook een virtual machine zijn. De belangrijkste voorwaarden zijn dat de machine:

* in staat is om [Docker](https://www.docker.com) te draaien.<br>**NB:** Om de PLUGIN infrastructuur te gebruiken is het noodzakelijk om Docker Engine en niet Docker Desktop te installeren. Docker desktop maakt gebruik van een virtuele machine die niet compatibel is met de PLUGIN infrastructuur.
* toegang heeft tot de data (zie ook [hieronder](#technisch-vlak-target))

De specificaties van de Linux server zijn als volgt:

* \>= 16 cores, x86/x64 CPU
* \>= 56 GB CPU RAM
* \>= 360 GB SSD
* virtualization enabled
* GPU (optioneel, maar aanbevolen):
    - [CUDA compatible](https://developer.nvidia.com/cuda-gpus) NVIDIA kaart
    - 16 GB GPU RAM

Indien voor (iets) lagere specificaties van CPU of RAM gekozen wordt, zal het systeem nog steeds werken, maar duren berekeningen mogelijk wat langer. Qua SSD-opslag wordt minder capaciteit afgeraden. Of een **GPU** nodig is, is afhankelijk de use cases waaraan deelgenomen wordt. In het algemeen is het zo een GPU vereist is als datastation deelnemen in het trainen van algoritmes. Als een ziekenhuis alleen een getraind model wil gebruiken op haar eigen data (_inference_), dan is dat mogelijk zonder GPU.

## Netwerk

* \>= 100Mbit ethernet
* Port 443/TCP (https) open voor _uitgaand_ verkeer naar ...
    * DHD
        * vantage6 server: [https://plugin.dhd.nl](https://plugin.dhd.nl)
        * Docker registry: [https://plugindhd.blob.core.windows.net](https://plugindhd.blob.core.windows.net)
        * Docker registry (voor updates van vantage6): [https://harbor2.vantage6.ai](https://harbor2.vantage6.ai)
        * blob storage: [https://plugindhd.azurecr.io](https://plugindhd.azurecr.io)
    * IKNL
        * vantage6 server: [https://cotopaxi.vantage6.ai](https://cotopaxi.vantage6.ai)
        * Docker registry: [https://harbor2.vantage6.ai](https://harbor2.vantage6.ai)
    * [websites nodig voor installatie/upgrade Python3, Docker, etc.]

## Toegang tot data

## Beschikbaar stellen van data
Om federatieve toepassingen mogelijk te maken, is het belangrijk dat iedere deelnemer zijn/haar klinische data op dezelfde manier aan het platform aanbiedt. Naast eerder genoemde syntactische en semantische interoperabiliteit, is het noodzakelijk op ook technische standaarden af te spreken. Indien bijvoorbeeld wordt gekozen voor FHIR als informatiestandaard, dan kan de technische interface op verschillende manieren worden geimplementeer:


1. Via een FHIR-server en de bijbehorende [REST API](https://hl7.org/fhir/http.html), zoals [HAPI](https://hapifhir.io/hapi-fhir/) of [Firely](https://fire.ly/products/firely-server/) Server. Voor efficiente data-overdracht, zou gebruik gemaakt kunnen worden van de [bulk data API](https://hl7.org/fhir/uv/bulkdata/) en [nd-json](https://hl7.org/fhir/nd-json.html).
2. Via een relationele database, zoals [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2022) of [PostgreSQL](https://www.postgresql.org), waarbij de FHIR resources ofwerl i) tabulair worden opgeslagen (met ieder attribuut van een resource in een aparte kolom), ofwerl als document (in een kolom van type JSON-B).
3. Via een data lake / blob storage, waarbij de resources als [nd-json](https://hl7.org/fhir/nd-json.html) bestanden worden opgeslagen en worden ontsloten via een (in process) database management systeem (zoals [DuckDB](https://duckdb.org)).

Ongetwijfeld zijn er nog andere opties mogelijk.

De eerste optie heeft als voordeel dat andere applicaties binnen het ziekenhuis gebruik kunnen maken van dezelfde server. Bijvoorbeeld voor Clinical Decision Support. De tweede optie sluit goed aan bij de technology stack die al in veel ziekenhuizen beschikbaar is, en wordt reeds toegepast door het LUMC, ErasmusMC en UMCUtrecht. De derde optie is waarschijnlijk (financieel) het voordeligst, omdat alleen data-opslag nodig is; een database of app server is niet noodzakelijk.

