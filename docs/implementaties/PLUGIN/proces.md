# Proces voor federatieve verwerking met PLUGIN

Deze pagina beschrijft hoe de PLUGIN-implementatie, die gebruikmaakt van vantage6, de processen voor [federatieve analyse](../../proces/analyseren.md) en het [klaarzetten van data](../../proces/klaarzetten.md) ondersteunt. PLUGIN/vantage6 is een concreet voorbeeld van hoe een Datastation en een Processing Hub kunnen samenwerken voor secundair datagebruik, zoals beschreven in het hoofdstuk over het [datastation](../../applicatie/laag-3/data-station.md).

In deze implementatie wordt de rol van het Datastation vervuld door een **vantage6 Node**. De coördinatie tussen de nodes wordt beheerd door een **vantage6 Server**. De datagebruiker initieert de taken vanaf een Processing Hub, die in deze context functioneert als een client naar de vantage6-infrastructuur.

## Opzetten van een samenwerkingsverband

Om een federatief proces te starten, moet eerst een samenwerkingsverband worden opgezet. Binnen vantage6 worden hiervoor de volgende entiteiten gebruikt:

![](./vantage6-rollen.svg)

*   **Samenwerking (Collaboration):** Een verzameling van organisaties (dataleveranciers) die met elkaar samenwerken. Dit komt overeen met de groep dataleveranciers waarvoor een datagebruiker een vergunning heeft.
*   **Organisatie (Organization):** Een deelnemende entiteit, zoals een ziekenhuis of onderzoeksinstituut.
*   **Node:** De technische implementatie van een Datastation. Dit is een service die bij de organisatie (datahouder) draait en taken (algoritmes) uitvoert op de lokale data.
*   **Gebruiker (User):** Een persoon die namens een organisatie op de Processing Hub taken mag aanmaken en beheren.
*   **Taak (Task):** Een specifieke opdracht, zoals het trainen van een model of het uitvoeren van een analyse, die naar een of meerdere nodes wordt gestuurd.
*   **Rol (Role) en Regel (Rule):** Definiëren de permissies van een gebruiker.

