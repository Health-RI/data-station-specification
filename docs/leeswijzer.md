# Vraagestelling en leeswijzer


## Centrale ontwerp- en onderzoeksvragen

In dit document wordt de architectuur van een federatieve BVO uitgewerkt dat kan worden implementeerd als onderdeel van een landelijk dekkend basisinfrastructuur voor voor secundair gebruik van data. Daarbij staan de volgende ontwerp- en onderzoeksvragen centraal:

- Kan een eenduidige functionele en technische specificatie gegeven worden van federatieve BVOs gebaseerd op data stations, dat consistent is met bestaande referentie architecturen?
- Op welke manier zouden data stations gestandaardiseerd kunnen worden om te komen tot maximale interoperabiliteit van federatieve BVOs?
- Op welke manier kunnen hybride BVOs, zijnde een synergie tussen federatieve en centrale BVOs, gerealiseerd worden en welke mogelijkheden zijn er om hierin tot standaardisatie te komen?
- Zijn er lancunes danwel tegenstrijdigheden in de huidge benadering van de EHDS voor secundair gebruik die het gebruik van federatieve BVOs in de weg staan? Zo ja, welke oplossingsrichtingen zijn er?
- Wat is de volwassenheid van de bestaande referentie implementaties ten opzichte van bovengenoemd ontwerp:
    - KIK-V als referentie implementatie van data stations voor gefedereerde analyse
    - PLUGIN/vantage6 als referentie implementatie van data stations voor gefedereerde analyse en gefedereerd leren


## Leeswijzer

Dit document is als volgt opgesteld. In het hoofdstuk **Architectuur** allereerst een algemene beschrijving gegeven van data spaces. Hierbij worden de basisprocessen van data aanvraag tot data gebruik en publicatie beschreven in termen van use cases, waarbij we gebruik maken van de [Use Case 3.0](https://www.ivarjacobson.com/files/use-case_3.0_v1.0.pdf) modeleringstechniek. De relevante concepten binnen de architectuur van een data space worden toegelicht, om daarmee de context van een data station helder in beeld te hebben. Waar nodig wordt verwezen naar een [Archimate model van de data space](https://health-ri.github.io/data-spaces-archimate/).

De sectie **Functionele componenten** gaat in meer detail in op de verschillende componenten van de federatieve BVO en het data station _an sich_. De specificaties van TEHDAS2 worden als startpunt gebruikt en nader uitgewerkt. Vervolgens wordt met deze beschrijving van de componenten de verschillende **Implementaties** geanalyseerd en beschreven. Tot slot wordt in **Discussie** de belangrijkste bevindingen op een rij gezet in relatie tot de vraagstelling en suggesties gedaan voor verdere ontwikkeling in de toekomst.

