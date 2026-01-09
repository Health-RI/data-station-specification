#  3. Perspectief: informatie
## Semantische en syntactische interoperabiliteit

Om gezondheidsgegevens zinnig te kunnen hergebruiken moet de vorm (syntax) en betekenis (semantiek) vergelijkbaar en uitwisselbaar zijn. Deze twee vormen van interoperabiliteit zijn essentiele randvoorwaarden. Om te begrijpen hoe computers met elkaar "praten", kunnen we dit vergelijken met hoe mensen communiceren.

* **Syntactische interoperabiliteit (de envelop & de grammatica):**
    Dit gaat over de **vorm** en de **structuur** van het bericht, zoals bijvoorbeeld een brief. Syntactische interoperabiliteit betekent dat de ontvanger de brief fysiek kan openen, herkent dat het een brief is, en dat zij de letters kan lezen (bijvoorbeeld het Latijnse alfabet). In de computerwereld betekent dit dat twee systemen elkaars bestanden technisch kunnen openen en de structuur herkennen (bijv. "hier staat de naam", "daar staat de datum").
    
    !!! info "Analogie"
    
        Ik stuur jou een zin die grammaticaal perfect klopt: *"De blerf schrobt de grakker."* De ontvanger kan de zin lezen (syntax is correct), maar heeft geen idee wat de verzender ermee bedoelt te zeggen.

* **Semantische interoperabiliteit (de betekenis):**
    Dit gaat over de **inhoud** en het **begrip**. Als de brief eenmaal is geopend, willen we begrijpen wat er staat. We moeten dezelfde taal spreken en dezelfde definities gebruiken. Als ik "bank" schrijf, moet de ontvanger weten of ik een zitmeubel bedoel of een geldinstelling.
    
    !!! info "Analogie"
    
        Om *"De blerf schrobt de grakker"* te begrijpen, hebben we een woordenboek nodig dat uitlegt wat een 'blerf' is. Semantische interoperabiliteit zorgt ervoor dat de computer niet alleen "180" ziet staan, maar begrijpt dat dit een "bloeddruk" is in "mmHg".


## Informatiemodellen voor syntactische interoperabiliteit
Om gegevens technisch uit te wisselen, hebben we standaarden nodig die de **structuur** bepalen.In de zorg kent vele informatie modellen, maar in de afgelopen jaar is de sector aan het convergeren naar openEHR, OMOP en FHIR als de belangrijkste informatiemodellen.[@tsafnat2024converge] Hoewel ze ook betekenis (semantiek) bevatten, is hun belangrijkste functie dat ze de "container" voor de data.



=== "FHIR"

    Fast Healthcare Interoperability Resources (FHIR) richt zich vooral op het uitwisselen van gegevens, bijvoorbeeld tussen een ziekenhuis en een app op je telefoon. Het gebruikt hiervoor informatiebouwstenen: er is een kaartje voor 'Patiënt', een kaartje voor 'Medicatie', etc. Het is heel flexibel en modern, vergelijkbaar met hoe internetpagina's werken. De syntax van FHIR schrijft voor hoe de digitale berichten eruit moeten zien. FHIR is populair omdat het dezelfde technische standaarden gebruikt als het Internet, waardoor het voor ontwikkelaars van applicaties makkelijk is om mee te werken.
    
=== "openEHR"

    openEHR is vooral gericht op het langdurig en zeer gedetailleerd vastleggen van medische dossiers, onafhankelijk van leveranciers. Ook openEHR werkt met het concept van informatiebouwstenen, maar doet dit om een meer geavanceerde manier dan FHIR of OMOP. Zo worden niet alleen elementaire bouwstenen gedefinieert, maar kunnen samengestelde medische concepten worden gedefineerd met zogenaamde archetypen. Qua syntactische interoperabiliteit richt openEHR zich vooral op de structuur voor **opslag**. Waar FHIR zich richt op het *versturen* van de brief, richt openEHR zich op hoe je het dossier in de kast *archiveert* zodat het over 20 jaar nog steeds leesbaar is.

=== "OMOP"

    De Observational Medical Outcomes Partnership (OMOP) standaard 
    * *Doel:* Grootschalig wetenschappelijk onderzoek en data-analyse over meerdere ziekenhuizen of landen heen.
    * *Hoe het werkt:* OMOP dwingt data uit allerlei verschillende systemen in één universeel tabel-formaat (het Common Data Model). Het zet alle data om naar een standaardtaal zodat onderzoekers één vraag ("Hoeveel mensen kregen griep na medicijn X?") aan honderd verschillende databases kunnen stellen.
    * *Syntactische rol:* Het standaardiseert de database-structuur voor **analyse**.


