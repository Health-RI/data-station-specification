# KIK-V implementatie: applicatie

## Het KIK-V data station

Het KIK-V data station is een gestandaardiseerde applicatie waarmee de syntactische en semantische interoperabiliteit van data wordt gerealiseerd. Hiertoe is een specificatie opgesteld zodat zakelijke dienstverleners een _datastation-as-a-service_ kunnen aanbieden. Een KIK-V data station moet ten minste voldoen aan alle onderstaande functionaliteiten. Uiteraard staat het de data station leveranciers daarnaast vrij om hun eigen functionaliteiten toe te voegen. 

| Vereiste functionaliteit | Omschrijving |
|:-------------------------|:-------------|
| Gegevens importeren | het systeem kan gegevens ophalen via verschillende manieren, zoals API's, databankkoppelingen of bestanden (zoals XML, JSON, CSV). |
| Omzetten naar standaardformaat | data wordt automatisch omgezet naar een standaardformaat (RDF) |
| Beheren van koppelingen | je kunt koppelingen eenvoudig toevoegen, testen, aanpassen of verwijderen. |
| Automatisch en handmatig importeren | zowel geautomatiseerde als handmatige gegevensinvoer wordt ondersteund. |
| Ondersteuning van berekeningen | handmatige invoer van berekende gegevens is ook mogelijk. |
| Meerdere versies | het systeem werkt met verschillende ontologieën en versies van ontologieën. |
| Controleren op fouten | data wordt gevalideerd, bijvoorbeeld op volledigheid en juistheid. |
| Gegevens koppelen | data kan automatisch worden verbonden aan ontologieën. |
| Inzicht in acties | activiteiten zoals importeren en controleren worden opgeslagen in een logboek. |
| Vragen stellen | gevalideerde vragen stellen gebeurt via de SPARQL manier.  |
| Open standaarden en FAIR-principes | het systeem gebruikt internationaal erkende standaarden (RDF, SPARQL, OWL2) en ondersteunt toegankelijk en herbruikbaar delen van data. |
| Automatisch koppelen van data | het systeem kan zelfstandig verbanden leggen tussen gegevens. |
| Flexibel | nieuwe bronsystemen en partners kunnen gemakkelijk worden toegevoegd. |
| Geschikt voor zorginstellingen | zowel grote als kleine zorginstellingen, met verschillende IT-niveaus, kunnen het systeem gebruiken. |

Per december 2025 zijn er drie leveranciers van KIK-V data stations: [bince](https://bince.nl/over-het-product/daas-kik-v-zorginstituut), [nlcom](https://nlcom.nl/diensten/kik-v-daas/) en [SureSync](https://suresync.nl/datastation). Een screenshot van Bince geeft een indruk hoe het data station in de praktijk gebruikt wordt.

![](https://bince-2020.imgix.net/media/Bince-Datastation-KIK-V-Pagina-2-1.png?auto=format&crop=focalpoint&domain=bince-2020.imgix.net&fit=crop&fp-x=0.5&fp-y=0.5&ixlib=php-3.3.1&q=100&w=1170n)

## KIK-Starter

