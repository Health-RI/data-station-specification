# 4.5. Federatieve analyse

Federatieve analyse is identiek aan het concept van _Federated Database Systems_ zoals in de jaren 1980 voor het eerst is beschreven.[@heimbigner1985federated] Hierbij worden queries decentraal uitgevoerd op de datastations. De resultaten van deze queries worden vervolgens naar een aggregatie server gestuurd die de resultaten combineerd en mogelijk verder aggregeerd. In de context van de EHDS voert deze aggregatie server idealiter ook de _statistical disclosure control_.[@elliot2018future] uit, die erop toeziet dat het eindresultaat voldoet aan vooraf gedefinieerde eisen van anonimiteit. Een recent artikel over moderne gefedereerde database systemen geeft een overzicht van de verschillende vormen en oplossingsrichtingen voor federatieve analyse, de huidige standaarden en toekomstige uitdagingen.[@azevedo2020modern]


## 4.5.1. Verschillende vormen van federatieve analyse systemen

Federatieve analyse systemen kunnen worden geclassificeerd door te kijken naar de mate van heterogeniteit en het aantal query-interfaces dat wordt aangeboden, wat leidt tot de volgende vereenvoudigde indeling.

!!! abstract "Vereenvoudigde indeling van federatieve analyse systemen"

    |   | **Homogene data** | **Heterogene data** |
    |---|:------------------|:--------------------|
    | **Enkelvoudige interface** | **Federated Database System:** Gebruikt homogene datastores en een enkele standaard query-interface. Dit maakt vaak gebruik van een *mediator-wrapper* architectuur voor data-integratie. |  **Multistore System:** Integreert heterogene datastores (zoals een combinatie van RDBMS, NoSQL en Distributed File Systems) via één enkele query-interface. |
    | **Meerdere interfaces** | **Polyglot System:** Gebruikt homogene datastores maar biedt meerdere query-interfaces aan, waardoor semantische rijkdom wordt toegevoegd (bijv. Spark SQL). | **Polystore System:** De meest complexe vorm, waarbij heterogene datastores worden ontsloten via meerdere query-interfaces. Voorbeelden hiervan zijn BigDAWG en Apache Drill. |


    Daarnaast kunnen systemen worden ingedeeld op basis van hun koppeling (coupling):

    - **Loosely Coupled:** Autonome lokale datastores die benaderd worden via een gemeenschappelijke of lokale taal.
    - **Tightly Coupled:** Systemen die gebruikmaken van één taal voor het bevragen van zowel gestructureerde als ongestructureerde data, vaak gericht op performance en self-tuning.
    - **Hybrid Systems:** Een combinatie van beide benaderingen (bijv. Spark SQL).

De functionaliteit en gebruikerservaring van een federatieve analyse systeem wordt vooral bepaald door de query-interface(s) die worden aangeboden.

!!! abstract "Meest voorkomende query interfaces"

    === "SQL"

        SQL (Structured Query Language, oorspronkelijk SEQUEL) is een ANSI/ISO-standaardtaal voor een relationeel databasemanagementsysteem (DBMS). Het is een gestandaardiseerde taal die gebruikt kan worden voor taken zoals het bevragen en het aanpassen van gegevens in een relationele database. SQL kan met vrijwel alle moderne relationele databaseproducten worden gebruikt.
    
    === "NoSQL"

        No SQL of 'Not Only SQL' gaat uit van een document systeem, waarin de data in JSON formaat is opgeslagen. MongoDB is hier een voorbeeld van. Er is op dit moment geen open standaard voor NoSQL.

    === "Graph Query Language"

        Graph Query Language (GQL) is een nieuwe standaard voor het queryen van Labeled Property Graphs. GQL is afgeleid van Cypher, de query taal van neo4j, wat een van de meest gebruikte labeled property graph engines is. GQL is in april 2024 als standaard vastgesteld in ISO/IEC 39075.

    === "SPARQL"

        SPARQL (SPARQL Protocol And RDF Query Language) is een query-interface voor triple-stores en RDF-gebaseerde data. Met deze zoektaal is het mogelijk om informatie op te vragen voor applicaties op het semantisch web. Het is een W3C standaard, versie 1.1 is in 2009 vastgesteld.



## 4.5.2. Meest voorkomende implementaties

De huidige generatie federatieve systemen (zoals BigDAWG, CloudMdsQL en Myria) richt zich op het integreren van relationele data met diverse NoSQL- en bestandsformaten.

* 
**Query Talen:** De standaard is overwegend SQL-achtig (zoals HiveQL, SparkSQL) om integratie te vergemakkelijken, hoewel sommige systemen native query-talen of functionele talen ondersteunen om specifieke eigenschappen van onderliggende databases te benutten.


* 
**Schema Management:** De meeste multistores hanteren een *Global-as-View (GAV)* of *Local-as-View (LAV)* aanpak om globale schema's te definiëren over de lokale bronnen heen.


* 
**Optimalisatie:** Query-optimalisatie vindt plaats via kostenmodellen of heuristieken, waarbij technieken uit gedistribueerde databases worden toegepast, zoals *bind joins* en het 'pushen' van selecties naar de bron (pushdown).



## 4.5.3. Toekomstige Ontwikkelingen en Uitdagingen

Om datastations verder te ontwikkelen richting volwaardige federatieve analyseplatformen, moeten volgens het artikel nog diverse technologische uitdagingen worden overwonnen:

- **Semantische Mapping:** Het automatisch vertalen van query's naar het lokale dialect van een opslagsysteem en het integreren van resultaten blijft een uitdaging.
- **Gedistribueerde Transacties:** Het beheren van transacties over heterogene systemen, zeker wanneer NoSQL-stores (die vaak geen ACID ondersteunen) betrokken zijn, vereist nieuwe standaarden.
- **Complex Analytics & Lineaire Algebra:** De verschuiving van eenvoudige aggregaties (COUNT, SUM) naar voorspellende modellen (Machine Learning) vereist de integratie van lineaire algebra binnen het databasesysteem. Huidige systemen moeten data vaak inefficiënt converteren tussen de opslag en algebraïsche rekenpakketten; een nauwere, goedkopere integratie is noodzakelijk.
- **Dataplaatsing en Shuffle:** Systemen moeten intelligenter worden in het verplaatsen van data en tussenresultaten (shuffling) naar de *engine* die het beste model heeft om een specifieke query te beantwoorden.
- **Benchmarks:** Er is behoefte aan standaarden en benchmarks (zoals PolyBench) om de prestaties van complexe polystores en federatieve combinaties objectief te kunnen evalueren.