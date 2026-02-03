# 5.2. Een datastation met de composable data stack

## 5.2.1. De principes van de composable data stack

Zoals eerder vastgesteld heeft het datastation als taak om datahouder specifieke data te convergeren naar betrouwbare en ontsluitbare informatie. Elk datastation opereert in een unieke organisatorische context met eigen systemen, compliance eisen en technische capaciteiten. Via een lakehouse architectuur behoudt een datastation de flexibiliteit om diverse data beschikbaar te maken en te verwerken, maar wordt via metadata management en open standaarden een generieke minimale standaard afgedwongen. De gestandaardiseerde metadata laag zorgt voor de benodigde centrale coördinatie zonder lokale autonomie in te perken. Deze metadata laag functioneert als de gemeenschappelijke taal als basis voor federatieve samenwerking en interoperabiliteit.

!!! abstract "Basisprincipes van de composable data stack"
    
    De basis van een composable architectuur rust op drie pijlers:

    1. **Modulariteit:** Componenten (bouwstenen) kunnen onafhankelijk van elkaar worden vervangen of geschaald.
    2. **Interoperabiliteit:** Dankzij open standaarden (zoals Apache Arrow en Parquet) kunnen verschillende systemen zonder kostbare conversies samenwerken.
    3. **Ontkoppeling:** De fysieke opslag (_storage_), de data verwerking (_compute_) en de schema-informatie (_catalog_) zijn strikt van elkaar gescheiden.

De ontkoppeling van functies is een van de belangrijkste ontwerpprincipes van het datatstation. Ten tijde van het schrijven van deze specificaties zijn er vanuit de data engineering werkveld bewezen technische componenten die gebruikt kunnen worden.

=== "Storage (opslag)"

    In traditionele systemen is data vaak opgeslagen in een eigen, gesloten formaat dat alleen door de bijbehorende database-engine gelezen kan worden. In de Composable Data Stack wordt de opslaglaag geagnostiseerd.

    * **Open bestandsformaten:** Data wordt opgeslagen in gestandaardiseerde kolomgeoriënteerde formaten zoals **Apache Parquet**. Dit maakt de data toegankelijk voor een breed scala aan tools zonder dat de data verplaatst of getransformeerd hoeft te worden.
    * **Lakehouses:** Door gebruik te maken van object storage (zoals S3 of Azure Blob) als centrale bron, fungeert de opslaglaag als een 'single source of truth' die onafhankelijk van de rekenkracht kan groeien.

=== "Compute (verwerking en analyse)"

    Door de ontkoppeling van opslag wordt de 'compute-laag' vervangbaar. Dit stelt organisaties in staat om verschillende gespecialiseerde engines te gebruiken op dezelfde dataset.

    * **Engine-Agnostische Verwerking:** Een organisatie kan SQL-queries uitvoeren met de ene engine (bijv. DuckDB of Trino), terwijl een data scientist tegelijkertijd machine learning-modellen traint met een andere tool (bijv. PyTorch), direct op dezelfde data.
    * **Efficiënte data-uitwisseling:** Om de snelheid tussen verschillende compute-engines te waarborgen, fungeert **Apache Arrow** als de *lingua franca* voor data in het geheugen. Dit minimaliseert de overhead van serialisatie en deserialisatie (het omzetten van dataformaten).

=== "Catalog (schema informatie)"

    De verbindende factor in een gedecentraliseerde stack is de metadatalaag. Zonder centrale metadata ontstaat er versnippering.

    * **Tabelformaten:** Technologieën zoals **Apache Iceberg** of Delta Lake voegen een abstractielaag toe bovenop de ruwe bestanden. Ze beheren metadata over welke bestanden bij welke tabel horen, ondersteunen transacties (ACID) en maken tijdreizen (time-travel) door data mogelijk.
    * **Catalogus:** De catalogus fungeert als de inventaris van de gehele stack. Het houdt bij waar de data staat, wie de eigenaar is en wat de structuur (schema) is. Dit is essentieel voor de vindbaarheid en governance, vergelijkbaar met de FAIR-principes (Findable, Accessible, Interoperable, Reusable).

    !!! warning "Catalog vs. metadata"

        De catalogus in de composable data stack refereert naar het information schema van de data. Hiervoor zullen open standaarden zoals Apache Iceberg en DuckLake worden gebruikt. Deze catalogus is anders dan de metadata catalogus die op DCAT is gebaseerd en als generieke functie is beschreven binnen het landelijk dekkend netwerk.

