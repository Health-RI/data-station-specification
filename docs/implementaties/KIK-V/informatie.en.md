# 6.1.2. KIK-V implementation: information

## 6.1.2.1. Ontology

![](https://www.kik-v.nl/_next/image?url=https%3A%2F%2Fwww.kik-v.nl%2Fsite%2Fbinaries%2Fcontent%2Fgallery%2Fsite-content%2Fcontent-afbeeldingen%2Fplaatje-ontologie-voor-dummies.png&w=2560&q=70)

### What is an ontology

Within the KIK-V approach, ontology helps to create unambiguity so that everyone — from care providers to policymakers — speaks the same language. An ontology is a structured way of organising meaning and making it machine-readable. For example: in healthcare you have concepts (called *concepten* in KIK-V terminology) such as 'client', 'treatment' and 'invoice'. An ontology defines what these concepts mean and how they relate to one another. An ontology is therefore a knowledge model that helps people and information systems understand and process data about these concepts in a uniform way.

### Why is an ontology needed?

In care organisations, a great deal of information is recorded, but not always in the same way. One organisation speaks of a 'patient', while another says 'client'. This can be confusing when different parties want to exchange data.

The KIK-V ontology ensures that everyone in nursing home care speaks the same language, without the need to adapt existing data at source. A 'semantic layer' is, as it were, placed over the data, so that everyone understands the same information in the same way. This makes it easier to exchange data and to answer questions from government or other bodies unambiguously. A good example from the KIK-V ontology: instead of the term 'nursing home', a distinction is made between 'nursing home organisation' and 'nursing home building'. This immediately makes clear whether we are talking about the company providing the care or the physical building where people live.

### What is the ontology used for?

The KIK-V ontology is used to make information exchange in the Dutch nursing home care sector easier and more unambiguous. It consists of various components, for example for:

- Organisational structure
- Finance
- Care delivery
- Personnel

All of this information is publicly and freely available to view and download via the [KIK-V publication platform](https://kik-v-publicatieplatform.nl/). This allows providers in nursing home care and information-requesting parties working with KIK-V to view and use this information to collaborate more easily and share data.


## 6.1.2.2. Making data available

The [KIK-V step-by-step guide](https://www.kik-v.nl/starten-met-kik-v) describes how, at the start of implementation, an analysis is made of the available information and the approach to make it available. The analysis consists of:

- **Inventory of source systems**: source systems such as HRM, financial programmes and the EHR are mapped out.
- **Configuration of source systems**: assess whether the data needed to answer the questions is present in the source systems. Data that is missing, incomplete or incorrectly recorded in the source systems is designated as 'unavailable data'.

Using the so-called **reference designs**, it can be determined to what extent the **model dataset** — the total of data that can be used within the KIK-V approach — can be compiled in an automated manner.

### Reference designs

Reference designs form an important part of the implementation support provided by KIK-V. The reference designs detail, for many common applications, how the required data can be made available for calculating indicators. These reference designs were developed together with the vendors of the most commonly used systems. They can be used to determine to what extent the model dataset can be compiled automatically from the systems. They also provide insight into the adjustments that can be made to extract the remaining data from the systems.

As of December 2025, reference designs have been produced for [10 source systems](https://www.kik-v.nl/onderwerpen/r/referentieontwerpen), so that data holders need to perform as little of the mapping from the source system information model to the KIK-V ontology as possible themselves.

### Model dataset

The agreement set uses the model dataset to define the data that providers apply when formulating answers to the information questions described in an exchange profile. The model dataset is the result of the matching process — a coordination between information needs and data available at the care provider. The model dataset also includes the definitions of the data used.

The model dataset is used to give substance to the (concepts from the) information questions of consumers (data users) during data exchange. The set contains the semantics of the data that care providers make available for answering the questions. The semantics are uniformly recorded for all providers and consumers in an Ontology (a method for describing the meaning of concepts within a specific context).

Data holders can, whether or not in consultation with their software vendors, determine for themselves how to arrive at the correct mapping of data from the source data to the ontology (for the model dataset used). Data holders are themselves responsible for how they do this. This gives them the freedom to implement the link between source systems and the model dataset in their own way. The result of this is the provider dataset.

### Exchange profile

An exchange profile describes which questions are asked by an information-requesting party. This is a specific questionnaire per party and per subject. Each profile describes how the submitted answers are handled, what they are used for and how feedback to the care provider takes place. Various [exchange profiles](https://kik-v-publicatieplatform.nl/uitwisselprofielen) have been defined. To give an impression, here is an exchange profile in which the average number of staff members is calculated.

???+ abstract "Example exchange profile"

    #### Definitions

    * A person counts proportionally for the period during which he/she is a staff member in the quarter.
    * For example, during a quarter, a person who had an employment agreement for half of the quarter (and was therefore a staff member) counts as 0.5 in the calculation of the indicator. 
    * Both employed staff (PIL) and non-employed staff (PNIL) are included; trainees and volunteers are not.
    * Included in the [General Starting Points](https://kik-v-publicatieplatform.nl/documentatie/Algemene%20uitgangspunten/_) are: location, measurement period, care provider and the "Relationships between employment agreements, roles and groups".


    #### Explanation

    * The input parameter for this indicator is a year (yyyy), quarter (Qx) and the care office. The locations are shown by the care office region of the care office; this means that for some care providers only part of their locations are shown.

    #### Example

    The table below describes an example of how an employee counts in each of the categories. This employee had an employment agreement for half a quarter. The first half (one quarter of the quarter) the employee was a specialist in elderly medicine (a care provider function), the second half a manager (a non-care function).  

    | Classification | Care | Non-care | Total |
    |----------------|------|----------|-------|
    | Total organisation | 0.25 | 0.25 | 0.5 |
    | Location | 0.25 | 0.25 | 0.5 |


    #### Calculation

    1. Select all employment<sup>5</sup>, agency<sup>6</sup> and call<sup>7</sup> agreements (all subsets of employment agreement<sup>1</sup>) that overlapped with that quarter. This means the start date of the employment agreement<sup>1</sup> is before or on the end date of the quarter and the end date is not before the start of the quarter
    2. For these employment agreements<sup>1</sup>, select all employment agreement clauses<sup>2</sup> that overlap with the quarter.
    3. For these employment agreement clauses<sup>2</sup>, determine whether the function<sup>4</sup> is a care provider function<sup>3</sup>. 
    4. For these employment agreement clauses<sup>2</sup>, determine the location<sup>8</sup> and the person<sup>9</sup>.
    5. Calculate per person<sup>9</sup> the number of days that the employment agreement clauses overlapped with the quarter.
    6. Sum the numbers from step 5 per location<sup>8</sup>, for total, care<sup>3</sup> and non-care, and divide by the number of days in the quarter.
    7. For all locations<sup>8</sup>, retrieve the location number<sup>11</sup>. This is the input for the rows of the first column, classification. 
    8. Filter the locations<sup>8</sup> by care office region<sup>15</sup>. For this purpose, retrieve the localizable area<sup>12</sup> (the 6-digit postcode) for all locations<sup>10</sup>. Derive the first four digits from step 6; the derived postcode is used to look up a postcode area<sup>13</sup>. The postcode area<sup>13</sup> is part of an administrative area<sup>14</sup>, the care office region<sup>15</sup>.

    | Classification | Care | Non-care | Total |
    |----------------|------|----------|-------|
    | Total organisation | Step 6 | Step 6 | Step 6 |
    | Location 1 | Step 7 | Step 7 | Step 7 |
    | Location 2 | Step 7 | Step 7 | Step 7 |
    | Location *n* | Step 7 | Step 7 | Step 7 |

    #### Concepts and ontology

    * <sup>1</sup>. [employment agreement](http://purl.org/ozo/onz-pers#WerkOvereenkomst)
    * <sup>2</sup>. [employment agreement clause](http://purl.org/ozo/onz-pers#WerkOvereenkomstAfspraak)
    * <sup>3</sup>. [care provider function](http://purl.org/ozo/onz-pers#Zorgverlener%20(functie))
    * <sup>4</sup>. [function](http://purl.org/ozo/onz-g#OccupationalPositionRole)
    * <sup>5</sup>. [employment contract](http://purl.org/ozo/onz-pers#ArbeidsOvereenkomst)
    * <sup>6</sup>. [agency contract](http://purl.org/ozo/onz-pers#InhuurOvereenkomst)
    * <sup>7</sup>. [zero-hours contract](http://purl.org/ozo/onz-pers#OproepOvereenkomst)
    * <sup>8</sup>. [location](http://purl.org/ozo/onz-org#Vestiging)
    * <sup>9</sup>. [Person](http://purl.org/ozo/onz-g#Human) 
    * <sup>11</sup>. [location number](http://purl.org/ozo/onz-org#Vestigingsnummer)
    * <sup>12</sup>. [localizable area]( http://purl.org/ozo/onz-g#LocalizableArea)
    * <sup>13</sup>. [postcode area](http://purl.org/ozo/onz-g#PostcodeArea)
    * <sup>14</sup>. [administrative area](http://purl.org/ozo/onz-g#AdministrativeRegion)
    * <sup>15</sup>. [care office region](http://purl.org/ozo/onz-org#ZorgkantoorRegio)
