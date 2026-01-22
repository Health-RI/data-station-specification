# 7.2. Datastations voor primair vs. secundair gebruik

Dit document geeft een beschrijving van een decentrale BVO, met het [datastation](../applicatie/laag-3/data-station.md) en de [processing hub](../applicatie/laag-4/processing-hub.md) als de meest kenmerkende componenten. In vergelijking met de Cumuluz doelarchitectuur zien we vergelijkbare rollen voor het Cumuluz Datastation respectievelijk de Cumuluz Integrator. Zoals in de inleiding is gesteld, is een vergelijking van de architectuur voor primair vs. secundair een van de centrale onderzoeksvragen: 

> Zijn er lancunes danwel tegenstrijdigheden in de huidige benadering van de EHDS voor secundair gebruik die het gebruik van decentrale BVOs in de weg staan, met name ook in relatie tot datastations voor primair gebruik? Zo ja, welke oplossingsrichtingen zijn er?

In het onderstaande wordt ingegaan op deze vragen.

## 7.2.1. Verschil in grondslag voor geautoriseerde toegang

Wanneer we de Cumuluz doelarchitectuur vergelijken met dit document, dan zien we dat beide architecturen streven naar een "eenmalige registratie, meervoudig gebruik" benadering. Er is echter een essentieel verschil in de grondslag:

- **Primair gebruik:** gebaseerd op de behandelrelatie en toestemming van de patiënt.
- **Secundair gebruik:** Gebaseerd op een vergunning uitgegeven door een HDAB.

In het ontwerp van een Cumuluz Datastation is duidelijk gespecificeerd hoe via een centrale toestemmingsvoorziening (MITZ) toegang tot het datastation wordt gegeven. In het geval van secundair gebruik is er nog geen sluitende technische integratie waarbij een decentraal datastation autonoom vergunning die door de HDAB/DAAMS is uitgegeven kan valideren. Dit laatste staat los van MITZ, waarin alleen op de opt-out registratie voor secundair gebruik is vastgelegd.

## 7.2.2. Vergelijking primair en secundair datastation

???+ success "Overeenkomsten tussen primaire en secundaire datastations"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | DS-O1 | Vergelijkbare, zo niet identieke, ontwerp principes en niet-functionele vereisten. |
    | DS-02 | Een datastation valt in het domein van de datahouder. |
    | DS-O3 | Een datastation gaat uit van conformiteit, waarbij meerdere informatiemodellen worden ondersteund incl. functionaliteit om transformaties tussen deze modellen uit te voeren. |
         
???+ warning "Verschillen tussen primaire en secundaire datastations"
    | ID    | Omschrijving |
    |:------:|:-------------|
    | DS-V1 | Primair gebruik richt zich uitsluitend op klinische data. Secundair gebruik omvat ook bedrijfsmatige en logistieke data. |
    | DS-V2 | Localisatie van data in het primaire proces is gebaseerd op unieke identifiers voor personen, terwijl in het secundaire proces de gegevenscatalogus wordt gebruikt. |
    | DS-V3 | Toegangscontrole bij een datastation wordt uitgevoerd op persoonsniveau. Bij een secundair datastation is toegangscontrole ingericht op de berekening die wordt uitgevoerd. |
    | DS-V4 | Primair gebruik is geoptimaliseerd voor snelle (_latency_ minder dan 1 seconde) voor bevraging van data van één persoon, terwijl secundair gebruik uit gaat van bulk bevraging met een grotere latency. |
    | DS-V5 | Opslag van data is bij een primair datastation optioneel, bij een secondair datastations een vereiste om _data visiting_ te ondersteunen. |
    | DS-V6 | Een primair datastation heeft geen voorziening voor het lokaal uitvoeren van berekeningen. Voor een secondair datastations een vereiste om _data visiting_ te ondersteunen. |

## Vergelijking Integrator (primair) en Processing Hub (secundair)

???+ success "Overeenkomsten centrale interatie component in laag 4"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | L4-O1 | Vergelijkbare, zo niet identieke, ontwerp principes en niet-functionele vereisten. |
    | L4-O2 | Data gebruikers (systemen of personen) krijgen toegang tot data via één centrale ingang, er wordt gebruik gemaakt van een _hub-and-spoke_ netwerk topologie. |
    | L4-03 | Inrichting van laag 4 gaat uit van het [_four corner model_](https://health-ri.github.io/data-spaces-archimate/?view=id-65fda4e829df4a489df5644ffbbdb0e6): meerdere service providers zijn voorzien in het LDN. |

???+ warning "Verschillen centrale interatie component in laag 4"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | L4-V1 | Grondslag en rol van data gebruiker in primair proces is anders voor primair (behandelrelatie) en secundair (vergunning of gegevensverzoek). |
    | L4-V2 | De Processing Hub vervult een belangrijke functie voor output controle c.q. _statistical disclosure control_. Dit is bij primair gebruik niet aan de orde. |








### Geharmoniseerde API voor Permits en Autorisatie:**
Het Landelijk Afsprakenstelsel (LAS) moet worden uitgebreid met een specifieke "EHDS-connector". Deze API moet het voor een decentraal Datastation mogelijk maken om een digitale permit van de HDAB direct te vertalen naar lokale toegangsrechten in de BVO, vergelijkbaar met hoe de Generieke Functie Autorisatie werkt voor primair gebruik.


* **Dual-purpose Adapter Functies:**
De "Adapter"-rol in de CumuluZ-architectuur moet worden doorontwikkeld naar een dual-purpose component die zowel FHIR (primair) als analytische formaten (secundair) kan uitserveren vanuit dezelfde geabstraheerde datalaag. Dit borgt dat de data-integriteit tussen de patiëntenzorg en onderzoek behouden blijft.


* **Eenduidige Governance op "Data Access Committees" (DAC):**
Het proces voor het verlenen van toegang moet worden gestroomlijnd waarbij de lokale DAC van een ziekenhuis en de nationale HDAB via een federatief model samenwerken. Dit voorkomt dubbele administratieve lasten en zorgt ervoor dat de bronhouder de regie behoudt, conform architectuurprincipe C2.

Onderstaande tabellen geven een overzicht van de verschillen en overeenkomst tussen datastation voor primair en secundair gebruik, als ook voor de centrale integratie component in laag 4.






## Parking lot

- [EHRxF FHIR profiel](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/)