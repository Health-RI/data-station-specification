# 1.3. Vraagestelling en leeswijzer

## 1.3.1. Centrale ontwerp- en onderzoeksvragen

In dit document wordt de architectuur van een decentraal netwerk van BVOs uitgewerkt dat kan worden implementeerd als onderdeel van een landelijk dekkend basisinfrastructuur voor voor secundair gebruik van data. Daarbij staan de volgende ontwerp- en onderzoeksvragen centraal:

- Kan een eenduidige functionele en technische specificatie gegeven worden van een decentraal netwerk van BVOs gebaseerd op data stations, dat consistent is met bestaande referentie architecturen?
- Op welke manier zouden data stations gestandaardiseerd kunnen worden om tot maximale interoperabiliteit van een decentraal netwerk van BVOs te komen?
- Op welke manier kunnen kunnen data stations gebruikt worden voor data pooling naar een centrale TRE? Welke mogelijkheden zijn er om hierin tot standaardisatie te komen?
- Zijn er lacunes dan wel tegenstrijdigheden in de huidige benadering van de EHDS voor secundair gebruik die het gebruik van decentrale BVOs in de weg staan, met name in relatie tot data stations voor primair gebruik? Zo ja, welke oplossingsrichtingen zijn er?
- Wat is de volwassenheid van de bestaande referentie implementaties ten opzichte van bovengenoemd ontwerp:
    - KIK-V als referentie implementatie van data stations voor gefedereerde analyse;
    - PLUGIN/vantage6 als referentie implementatie van data stations voor i) gefedereerde analyse, ii) gefedereerd leren en iii) data pooling.


## 1.3.2. Leeswijzer

Dit document is als volgt opgesteld. In de sectie **Proces** wordt allereerst de basisprocessen van secundair gebruik beschreven, van data aanvraag tot data gebruik en publicaties. Daarbij gebruiken we de [Use Case 3.0](https://www.ivarjacobson.com/files/use-case_3.0_v1.0.pdf) modeleringstechniek. De relevante concepten binnen de architectuur van een data space worden toegelicht, om daarmee de context van een data station helder in beeld te hebben. Waar nodig wordt verwezen naar een [Archimate model van de data space](https://health-ri.github.io/data-spaces-archimate/). Het hoofdstuk over **Informatie** gaat in op semantische en syntactische interoperabiliteit als randvoorwaarde voor het (her)gebruik van gezondheidsgegevens. De sectie **Applicatie** gaat in meer detail in op de verschillende applicatie componenten van een decentrale en hybride BVO en het data station _an sich_. We volgen hierin het FAIR zandloper model als definitie van de lagen. Daarbij worden de specificaties van TEHDAS2 worden als startpunt gebruikt en nader uitgewerkt. De sectie **Infrastructuur** beschrijft vervolgens de fysieke technologie en standaarden die relevant zijn voor het realiseren van de applicatiecomponenten.

Nadat we vanuit verschillende perspectieven de architectuur hebben toegelicht, gaan we in **Implementaties** in op bestaande implementaties federatieve BVOs. Door met name KIK-V en PLUGIN als referentie implementaties te analyseren, willen we kritisch reflecteren op de voorgestelde specificatie van een data station voor secundair gebruik. Tot slot worden in **Discussie** de belangrijkste bevindingen op een rij gezet in relatie tot de vraagstelling en worden suggesties gedaan voor verdere ontwikkeling in de toekomst.

