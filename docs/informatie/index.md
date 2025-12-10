#  Perspectief: informatie
## Semantische en syntactische interoperabiliteit als randvoorwaarde voor (her)gebruik van gezondheidsgegevens

Om gezondheidsgegevens zinnig te kunnen hergebruiken moet de vorm (syntax) en betekenis (semantiek) vergelijkbaar en uitwisselbaar zijn. Deze twee vormen van interoperabiliteit zijn essentiele randvoorwaarden. Om te begrijpen hoe computers met elkaar "praten", kunnen we dit vergelijken met hoe mensen communiceren.

* **Syntactische interoperabiliteit (de envelop & de grammatica):**
    Dit gaat over de **vorm** en de **structuur** van het bericht, zoals bijvoorbeeld een brief. Syntactische interoperabiliteit betekent dat de ontvanger de brief fysiek kan openen, herkent dat het een brief is, en dat zij de letters kan lezen (bijvoorbeeld het Latijnse alfabet). In de computerwereld betekent dit dat twee systemen elkaars bestanden technisch kunnen openen en de structuur herkennen (bijv. "hier staat de naam", "daar staat de datum").
    > *Analogie:* Ik stuur jou een zin die grammaticaal perfect klopt: *"De blerf schrobt de grakker."* De ontvanger kan de zin lezen (syntax is correct), maar heeft geen idee wat de verzender ermee bedoelt te zeggen.

* **Semantische interoperabiliteit (de betekenis):**
    Dit gaat over de **inhoud** en het **begrip**. Als de brief eenmaal is geopend, willen we begrijpen wat er staat. We moeten dezelfde taal spreken en dezelfde definities gebruiken. Als ik "bank" schrijf, moet de ontvanger weten of ik een zitmeubel bedoel of een geldinstelling.
    > *Analogie:* Om *"De blerf schrobt de grakker"* te begrijpen, hebben we een woordenboek nodig dat uitlegt wat een 'blerf' is. Semantische interoperabiliteit zorgt ervoor dat de computer niet alleen "180" ziet staan, maar begrijpt dat dit een "bloeddruk" is in "mmHg".

---

## Informatiemodellen voor syntactische interoperabiliteit
Om gegevens technisch uit te wisselen, hebben we standaarden nodig die de **structuur** bepalen.In de zorg kent vele informatie modellen, maar in de afgelopen jaar is de sector aan het convergeren naar openEHR, OMOP en FHIR als de belangrijkste informatiemodellen.[@tsafnat2024converge]. Hoewel ze ook betekenis (semantiek) bevatten, is hun belangrijkste functie dat ze de "container" voor de data.

* **FHIR (Fast Healthcare Interoperability Resources): De Koerier**
    * *Doel:* Snelle uitwisseling van gegevens tussen systemen (bijv. tussen een ziekenhuis en een app op je telefoon).
    * *Hoe het werkt:* Zie FHIR als een set kleine, gestandaardiseerde "bouwblokjes" of kaartjes. Er is een kaartje voor 'Patiënt', een kaartje voor 'Medicatie', etc. Het is heel flexibel en modern, vergelijkbaar met hoe internetpagina's werken.
    * *Syntactische rol:* Het bepaalt precies hoe het digitale berichtje eruitziet dat over de lijn gaat.

* **openEHR: Het Archiefsysteem**
    * *Doel:* Het langdurig en zeer gedetailleerd vastleggen van medische dossiers, onafhankelijk van leveranciers.
    * *Hoe het werkt:* openEHR werkt als een zeer geavanceerde LEGO-doos. Het definieert "archetypen" (sjablonen) voor elk mogelijk medisch concept (zoals een bloeddrukmeting) met maximale precisie.
    * *Syntactische rol:* Het biedt een strikte structuur voor **opslag**. Waar FHIR zich richt op het *versturen* van de brief, richt openEHR zich op hoe je het dossier in de kast *archiveert* zodat het over 20 jaar nog steeds leesbaar is.

* **OMOP (Observational Medical Outcomes Partnership): De Onderzoekstabel**
    * *Doel:* Grootschalig wetenschappelijk onderzoek en data-analyse over meerdere ziekenhuizen of landen heen.
    * *Hoe het werkt:* OMOP dwingt data uit allerlei verschillende systemen in één universeel tabel-formaat (het Common Data Model). Het zet alle data om naar een standaardtaal zodat onderzoekers één vraag ("Hoeveel mensen kregen griep na medicijn X?") aan honderd verschillende databases kunnen stellen.
    * *Syntactische rol:* Het standaardiseert de database-structuur voor **analyse**.

---

