## Data Station

### Request Data Extraction

**Goal**: DAAMS vraagt om de dataproducten te extraheren en beschikbaar te stellen aan een Health Data User.

**Primary Actor**: Data Access Application Management System (DAAMS) (systeem)


### Execute Algorithm

**Goal**: Federated Analytics Portal vraagt om uitvoering van een algoritme en retournering van de resultaten

**Primary Actor**: Federated Analytics Portal (systeem)


### Process Data Request

**Goal**: Federated Analytics Portal verzoekt om data op basis van een vraag.

**Primary Actor**: Federated Analytics Portal (systeem)

**Preconditions**: 


**Main Success Scenario:**

1. Federated Analytics Portal verzend een bericht met het dataverzoek
2. Het systeem registreert het ontvangen bericht in het logboek
3. Het systeem verifieert de authenticeert de verzender van het bericht
4. Het systeem verifieert het dataverzoek
5. Het systeem voert de technische vraagstelling uit
6. Het systeem stelt een bericht samen met het antwoord op de vraag
7. Het systeem verzend het bericht naar het Federated Analytics Portal
8. Het systeem registreert het verzonden bericht in het logboek

**Extension Points:**


**Post-conditions**

- De vraag is beantwoord en geretourneerd