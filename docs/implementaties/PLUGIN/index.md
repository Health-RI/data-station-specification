# PLUGIN Healthcare

Het Platform voor Uitwisseling en Hergebruik van Klinische Data Nederland (PLUGIN) beoogt klinische data in de  Elektronische Patiëntendossiers (EPDs) van Nederlandse ziekenhuizen te ontsluiten op een veilige, schaalbare en duurzame wijze. PLUGIN is van oorsprong een initiatief van [Dutch Hospital Data](https://www.dhd.nl/), [Integraal Kankercentrum Nederland](https://iknl.nl/) en [Expertisecentrum Zorgalgoritmen](https://zorgalgoritmen.nl/) De basis infrastructuur maakt gebruik van [vantage6](https://vantage6.ai/) en maakt het mogelijk medische data decentraal beschikbaar te stellen voor zowel algemene gegevensuitwisseling als federatief leren en analyseren. 

Met use-cases [AI-ondersteund coderen](https://www.dhd.nl/producten-diensten/registratie-data/ondersteuning-bij-medische-codering/ai-ondersteund-coderen) en [het vullen en verrijken van de NKR](https://www.icthealth.nl/nieuws/veilig-en-efficient-data-delen-dankzij-het-plugin-initiatief) is aangetoond dat de infrastructuur schaalbaar in kan worden gezet voor de drie soorten van gefedereerde gegevensbewerking:

De PLUGIN infrastructuur implementeert verschillende componenten zoals in onderstaand diagram en tabel is weergegeven en worden in de volgende pagina's uitgelegd.

![](./plugin-overzicht.drawio.svg)

!!! note "Lijst van componenten"

    | Component | Functie |
    |:----|:---------|
    | PLUGIN-Analytics | gefedereerde analyse |
    | PLUGIN-ML | gefedereerd leren |
    | PLUGIN-Hub | data pooling |
    | vantage6 server | centrale processing hub waarop gebruikers, organizaties, samenwerkingsverbanden taken en resultaten worden beheerd en georchestreerd |
    | vantage6 UI | webapplicatie waarmee gebruikers kunnen interacteren met de server |
    | vantage6 API | programmatische aansturing van de server, incl. Python client en R client |
    | Docker registry | containers die zijn geautoriseerd om decentraal op de datastations uit te voeren |
    | Algorithm store | de metadata over de (algoritme) containers, inclusief ondersteuning van goedkeuringsproces |
    | vantage6 node | decentrale component van processing hub die de lokale berekeningen uitvoert |
    | algoritme container | tijdelijke lokale kopie van het algoritme dat wordt uitgevoeerd, wordt aangemaakt en verwijderd door de vantage6 node |
    | PLUGIN-Lake | Lakehouse voor serverless opslag en ETL transformaties op het datastation |


??? info "Externe documentatie"

    - [PLUGIN programma website](https://plugin.healthcare/)
    - [Installatiegids AI-ondersteund coderen](https://installatiegids-aioc.dhd.nl/)
    - [vantage6 gebruikersdocumentatie](https://docs.vantage6.ai/en/main/)
    - [vantage6 journal paper](https://vantage6.ai/documents/7/moncada-torres2020vantage6_57GU4Gt.pdf)
    - [vantage6 software management plan](https://vantage6.ai/documents/27/vantage6-software-management-plan-v1.0.pdf)