## Thesauri en taxonomieen voor semantische interoperabiliteit
Nu we de structuur hebben (via FHIR, openEHR of OMOP), moeten we de inhoud invullen. Hiervoor gebruiken we **terminologiestelsels** (thesauri en taxonomieën). Dit zijn de officiële woordenboeken van de zorg. Zonder deze codes zijn de bovenstaande informatiemodellen lege hulzen.

* **SNOMED CT (De Medische Encyclopedie):**
    * Dit is het meest uitgebreide medische woordenboek ter wereld. Het bevat codes voor ziektes, symptomen, operaties, lichaamsdelen, etc.
    * *Voorbeeld:* In plaats van dat de dokter "longontsteking" typt (wat in een ander land "pneumonia" heet), slaat de computer de code `233604007` op. Elke computer wereldwijd weet: dit is een longontsteking.

* **Loinc (Het Laboratoriumboek):**
    * Specifiek bedoeld voor lab-uitslagen en metingen.
    * *Voorbeeld:* Als er bloed wordt geprikt voor glucose, zorgt de LOINC-code ervoor dat het ene ziekenhuis precies weet dat het om "Glucose in serum, nuchter" gaat, en niet "Glucose in urine".

* **RxNorm (Het Medicijnboek - VS/Internationaal):**
    * Een standaard voor medicijnen, vooral sterk in de VS en gebruikt in internationaal onderzoek (zoals met OMOP). Het zorgt dat computers begrijpen dat "Paracetamol 500mg" hetzelfde actieve ingrediënt is als "Panadol 500mg".
    * *Let op:* In Nederland gebruiken we voor de dagelijkse zorg (recepten, apotheek) vaker de **G-Standaard** (beheerd door Z-Index), maar voor internationaal onderzoek wordt dit vaak vertaald naar RxNorm.

* **ICD-10 (Het Declaratieboek):**
    * Dit is een classificatie (taxonomie) die vooral wordt gebruikt voor statistiek en facturatie ("declaraties"). Het groepeert ziektes in categorieën.
    * *Verschil met SNOMED:* SNOMED is heel gedetailleerd voor de *behandeling* ("breuk van het derde kootje van de linker wijsvinger"), terwijl ICD-10 vaak wat grover is voor de *administratie* ("vingerfractuur").

---

## Ontologieen

TO DO: KIK-V uitleggen, ontologieen in b.v. genomics



## De Nederlandse context
Vaak ziet u in Nederland ook de term **ZIBs (Zorginformatiebouwstenen)**. ZIBs zijn de Nederlandse "afspraken" over hoe we een medisch concept (zoals 'Brandwond') definiëren. Een ZIB gebruikt **SNOMED** voor de betekenis en kan vervolgens technisch worden verpakt in **FHIR** (voor een app) of **openEHR** (voor het dossier).

## Wat leggen we uit

Er zijn standaarden in de maak om tussen de informatiemodellen vertalingen te maken. Conform TEHDAS2 moet een BVO transformaties tussen deze informatiemodellen ondersteunen. Voor de komende jaren zullen deze verschillende informatiemodellen blijven bestaan, dus we moeten hier een werkbare oplossing voor aanbieden.

| Transformatie | Beschrijving |
|:--|:--|
| [FHIR to OMOP](https://build.fhir.org/ig/HL7/fhir-omop-ig/)| **FHIR to OMOP** is a FHIR Implementation guide that provides details on how to transform healthcare data from FHIR to the OMOP Common Data Model. It aims to bridge the gap between these two widely used formats in healthcare and research. The standard defines mappings between FHIR resources and OMOP data tables, focusing on commonly used EHR data.
| [FHIRconnect](https://sevkohler.github.io/FHIRconnect-spec/build/site/FHIRconnect/v1.0.0/index.html) | **FHIRconnect** is a mapping specification for bidirectional mapping between openEHR and FHIR. The goal is to create a mapping language that communities can use to transform data between these standards. The markup language used to express the mappings is YAML. |
| [openEHR to OMOP](https://github.com/SevKohler/Eos) | The **EOS** research project has developed an ETL engine to transform openEHR into OMOP. |





Er zijn reeds verschillende thesauri beschikbaar, maar die worden nog te weinig gebruikt. Er zijn ook al vertalingen tussen verschillende thesauri

- DHD diagnose thesaurus: koppelt ICD10, Snomed en het Nederlandse DBC systeem
- DHD verrichting thesaurus: ...
- Z-Index mapping naar RxNorm van ErasmusMC
- Artikel Cornet et al. van Z-index naar ATC naar RxNorm

De rol van generatieve AI c.q. LLMs: hulpmiddel om ongestructureerde data (vrij tekst) om te zetten naar gestructureerde data (in een gekozen informatiemodel, gecodeerd met een gekozen terminologieyysteem)

