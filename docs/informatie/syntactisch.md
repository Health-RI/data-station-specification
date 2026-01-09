# 3.1. Syntactische interoperabiliteit

## 3.1.1. Convergentie van openEHR, FHIR en OMOP

![](syntactic-convergence.png)

In de zorg worden veel verschillende informatie modellen gebruikt, maar in de afgelopen jaar is de sector aan het convergeren naar openEHR, OMOP en FHIR als de belangrijkste informatiemodellen.[@tsafnat2024converge] Om syntactische interoperabiliteit tussen deze drie standaarden te realiseren, is het noodzakelijk om specificaties c.q. mappings op te stellen hoe elementen uit het ene informatiemodel vertaald moeten worden naar het andere. Idealiter staan deze formele mappingsspecificaties los van de specifieke implementatie van software om de mappings daadwerkelijk te realiseren, zoals in bovenstaand diagram is weergegeven.


## 3.1.2. Formele specificaties voor syntactische mappings

Ten tijde van het schrijven van dit document zijn de volgende (eerste versies van) formele mappingsspecificaties beschikbaar.


=== "**FHIRconnect**"

    De [FHIRconnect Specificatie](https://sevkohler.github.io/FHIRconnect-spec/build/site/FHIRconnect/v1.0.0/index.html). Deze aanpak gebruikt een Domain Specific Language (DSL) om mappings te definiëren. Het abstraheert de transformatielogica naar "Mapping Templates" die onafhankelijk zijn van de onderliggende programmeertaal.

=== "**HL7 FHIR-OMOP IG**"

    De [HL7 FHIR-OMOP Implementation Guide](https://build.fhir.org/ig/HL7/fhir-omop-ig/) biedt de formele regels voor cross-paradigma mapping, waarbij het transactionele karakter van FHIR en het longitudinale karakter van OMOP worden verzoend.

=== "**OMOCL**"

    De [OMOP Conversione Language](https://www.sciencedirect.com/science/article/pii/S1532046423001582) is een domein-specifieke taal waarin mapping van openEHR archetypes zijn gemaakt naar het OMOP CDM. Het is het resultaat van ee onderzoeksproject en is in juli 2025 ter consultatie  voorgelegd aan de openEHR community met als doel om het als formele specificatie te adopteren. EOS is de referentie implementatie van OMOCL. 


## 3.1.3. Implementaties van syntactische mappings

Implementaties zijn de uitvoeringsmotoren (engines) die de formele specificaties interpreteren om gegevens te transformeren of te verplaatsen. Daarbij wordt onderscheidt gemaakt tussen twee verschillende implementatie patronen.

1. Een facade-patroon implementeert een real-time mapping laag bovenop een bestaande database.
2. Een ETL-patroon implementeert data transformatie 'straten' die periodiek (typisch dagelijks) de data van het ene formaat naar het andere vertalen. Dit patroon komt uit datawarehousing.

=== "**openFHIR**"

    [openFHIR](https://open-fhir.com/#access) is een commerciele implementatie van de FHIRconnect specificatie. Het gebruikt een facade-patroon om bi-directioneel FHIR data in openEHR op te slaan, en FHIR data uit openEHR te lezen. 

=== "**EOS**"

    Het [Eos Framework](https://github.com/SevKohler/Eos) is de referentieimplementatie van de OMOCL mappingspecificatie. Het volgt een ETL patroon en is geimplementeerd in Java.

=== "**OMOPonFHIR**"
    
    Het [OMOPonFHIR](https://github.com/omoponfhir) project levert de softwarecomponenten (servers, adapters) die de bidirectionele FHIR interface realiseren bovenop het OMP CDM. Deze oplossing volgt een facade-patroon: wanneer een client een FHIR `Observation` opvraagt via een REST API, onderschept de facade-laag het verzoek, voert een query uit op de onderliggende OMOP `MEASUREMENT`-tabel in real-time, en transformeert het resultaat naar een FHIR JSON-resource middels de formele specificatie. Middels dit facase patroon kunnen FHIR berichten ook worden opgeslagen in de OMOP database. OMOPonFHIR gaat uit van OMOP CDM 5.4 en FHIR v4 en is geimplementeerd in Java. Het is ontwikkeld voordat de HL7 FHIR-OMOP IG beschikbaar was en heeft daarom de mappings zelf gedefinieerd.


### 3.1.4. Implicaties voor datastation

Conform TEHDAS2 moeten BVOs syntactische operabiliteit ondersteunen, incl. transformaties tussen de meest voorkomende informatiemodellen zoals hierboven is beschreven (zie FCR-1 en FCR-2 in de [TEHDAS2 requirements](../appendix/tehdas2-requirements.md)). In het geval dat datasets of zelfs hele databases beschikbaar zijn in een van de drie informatiemodellen, kunnen van syntactische transformaties goed worden uitgevoerd. Naar verwachting zullen bovengenoemde specificaties en referentieimplementaties komende jaren een mate van volwassenheid behalen dat ze kunnen worden opgenomen als component binnen een BVO.

Daarbij is het goed om op te merken dat alle openEHR, FHIR en OMOP vaak gebruik maken van dezelfde taxonmieen, thesauri en/of ontologieen. Als bijvoorbeeld binnen openEHR SNOMED wordt gebruikt, dan kan een transformatie naar FHIR en/of OMOP zonder verlies van betekenis worden gedaan omdat de SNOMED codering integraal wordt overgenomen. In de praktijk zal het grootste pijnpunt liggen in semantische transformaties. Stel, een datahouder maakt gebruik van de G-standaard voor medicatie, wat in Nederland de meest gebruikte taxonomie is voor medicatie. En stel dat de datahouder de data in FHIR formaat kan aanleveren heeft, en dat het op het datastation in OMOP formaat beschikbaar gesteld moet worden. Met gebruik van de FHIRconnect specificatie zal de _syntactische_ transformatie relatief makkelijk te implementeren zijn. De _semantische_ mapping van de G-standaard naar bijvoorbeeld IDMP als Europese standaard voor medicatie zal veel bewerkelijker zijn.

Hetzelfde geldt voor het ontsluiten van bronsystemen met een niet-standaard informatiemodel, zoals bij veel zorginformatiesystemen het geval is. In de praktijk is het vaak relatief makkelijk om het _legacy_ informatiemodel te mappen naar openEHR, FHIR of OMOP. Het aantal dienstverleners dat hiervoor producten en diensten aanbiedt groeit ook gestaag. Maar ook hier zit het pijnpunt in de semantische mappings. Als bijvoorbeeld medicatievoorschriften in het bronsysteem als vrije tekst is opgeslagen, dan kan het erg bewerkelijk zijn om die tekst om te zetten naar het  vereiste codestelsel. De details van semantische transformaties worden in de volgende sectie besproken. Voor nu sluiten we af met een lijst van voorbeelden.

| Bronsysteem | Doelsysteem | Toelichting |
|:------------|:------------|:------------|
| Epic FHIR v3 | OMOP CDM 5.4 | - FHIR v3 naar v4 vertalen met gebruik van bestaande specifcaties<br>- FHIRconnect specificatie gebruiken en implementeren programmeertaal naar keuze<br>- Lage complexiteit mits codestelses in FHIR v3 reeds goed gebruikt worden in het bronsysteem |
| openEHR | OMOP CDM 5.4 | - RSO Zuid-Limburg heeft binnen haar regio reeds de transformatie van _legacy_ systemen naar openEHR gemaakt voor primair gebruik van data<br>- Met OMOCL en EOS kunnen vanuit openEHR met een ETL patroon datastations voor secundair gebruik worden geimplementeerd |
| OMOP CDM 5.4 | FHIR | - Stel een landelijke kwaliteitsregistratie gebruikt OMOP en wil een app voor burger maken die het mogelijk maakt om informatie over zichzelf op te zoeken<br>- Met OMOPonFHIR kan een FHIR-facade worden gerealiseerd om daarmee een API voor de app aan te bieden |


