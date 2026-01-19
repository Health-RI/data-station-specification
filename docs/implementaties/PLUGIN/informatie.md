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