## _Knowledge organisation systems_ voor semantische interoperabiliteit

Semantische interoperabiliteit is erop gericht om verschillende computersystemen gegevens te kunnen laten uitwisselen met een ondubbelzinnige, gedeelde betekenis. In tegenstelling tot syntactische interoperabiliteit, die zich richt op het formaat van gegevensuitwisseling, zorgt semantische interoperabiliteit ervoor dat de betekenis van de gegevens behouden blijft en consistent wordt begrepen tussen verschillende systemen. Om semantische interoperabiliteit te realiseren is een _knowledge organisation system_ (KOS) nodig dat bestaat uit verschillende componenten.

| Doel | Voorbeeld | KOS component | Voorbeelden zorg |
|:----------|:----------|:---------|:-----------------|
| **Herkennen van synoniemen** | Emmentaal, als in Emmentaler kaas | Woordenlijsten, synoniem lijsten | Pinkhof compact medisch woordenboek |
| **Verklaren van dubbelzinnigheid (ambiguiteit)** | Emmentaal (als kaas) is niet hetzelfde als Emmental (de vallei) | _Authority file_ | Medical Subject Headings (MeSH) |
| **Hierarchische relaties** | Emmental is een koeienmelkse kaas<br>Koeienmelkse kaas is een kaas<br>Emmentaal (vallei) is onderdeel van Zwitserland | Taxonomie | ICD10, ATC |
| **Associatieve relaties** | Emmentaler kaas is gerelateerd aan koeienmelk<br>Emmentaler kaas is gerelateerd aan Emmentaal (vallei) | Thesaurus | RxNorm, DHD Diagnose- en verrichtingenthesaurus |
| **Klassen, eigenschappen, restricties** | Emmental is een klasse van koeienmelkse kaas<br>Koeienmelkse kaas is een sub-klasse van kaas<br>Elke kaas heeft exact een land van herkomst<br>Emmental is gemaakt van koeienmelk | Ontologie | SNOMED CT, LOINC Ontologie, KIK-V ontologie |

??? info "Toelichting en voorbeelden KOS"

    De verschillende KOS componenten kunnen gezien worden als concentrische cirkels, waarbij woordenlijsten de meest basale component zijn en ontologieen het meest uitgebreide. Hieronder een paar voorbeelden.

    * **SNOMED CT** is een van de meest uitgebreide medische ontologieen. Het bevat concepten voor ziektes, symptomen, operaties, lichaamsdelen, etc. en associatieve relaties tussen deze concepten die bijvoorbeeld een relatie leggen tussen een symptoom en een aandoening.
    * **LOINC** is van oorsprong een taxonomie bedoeld voor lab-uitslagen en metingen. Het is recentlijk geintgreerd met SNOMED tot de [LOINC Ontology](https://loincsnomed.org/).
    * **RxNorm** is een van oorsprong Amerikaanse thesaurus voor medicijnen. , vooral sterk in de VS en gebruikt in internationaal onderzoek (zoals met OMOP). In Europa wordt toegewerkt naar het gebruik van **[IDMP](https://www.iso.org/obp/ui/en/#iso:std:iso:11616:ed-2:v1:en)**, wat een uitgebreidere set van standaarden is om medicijnen en medicinale producten eenduidig te herkennen. In Nederland gebruiken we voor de dagelijkse zorg (recepten, apotheek) vaker de **G-Standaard** (beheerd door Z-Index), maar voor internationaal onderzoek wordt dit vaak vertaald naar RxNorm.
    * **ICD-10** is een taxonomie die vooral wordt gebruikt voor statistiek en facturatie. Het groepeert ziektes in categorieën.

    Het is goed om op te merken dat alle syntatische standaarden (FHIR, OMOP, openEHR) altijd gebruik maken van meerdere KOS componenten. Op zijn moeten codelijsten (taxonomieen) gebruikt worden, in het meest uitgebreide geval wordt een ontologie gebruikt. Zo wordt SNOMED vrijwel altijd gebruikt bij implementaties van OMOP, openEHR en FHIR.

In het volgende wordt beschreven hoe syntactische en semantische gerealiseerd kan worden binnen de architectuur voor secundair gebruik van data.