De **vantage6 Server** beheert deze entiteiten en zorgt voor veilige communicatie en correcte autorisatie, in lijn met de governance-eisen van de dataspace. Medical Data Works heeft afgelopen jaren veel ervaring opgedaan met het opzetten van dergelijke samenwerkingsverbanden en heeft hiertoe standaard [overeenkomsten en governance documenten](https://www.medicaldataworks.nl/governance) opgesteld en [open source beschikbaar gesteld](https://cris.maastrichtuniversity.nl/en/publications/a-governance-framework-for-federated-learning-projects-in-healthc/). 

*   **Infrastructure User Agreement:** Een overeenkomst tussen elk datastation en de beheerder van de infrastructuur. Hierin staan de rollen en verantwoordelijkheden op het gebied van de infrastructuur van de partijen beschreven. Dit contract staat los van het project of de samenwerking, en kan dus worden hergebruikt voor toekomstige projecten.
*   **Consortium Agreement:** Hoewel er patientdata op individuele basis wordt verstuurd, beschrijft dit document de omgang met intellectueel eigendom, welke partijen toestemming hebben om nieuwe taken te starten, en wie recht heeft de resultaten te publiceren.
*   **Data Processing or Joint Controller Agreement:** In het geval van federated learning vindt verwerking op het datastation plaats van de eigenaar van de data, op verzoek van de instantie die het algoritme rondstuurt. Voor de AVG is dan ook een data processing agreement nodig. Wanneer deelnemende ziekenhuizen ook deelnemen in de ontwikkeling van de rondgestuurde algoritmen, is een joint controller agreement nodig om aan te geven dat beide partijen betrokken waren bij de uitwerking van de verwerking.

## Uitvoeren van een federatieve taak

Het uitvoeren van een federatieve taak, zoals federatief leren of een federatieve analyse, volgt een vast proces dat is ontworpen om data lokaal te houden.

1.  **Taakcreatie:** Een gebruiker (bijv. een onderzoeker via de Processing Hub) maakt een centrale taak aan. Deze taak specificeert welk algoritme moet worden uitgevoerd en op welke Datastations (nodes).
2.  **Distributie:** De vantage6 Server ontvangt de centrale taak en deelt deze op in subtaken voor elke deelnemende node.
3.  **Lokale Uitvoering:** Elke node voert de taak (het algoritme) uit op de lokale data. Dit gebeurt in een geïsoleerde omgeving (een Docker-container), zoals beschreven in de usecase [Verwerk algoritme en geef resultaat terug](../../applicatie/laag-3/data-station.md#414-verwerk-algoritme-en-geef-resultaat-terug). De ruwe data verlaat de node niet.
4.  **Resultaten retourneren:** De node stuurt het resultaat (bv. een lokaal getraind model of een geaggregeerd antwoord) terug naar de centrale locatie die de taak coördineert.
5.  **Aggregatie:** De resultaten van alle nodes worden geaggregeerd om tot een eindresultaat te komen. Dit kan een iteratief proces zijn, waarbij de geaggregeerde resultaten worden gebruikt voor een volgende ronde van subtaken.

## Principe van taakverdeling

Een kernprincipe van federatieve verwerking is de scheiding tussen een centraal coördinerend deel en decentrale, federatieve delen van een algoritme.

Stel, we willen het gemiddelde berekenen over data die verdeeld is over twee locaties: `a = [1,2,3]` en `b = [4,5]`. De berekening is `(sum(a) + sum(b)) / (len(a) + len(b))`.

*   **Federatief deel:** Elke locatie berekent lokaal `sum()` en `len()`. Dit zijn de subtaken die op de `Datastations` (nodes) worden uitgevoerd.
*   **Centraal deel:** Het coördinerende algoritme verzamelt de resultaten (`sum` en `len` van elke locatie) en voert de uiteindelijke deling uit om het globale gemiddelde te krijgen.

Belangrijk is dat de centrale coördinatie niet per se op de vantage6 server plaatsvindt. Om de server licht te houden, wordt de centrale (aggregerende) taak zelf ook als een container op een van de nodes uitgevoerd. De vantage6 server fungeert puur als doorgeefluik en autorisatie-orgaan. Dit patroon is hieronder schematisch weergegeven.

!!! note "Toelichting taakverdeling"

    De meest simpele taakverdeling in vantage6 is als volgt. De datagebruiker (links) creëert een taak voor het centrale deel van het algoritme (roze zeshoek). Het centrale deel creëert sub-taken voor de gefedereerde delen (groene zeshoeken). Wanneer de sub-taken zijn         voltooid, verzamelt het centrale deel de resultaten en berekent het het uiteindelijke resultaat, dat vervolgens beschikbaar is voor de datagebruiker.            
    
    ![](./algorithm_central_and_subtasks.png)

    In de praktijk werkt de taakverdeling net iets anders. De datagebruiker creëert een taak voor het centrale deel van het algoritme. Dit wordt geregistreerd op de server en leidt tot de creatie van een centrale algoritmecontainer op een van de vantage6 nodes.  Het centrale algoritme creëert vervolgens sub-taken voor de gefedereerde delen van het algoritme, die opnieuw worden geregistreerd op de server. Alle vantage6 nodes waarvoor de sub-taak bedoeld is, beginnen hun werk door het gefedereerde deel van het algoritme uit te voeren. De vantage6 nodes sturen de resultaten terug naar de vantage6 server, vanwaar ze worden opgepikt door het centrale algoritme. Het centrale algoritme berekent vervolgens het uiteindelijke resultaat en stuurt dit naar de processing hub, waar de datagebruiker het kan ophalen.

    ![](./task_journey.png)

    Het is gemakkelijk om de centrale vanatage6 server te verwarren met het centrale deel van het algoritme: de vantage6 server is het centrale deel van de infrastructuur, maar niet de plaats waar het centrale deel van het algoritme wordt uitgevoerd (Fig. 2). Het centrale deel wordt feitelijk uitgevoerd op een van de vantage6 nodes, omdat dit meer flexibiliteit biedt: een algoritme kan bijvoorbeeld zware rekenbronnen nodig hebben om de aggregatie uit te voeren, en het is beter om dit te doen op een vantage6 node dat over deze bronnen beschikt, in plaats van de server te moeten upgraden telkens wanneer een nieuw algoritme meer bronnen nodig heeft.   

## Federatief leren met PLUGIN/vantage6

De PLUGIN-architectuur is gebaseerd op vantage6. Het gefedereerd leren van een algoritme omvat een reeks gecoördineerde stappen tussen de onderzoeker, de centrale server en de datastations. Dit proces is ontworpen om de analyse uit te voeren zonder dat de brongegevens de lokale omgeving van het datastation verlaten. Hieronder volgt een detailleerde beschrijving wat elk van de applicatiecomponenten hierin doen.

```mermaid
    sequenceDiagram
        actor Onderzoeker
        participant Server
        participant Aggregator as Secure Aggregation Server (SAS)
        participant Registry as Docker Registry

        box "Meerdere worker-nodes"
            participant Node as Node(s)
        end

        Onderzoeker->>Server: Authenticatie
        Onderzoeker->>Server: Taak specificatie (Server API)

        Aggregator->>Server: Hoofdtaak ophalen
        Aggregator->>Registry: Docker-image ophalen (hoofdtaak)

        Aggregator->>Server: Subtaken aanmaken

        loop Voor elke subtaak (parallel uitgevoerd)
            Node->>Server: Subtaak ophalen
            Node->>Registry: Docker-image ophalen (subtaak)
            Node->>Server: Resultaat van subtaak opslaan
            Aggregator->>Server: Subtaakresultaten ophalen
            Aggregator->>Aggregator: Verificatie en aggregatie
        end

        Aggregator->>Server: Eindresultaat van hoofdtaak indienen

        Onderzoeker->>Server: Eindresultaat ophalen
```

???+ note "**Authenticatie**"

    De onderzoeker start het proces door te authenticeren bij de centrale Vantage6-server.

??? note "**Taak specificatie**"
    
    Na succesvolle authenticatie definieert de onderzoeker een taak. Hierbij wordt opgegeven:
    *   Welk algoritme (Docker-image) gebruikt moet worden.
    *   Specifieke inputparameters voor de analyse.
    *   Het aantal iteraties (indien van toepassing, voor machine learning).
    *   De identiteit van de *Secure Aggregation Server* (SAS), de node die verantwoordelijk is voor het aggregeren van resultaten.

??? note "**Verzending naar nodes**"
    
    De centrale server stuurt de taak door naar de betrokken nodes. De SAS (Secure Aggregation Server, een specifieke node) ontvangt het verzoek als eerste.

??? note "**Start hoofdalgoritme (SAS)**"
    
    De SAS downloadt het Docker-image, start het hoofd-algoritme en orkestreert de subtaken die door de datastations uitgevoerd moeten worden.

??? note "**Start subtaken (datastations)**"
    
    De datastations ontvangen hun subtaak van de centrale server, downloaden hetzelfde Docker-image en starten het lokale deel van het algoritme. De analyse wordt uitgevoerd op de lokale data.

??? note "**Verzending lokale resultaten**"
    
    Na elke trainingscyclus of analysestap stuurt het algoritme op het datastation de lokale resultaten (bijv. modelgewichten of statistische coëfficiënten) naar de SAS. De brongegevens verlaten het datastation niet.

??? note "**Verificatie en aggregatie**"
    
    De SAS verifieert de resultaten, extraheert de metadata en voegt de resultaten van alle datastations samen tot een geaggregeerd tussenmodel. Dit voltooit één iteratie.

??? note "**Vervolg-iteraties**"
    
    Voor vervolgstappen vragen de datastations de geaggregeerde resultaten van de vorige ronde op bij de SAS om hun lokale modellen verder te trainen. Deze cyclus herhaalt zich totdat het model convergeert of het gewenste aantal iteraties is bereikt.

??? note "**Afronding**"
    
    De SAS informeert de onderzoeker dat de taak is voltooid. De onderzoeker kan vervolgens het finale, globale model downloaden van de server. Gedurende het proces heeft niemand, ook de onderzoeker niet, toegang tot de tussenresultaten, wat de veiligheid waarborgt.
    
## Gebruik van PLUGIN voor federatieve analyse en data pooling

PLUGIN/vantage6 is van oorsprong opgezet voor het ondersteunen van federatief leren. Echter, dezelfde infrastructuur en processen kunnen worden toegepast voor verschillende vormen van secundair datagebruik.

=== "Gefedereerde analyse"

    Bij gefedereerde analyse is het doel niet het trainen van een model, maar het uitvoeren van een statistische analyse. Het "algoritme" is hierbij een aggregatiequery (bv. `COUNT` of `AVG`).

    *   Elk PLUGIN-datastation voert de query lokaal uit.
    *   De geaggregeerde (niet-identificeerbare) resultaten worden naar de centrale taak gestuurd.
    *   De centrale taak combineert de resultaten voor een overkoepelend antwoord.

    Dit sluit direct aan bij de usecase [Geef antwoord op dataverzoek](../../applicatie/laag-3/data-station.md#415-geef-antwoord-op-dataverzoek).


=== "Data pooling (doorleveren van data)"

    De infrastructuur kan ook worden gebruikt om data te verzamelen op een centrale locatie, zoals een Processing Hub. Dit wordt "Data Pooling" genoemd. Hierbij is het "algoritme" een selectiequery.

    *   Elk PLUGIN-datastation voert een selectiequery uit om een specifieke dataset of cohort te selecteren.
    *   In plaats van een geaggregeerd resultaat, stuurt de node de geselecteerde ruwe data 'as-is' door naar de Processing Hub.

    Dit proces sluit aan bij het scenario voor centrale beschikbaarstelling zoals beschreven in de usecase [Maak data beschikbaar voor secundair gebruik](../../applicatie/laag-3/data-station.md#413-maak-data-beschikbaar-voor-secundair-gebruik). Privacy en veiligheid hangen hierbij af van de beveiliging van de ontvangende Processing Hub.
