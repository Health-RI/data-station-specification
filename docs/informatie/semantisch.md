# 3.2. Semantische interoperabilitieit[^1]

## 3.2.1. Het probleem van semantische interoperabiliteit

Semantische interoperabiliteit gaat verder dan gedeelde gegevensformaten of gemeenschappelijke terminologieën - het vereist dat verschillende systemen uitgewisselde gegevens op dezelfde manier interpreteren. Het bereiken hiervan hangt af van hoe goed de ontologie van elk systeem de beoogde betekenis van de concepten die het gebruikt vastlegt. De volgende diagrammen illustreren hoe systemen kunnen verschillen in hun benadering van een gedeelde conceptualisatie, en hoe deze verschillen hun vermogen om betekenisvol samen te werken beïnvloeden.

![](https://health-ri.github.io/semantic-interoperability/semantic-interoperability/assets/images/semantic-interoperability-systems-all.png)

Bovenstaand diagram illustreert hoe drie verschillende systemen proberen dezelfde conceptualisatie te representeren - d.w.z. een gedeeld begrip van de echte wereld - maar met verschillende niveaus van succes. Elk systeem gebruikt een andere ontologie om zijn interne model te beperken, wat leidt tot verschillen in hoe getrouw ze de beoogde betekenis vastleggen.

- Systeem A (links) vertegenwoordigt een ideaal geval. Zijn ontologie sluit nauw aan bij de beoogde semantiek (groene gebied), zonder extra interpretaties toe te voegen of geldige uit te sluiten. Dit wordt beschreven als een nauwe benadering van de beoogde modellen - een zeer wenselijke, hoewel vaak moeilijk te bereiken, situatie voor semantische interoperabiliteit.

- Systeem B (midden) gebruikt een meer permissieve ontologie. Het rode gestippelde gebied toont onbedoelde modellen die logisch consistent zijn met het formalisme van Systeem B maar afwijken van de beoogde betekenis. Een dergelijke overgeneralisatie kan leiden tot **valse overeenstemming**: systemen die interoperabel lijken omdat ze hetzelfde vocabulaire gebruiken, maar de termen eigenlijk verschillend interpreteren.

- Systeem C (rechts) maakt de tegenovergestelde fout. Zijn ontologie is te restrictief: het blauw gestreepte gebied vertegenwoordigt geldige betekenissen waarmee het geen rekening houdt. Dit kan gebeuren wanneer de beperkingen van een systeem te smal of onvolledig zijn, wat leidt tot de uitsluiting van noodzakelijke interpretaties en verlies van informatie.

Echte semantische interoperabiliteit vereist dus meer dan syntactische of logische afstemming. Het vereist een gedeeld wereldbeeld - een convergentie over wat bestaat, hoe het kan worden beschreven, en welke interpretaties geldig zijn.


## 3.2.2. Hoe wordt Semantische Interoperabiliteit Bereikt?

Het bereiken van semantische interoperabiliteit omvat verschillende stappen:

- **Gestandaardiseerde vocabulaires en ontologieën:** Gebruik van gedeelde terminologieën zoals SNOMED CT, LOINC, of domein-specifieke ontologieën om consistent begrip van gegevenselementen te waarborgen.
- **Metadata en annotaties:** Semantische lagen aan gegevens toevoegen met behulp van RDF, OWL of JSON-LD om context en betekenis te bieden.
- **Mappings en afstemmingen:** Links creëren tussen verschillende vocabulaires of datasets om gegevensintegratie en interoperabiliteit te vergemakkelijken.
- **Tools en platformen:** Gebruik van interoperabiliteitskaders, API's en kennisgrafen om naadloze gegevensuitwisseling en begrip te ondersteunen.
- **Ontologisch gefundeerde talen:** Gebruik van modelleertalen die helpen om de ontologische aannames die zijn ingebed in gegevens en systemen expliciet uit te drukken. Zoals Guizzardi betoogt, is het niet genoeg dat representatietalen formeel expressief zijn - ze moeten gebruikers ondersteunen bij het articuleren en verifiëren van de werkelijke semantiek van hun modellen door middel van ontologische verplichtingen. OntoUML is zo'n taal - expliciet gefundeerd in de Unified Foundational Ontology (UFO) - die semantisch rijke, intern consistente en verifieerbare conceptuele modellering mogelijk maakt.

[^1]: De tekst op deze pagina is grotendeels overgenomen uit het [Semantic Interoperability](https://health-ri.github.io/semantic-interoperability/semantic-interoperability) initiatief van Health-RI. Daar waar dat initiatief zich richt op een zeer gedegen analyse en oplossing van het semantische interoperabiliteitsprobleem, nemen wij voor de datastation specificatie een meer pragmatische aanpak.


## 3.2.3. Implicaties voor datastations

- HRI project richt zich op ontological alignment
- Wij richten ons meer pragmatisch op mappings tussen meest gebruikte thesauri en ontologieen
    - [SSSOM](https://github.com/mapping-commons/sssom) icm met [SEMAPV](https://github.com/mapping-commons/semantic-mapping-vocabulary) geeft basis om dit op een gestandaardiseerde manier te doen
    - Er zijn al mapping beschikbaar, bijvoorbeeld voor aandoeningen en medicatie
    - In de opschaling van datastations zouden we in Nederland kunnen samenwerken om bestaande mappings in SSSOM + SEMAPV beschikbaar te stellen
        - DHD Diagnose- en Verrichtingenthesaurus
        - Z-Index mapping naar RxNorm van ErasmusMC
        - Artikel Cornet et al. van Z-index naar ATC naar RxNorm

- Een andere aanpak gebruikt RDF en graaftechnologie om verschillende datasets te integreren, vergelijkbaar met Zwitserse SPHN [@gouthamchand2024makinga]. Maar is het dan niet makkelijker om data tijdelijk naar centrale BVO te sturen en daar door gebruiker te laten integreren?
- Voor specifieke domeinen zoals radiomics, vergt het realiseren van semantische interoperabiliteit zeer specialistische kennis [@kalendralis2020faircompliant]. Ook daar pragmatischer om dat in centrale BVO te doen, totdat we beter zicht hebben hoe de data (in dit geval radiology beelden) het beste generiek beschikbaar gesteld kunnen worden.




