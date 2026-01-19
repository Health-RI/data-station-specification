# 7.1. Data stations voor primair vs. secundair gebruik

Dit document geeft een beschrijving van een federatieve BVO, met het [data station](../componenten/laag-3/data-station.md) en de [Federated Processing Hub](../componenten/laag-4/fph.md) als de meest kenmerkende componenten. In de context van primair gebruik wordt ook gesproken over data stations en centrale integratie componenten zoals bijvoorbeeld de [_Interoperability Layer_](https://guides.ohie.org/arch-spec/openhie-component-specifications-1/openhie-interoperability-layer-iol) in de OpenHIE architectuur. Doel is om een van de onderzoeksvragen hierover te addresseren:

> Zijn er lancunes danwel tegenstrijdigheden in de huidige benadering van de EHDS voor secundair gebruik die het gebruik van federatieve BVOs in de weg staan, met name ook in relatie tot data stations voor primair gebruik? Zo ja, welke oplossingsrichtingen zijn er?

Onderstaande tabellen geven een overzicht van de verschillen en overeenkomst tussen data station voor primair en secundair gebruik, als ook voor de centrale integratie component in laag 4.

### Overeenkomsten en verschillen data stations

???+ success "Overeenkomsten tussen primaire en secundaire data stations"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | DS-O1 | Vergelijkbare, zo niet identieke, ontwerp principes en niet-functionele vereisten op het gebied van authenticatie, localisatie, beveiliging etc. |
    | DS-02 | Een data station valt in het domein van de data houder. |
    | DS-O3 | Een data station gaat uit van conformiteit, waarbij meerdere informatiemodellen worden ondersteund incl. functionaliteit om transformaties tussen deze modellen uit te voeren. |
         
???+ warning "Verschillen tussen primaire en secundaire data stations"
    | ID    | Omschrijving |
    |:------:|:-------------|
    | DS-V1 | Primair gebruik richt zich uitsluitend op klinische data. Secundair gebruik omvat ook bedrijfsmatige en logistieke data. |
    | DS-V2 | Localisatie van data in het primaire proces is gebaseerd op unieke identifiers voor personen, terwijl in het secundaire proces de gegevenscatalogus wordt gebruikt. |
    | DS-V3 | Toegangscontrole bij een data station wordt uitgevoerd op persoonsniveau. Bij een secundair data station is toegangscontrole ingericht op de berekening die wordt uitgevoerd. |
    | DS-V4 | Primair gebruik is geoptimaliseerd voor snelle (_latency_ minder dan 1 seconde) voor bevraging van data van één persoon, terwijl secundair gebruik uit gaat van bulk bevraging met een grotere latency. |
    | DS-V5 | Opslag van data is bij een primair data station optioneel, bij een secondair data stations een vereiste om _data visiting_ te ondersteunen. |
    | DS-V6 | Een primair data station heeft geen voorziening voor het lokaal uitvoeren van berekeningen. Voor een secondair data stations een vereiste om _data visiting_ te ondersteunen. |


### Overeenkomsten en verschillen integratie component in laag 4

???+ success "Overeenkomsten centrale interatie component in laag 4"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | L4-O1 | Vergelijkbare, zo niet identieke, ontwerp principes en niet-functionele vereisten op het gebied van authenticatie, localisatie, beveiliging etc. |
    | L4-O2 | Data gebruikers (systemen of personen) krijgen toegang tot data via één centrale ingang, er wordt gebruik gemaakt van een _hub-and-spoke_ netwerk topologie. |
    | L4-03 | Inrichting van laag 4 gaat uit van het [_four corner model_](https://health-ri.github.io/data-spaces-archimate/?view=id-65fda4e829df4a489df5644ffbbdb0e6): meerdere service providers zijn voorzien in het LDN. |

???+ warning "Verschillen centrale interatie component in laag 4"
    | ID    | Omschrijving |
    |:-----:|:-------------|
    | L4-V1 | Grondslag en rol van data gebruiker in primair proces is anders voor primair (behandelrelatie) en secundair (vergunning of gegevensverzoek). |
    | L4-V2 | De Processing Hub vervult een belangrijke functie voor output controle c.q. _statistical disclosure control_. Dit is bij primair gebruik niet aan de orde. |

## Parking lot

- [EHRxF FHIR profiel](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/)