## Federated Analytics Portal

### Sign Up

**Goal**: Health Data User meldt zich aan en registreert zich

**Primary Actor**: Health Data User (natuurlijk persoon of rechtspersoon)


### Register Algorithm

**Goal**: Health Data User registreert een algoritme voor analyse op gezondheidsgegevens

**Primary Actor**: Health Data User (natuurlijk persoon of rechtspersoon)

**Preconditions**: 

- De primaire actor is een geregistreerde gebruiker

**Main Success Scenario:**

- Health Data User start project voor gefedereerde analyse.
- Health Data User uploadt het algoritme en de bijbehorende configuratie, waaronder de coniguratie voor het bouwen van een image.
- Health Data User presenteert de vergunning voor toegang tot gezondheidsgegevens.
- Verzend algoritme en de configuratie naar DAAMS met een verzoek tot verificatie. Met het verzoek wordt de vergunning meegezonden.
- Het systeem wacht totdat DAAMS met een antwoord komt op het verzoek. Er is akkoord op het algoritme.
- Het systeem notificeert de Health Data User dat er akkoord is gegeven op het algoritme.
- Het systeem bouwt op basis van de configuratie een container image voor het algoritme
- Het systeem registreert het image in een gekwalificeerde Container Image Registry

**Extension Points:**


**Post-conditions**

- Image van de container met het algoritme is geregistreerd


### Conduct Federated Analytics

**Goal**: Health Data User ontvangt de resultaten van een federatieve data-analyse

**Primary Actor**: Health Data User (natuurlijk persoon of rechtspersoon)


### Conduct Descriptive Analytics

**Goal**: Health Data User ontvangt de resultaten van een verzoek om data

**Primary Actor**: Health Data User (natuurlijk persoon of rechtspersoon)