## 5.2.2. Declarative ETL data verwerkingsstraten

Een ander essentieel aspect van de composable data stack is het werken met zogenaamde declaratieve ETL verwerkingsstraten. In de traditionele data-engineering (imperatieve ETL) ligt de nadruk op *hoe* data verplaatst en getransformeerd wordt via complexe scripts. De verschuiving naar een **declaratieve aanpak** is principieel anders: de focus verschuift naar *wat* het eindresultaat moet zijn. Dit vormt de basis voor het betrouwbaar schalen van data-ecosystemen en het leveren van hoogwaardige data producten binnen decentrale netwerken en data spaces.

=== "Declarative ETL"
    
    Een declaratieve pipeline (gebaseerd op principes van de *Modern Data Stack* en *Functional Data Engineering*) beschrijft de gewenste eindsituatie van de data, in plaats van de specifieke stappen om daar te komen.

    * **Definitie boven Executie:** In plaats van een volgorde van scripts (bijv. "stap A, dan stap B"), definieert de ontwikkelaar de logica van de transformatie (bijv. via SQL of YAML). Het onderliggende systeem (zoals dbt, Dagster of Spark Declarative Pipelines) bepaalt de optimale volgorde, afhankelijkheden en benodigde rekenkracht. Deze aanpak maakt het mogelijk om de nieuwe informatiestandaarden zoals beschreven in [hoofdstuk 3](../informatie/index.md) op een efficiente manier te implementeren in de datastations.
    * **Idempotentie en Reproduceerbaarheid:** Omdat de uitkomst gedefinieerd is, kan een pipeline herhaaldelijk gedraaid worden met dezelfde input zonder onverwachte zijeffecten. Dit is cruciaal voor foutcorrectie en het historisch herberekenen van data.
    * **Self-Healing en Lineage:** Het systeem begrijpt de relaties tussen datasets automatisch. Als een bronbestand verandert, weet de declaratieve stack precies welke afgeleide tabellen bijgewerkt moeten worden.

=== "Data producten"

    De overstap naar declaratieve pipelines maakt het mogelijk om data niet langer als een bijproduct van een proces te zien, maar als een volwaardig **data product**. Een data product is een autonome, leesbare en direct bruikbare eenheid van informatie.

    * **Kwaliteitsgaranties (SLA's):** Een data product bevat niet alleen de rauwe gegevens, maar ook metadata over de kwaliteit, herkomst (lineage) en actualiteit.
    * **Eigenaarschap:** Door de logica declaratief vast te leggen, is het eenvoudiger om verantwoordelijkheid toe te wijzen aan de domeinexperts die de data het beste begrijpen.
    * **Consumptiegericht:** Een data product is ontworpen voor de eindgebruiker (bijv. een onderzoeker of analist) en is via standaard interfaces (zoals API's of open tabelformaten) direct toegankelijk zonder dat diepgaande kennis van de broncode nodig is.

    In de praktijk kan het dus zijn dat in één ETL verwerkingsstraat meerdere data producten worden gecreerd die beschikbaar worden gesteld voor secundair gebruik.

=== "Integratie in data spaces"

    In een **Data Space** (een federatief netwerk waarin organisaties veilig data uitwisselen) zijn data producten de centrale objecten van transactie. Declaratieve pipelines zijn hierbij de 'fabriek' die deze producten betrouwbaar produceert.

    * **Interoperabiliteit:** In een data space moeten verschillende partijen elkaars data begrijpen. Declaratieve definities dwingen het gebruik van gedeelde schema's en semantische standaarden af, wat essentieel is voor automatische integratie.
    * **Soevereiniteit en Governance:** Omdat de transformatielogica transparant en gedocumenteerd is (als code), kunnen beleidsregels voor toegang en privacy (bijv. anonimisering) direct in de pipeline-definitie worden geïntegreerd.
    * **Schaalbaarheid in Federaties:** Wanneer elke deelnemer in een data space zijn data aanbiedt als een gestandaardiseerd data product (geproduceerd via declaratieve methoden), ontstaat een schaalbaar netwerk. Nieuwe bronnen kunnen eenvoudig worden aangesloten zonder dat de centrale architectuur aangepast hoeft te worden.






