# Informatie

## Use Cases

Een vijftal use cases worden in PLUGIN uitgewerkt:

* [AI-ondersteund coderen](https://www.dhd.nl/producten-diensten/registratie-data/ondersteuning-bij-medische-codering/ai-ondersteund-coderen)
* [het vullen en verrijken van de NKR](https://www.icthealth.nl/nieuws/veilig-en-efficient-data-delen-dankzij-het-plugin-initiatief)
* Signalering van metastasen op afstand
* Dashboard voor de Palliatieve Zorg
* Voorspellen klinische verslechtering, delier, en kwetsbaarheid na ontslag

### AIOC

Medisch codeurs leggen de aandoeningen waaraan patiënten lijden vast in ICD-10 codes. Leidend hierbij zijn de brieven en verslagen die medisch specialisten hebben geschreven over de patiënt, de aandoeningen waaraan de patiënt lijdt en de behandelingen die de patiënt ondergaat. vanaf 2023 is de codering van dagopnamen verplicht. Echter, de kwaliteit en uniformiteit van de diagnoseregistratie van dagopnamen in de LBZ nam al jaren af. Daarnaast neemt het aantal medisch codeurs in ziekenhuizen drastisch af.

Daarom is besloten om een AI-model te ontwikkelen dat automatisch dagopnamen kan voorzien van een ICD-10 codering. Het NLP-model (AI) is ontwikkeld op ongestructureerde data (ontslabrieven, polibrieven, OK-verslagen en PA-verslagen). Het model is momenteel (okt 2023) in staat om 70% van de dagopnamen te voorzien van een automatische codering. Het AI-model heeft aan de hand van honderdduizenden opnamen, ICD-10 coderingen en miljoenen brieven en verslagen verbanden leren leggen tussen de termen die medisch specialisten gebruiken om de aandoeningen van de patiënten te omschrijven en de ICD-10 codes waarmee deze aandoeningen dienen te worden gecodeerd. Het AI-model is nu in staat om een substantieel deel (gemiddeld 65%) van de codering van de dagopnamen van medisch codeurs uit handen te nemen. Hierdoor krijgen medisch codeurs meer ruimte om zich te richten op ingewikkelder codeerwerk, zoals dat van de klinische opnamen.

## Data

Om de interoperabiliteit van data te garanderen (zie Semantische en syntactische interoperabiliteit) voor het trainen en toepassen van modellen binnen PLUGIN, wordt EPD-data gestandaardiseerd naar een landelijk model, uitgedrukt in [FHIR profielen](https://plugin.healthcare/fhir/artifacts.html#plugin-profielen). Vereiste data wordt door middel van extractiescripts en handmatig werk klaar gezet in een uniforme standaard, en in een vaste folderstructuur. De gefedereerde analyses, modellen en vragen kunnen hierdoor uitgaan van vaste terminologie en locaties van data, ongeacht op welke node ze worden uitgevoerd. Dankzij deze standaardisering is data hierna voor meerdere doeleinden bruikbaar.

### Data-extractie

De extractie en standaardisering van EPD-data naar de gewenste FHIR profielen is afhankelijk van de EPD-leverancier. In het geval van Chipsoft Hix is scripting beschikbaar. In het geval van dagopname gerelateerde brongegevens biedt Epic functionaliteit aan voor het exporteren hiervan.Data dient te worden gepseudonimiseerd voordat het beschikbaar wordt gemaakt in het data station. Hiervoor zijn voor zowel EPIC als Chipsoft HiX scripts. In het geval van AIOC worden gegevens beschikbaar gesteld op het niveau van de individuele opname, informatie over zorgactiviteiten en ongestructureerde data. Deze data is afkomstig uit ontslagbrieven, polibrieven, operatieverslagen en de PA-verslagen.
# Gebruik van informatiemodellen en thesauri in PLUGIN


## Informatiemodellen voor syntactische interoperabiliteit

Ten tijde van het schrijven van dit document heeft PLUGIN gewerkt met twee verschillende informatiemodellen die elk in een afzonderlijke usecase zijn beproefd c.q. geimplementeerd.

!!! note "Informatiemodellen in PLUGIN"

    === "FHIR"

        Vanuit het originele ontwerp heeft PLUGIN in het gebruik van FHIR geprioriteerd. De overwegingen om dit informatiemodel te gebruiken is beschreven in een artikel door Kapitan et al. (2025).[@kapitan2025data] Een van de belangrijke principes hierin is dat van late-binding: doordat PLUGIN is bedoeld als generieke infrastructuur, is de gedachte dat het opleggen van condities en restricties in de binnenkomende data stapgewijs kan worden gedaan. Uitgaande van FHIR R4 als basis, wordt de data 'getrechterd' naar steeds specifiekere profielen, zijnde het zibs2020 profiel, nl-core en het profiel van de uiteindelijke toepassing, in dit geval de NCR-EHR profiel van de Nederlandse Kankerregistratie. 
        
        ![](./late-binding.png)

        Deze aanpak is succesvol beproefd in een usecase met het RadboudUMC, waarbij gegevens voor hoofd-halskanker automatisch uit de Epic FHIR v3 API zijn onttrokken en vertaald naar het target profiel.

    === "AI-ondersteund coderen"

        Voor het project "AI-ondersteund coderen" wordt een specifieke set gegevens gebruikt. DHD heeft hiervoor een AI-model ontwikkeld dat op basis van ongestructureerde data (brievenverslagen) automatisch ICD-10 codes kan genereren voor dagopnames. 
        
        Deelnemende ziekenhuizen leveren hiervoor een dataset aan die bestaat uit:
        
        *   Brievenverslagen
        *   Diagnoses
        *   Opnames
        *   Subtrajecten
        *   Zorgactiviteiten

        Binnen het project worden deze gegevens middels gestandaardiseerde extractiescript uit het bronsysteem onttrokken, zijnde Epic of Chipsoft HiX. Het [AIOC informatiemodel](https://plugin.healthcare/fhir/artifacts.html#logical-models-aioc) is een subset van de [Landelijke Basisregistratie Ziekenhuiszorg](https://www.dhd.nl/producten-diensten/registratie-data/ontdek-de-mogelijkheden-van-de-lbz/hulpmiddelen-lbz), een informatiemodel wat sinds 2014 in gebruik is. In principe kan het LBZ model gemapped worden naar FHIR, OMOP of openEHR, maar dit is nog niet gedaan.

In de doorontwkkeling van PLUGIN is voorzien dat andere informatiemodellen (OMOP, openEHR) ondersteund gaan worden, met gebruik van de gestandaardiseerde transformaties tussen de drie informatiemodellen zoals is beschreven in de sectie over [syntactische interoperabiliteit](../../informatie/syntactisch.md).


## DHD thesauri als basis voor semantische interoperabiliteit

Voor semantische interoperabiliteit leunt PLUGIN sterk op de expertise en standaarden van DHD (Dutch Hospital Data), en specifiek de [Diagnose- en Verrichtingenthesaurus](https://www.dhd.nl/producten-diensten/registratie-data/oplossingen-voor-registratievraagstukken). Deze thesauri zijn zijn de landelijke standaarden voor de registratie van medische diagnosen respectievelijk verrichtingen. De thesauri bestaan uit lijsten met uniforme termen die worden ingeladen in het epd. Hierdoor kunnen artsen en andere zorgprofessionals de termen aan de bron vastleggen in de taal die zij in de praktijk gebruiken. Elke twee maanden verschijnen nieuwe versies, zodat de lijsten altijd actueel zijn. Door deze thesauri te gebruiken, zorgt PLUGIN ervoor dat analyses die over verschillende ziekenhuizen heen worden uitgevoerd, gebaseerd zijn op data met een consistente en gedeelde betekenis. Zo kunnen concepten automatisch worden afgeleid naar DBC-codes, ICD-10-codes, conciliumcodes (opleidingscodes) en het internationale terminologiestelsel SNOMED.

In de doorontwikkeling van PLUGIN wordt gedacht om de thesauri uit te breiden met de [SSSOM-methode](https://mapping-commons.github.io/sssom/). Daarmee kunnen niet alleen mappings tussen verschillende codestelsel gemaakt worden, maar kan ook aangegeven worden of een mapping een `exactMatch`, een `broadMatch` of een `narrowMatch` is. Dit is van waarde omdat bijvoorbeeld in de huisartsen zorg veel bredere diagnosen worden geregistreerd zoals epilepsie, terwijl in een ziekenhuis of UMC in meer detail de diagnose wordt gecodeerd, bijvoorbeeld focale epilepsie.
