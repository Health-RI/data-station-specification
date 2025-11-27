# Data zoeken en vinden (data discovery)

Het zoeken en vinden van data is de eerste stap in het hele proces. Een potentiële aanvrager — zoals een onderzoeker of een beleidsdepartement — wil eerst ontdekken welke data over een bepaald onderwerp beschikbaar zijn en onder welke voorwaarden deze kunnen worden gebruikt. Dit zoeken gebeurt via een nationale catalogus van gezondheidsgegevens. Op Europees niveau worden deze nationale catalogi ontsloten via het centrale platform van HealthData@EU (hierna: het centrale platform).

Het publiceren en beheren van een nationale catalogus van gezondheidsinformatie is een taak van de HDAB, zoals vastgelegd in artikel 57 van de EHDS.

## Overzicht van de usecases

```puml
@startuml

actor "Time\n(ding)" as T
actor "Dataleverancier\n(organisatie)" as DL_I
actor "Dataleverancier\n(organisatie)" as DL_O
actor "Nationaal Contactpunt voor e-Health(systeem)" as MSB
actor "Publiek\n(mens of organisatie)" as B

rectangle "Nationale Catalogus van Gezondheidsgegevens" {
  usecase "Meld\ndatacatalogus aan" as UC1
  usecase "Haal datacatalogus\nvan dataleverancier op" as UC2
  usecase "Zoek datasets" as UC3
}

DL_I --> UC1
T --> UC2
B --> UC3

UC2 --> DL_O
UC2 --> MSB

@enduml
```

### Welke data wordt gepubliceerd in de catalogus


