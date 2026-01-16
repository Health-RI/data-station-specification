# PLUGIN Healthcare

Het Platform voor Uitwisseling en Hergebruik van Klinische Data Nederland (PLUGIN) beoogt klinische data in de  Elektronische Patiëntendossiers (EPDs) van Nederlandse ziekenhuizen te ontsluiten op een veilige, schaalbare en duurzame wijze. PLUGIN is van oorsprong een initiatief van [Dutch Hospital Data](https://www.dhd.nl/), [Integraal Kankercentrum Nederland](https://iknl.nl/) en [Expertisecentrum Zorgalgoritmen](https://zorgalgoritmen.nl/) De basis infrastructuur maakt gebruik van [vantage6](https://vantage6.ai/) en maakt het mogelijk medische data decentraal beschikbaar te stellen voor zowel algemene gegevensuitwisseling als federatief leren en analyseren. 

Met use-cases [AI-ondersteund coderen](https://www.dhd.nl/producten-diensten/registratie-data/ondersteuning-bij-medische-codering/ai-ondersteund-coderen) en [het vullen en verrijken van de NKR](https://www.icthealth.nl/nieuws/veilig-en-efficient-data-delen-dankzij-het-plugin-initiatief) is aangetoond dat de infrastructuur schaalbaar in kan worden gezet voor de drie soorten van gefedereerde gegevensbewerking:

* Gefedereerde analyse, zoals bijvoorbeeld het herkennen van patiënten voor klinische trials;
* Gefedereerd leren, zoals [AI-ondersteund coderen](https://www.dhd.nl/producten-diensten/registratie-data/ondersteuning-bij-medische-codering/ai-ondersteund-coderen)
* Gegevensuitwisseling, zoals [het vullen en verrijken van de NKR](https://www.icthealth.nl/nieuws/)

De PLUGIN infrastructuur implementeert de volgende componenten:

- Het datastation met de volgende componenten:
    - een Linux server waarop alle software componenten van het datastation zijn geimplementeerd;
    - PLUGIN-Lake (in ontiwkkeling) dat de ETL functies en het lakehouse implementeert;
    - de vantage6 node;
    - de lokale kopie van het algoritme dat wordt uitgevoeerd; dit is een tijdelijke component dat door de vantage6 node wordt aangemaakt en verwijderd als onderdeel van het federated processing proces.

- De processing hub met de volgende componenten:
    - een of meerdere Linux server waarop alle software componenten van de processing hub zijn geimplementeerd;
    - de vantage6 server zijnde de centrale processing hub waarop gebruikers, organizaties, samenwerkingsverbanden taken en resultaten worden beheerd en georchestreerd;
    - de vantage6 UI, een webapplicatie waarmee gebruikers kunnen interacteren met de server;
    - de vantage6 API, waarmee de server programmatisch aangestuurd kan worden en geintegreerd kan worden in workflows met gebruik van de Python client en/of de R client;
    - een Docker registry met daarin containers die zijn geautoriseerd om decentraal op de datastations uit te voeren;
    - een optionele _algorithm store_ om binnen een federatief netwerk verschillende soorten goedgekeurde berekeningen met elkaar te delen en federatief uit te voeren;



!!! info "Externe documentatie"

    - [PLUGIN programma website](https://plugin.healthcare/)
    - [Installatiegids AI-ondersteund coderen](https://installatiegids-aioc.dhd.nl/)
    - [vantage6 gebruikersdocumentatie](https://docs.vantage6.ai/en/main/)
    - [vantage6 journal paper](https://vantage6.ai/documents/7/moncada-torres2020vantage6_57GU4Gt.pdf)
    - [vantage6 software management plan](https://vantage6.ai/documents/27/vantage6-software-management-plan-v1.0.pdf)