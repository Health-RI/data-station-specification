# 2.1. Finding data (_data discovery_)

Finding data is the first step in the entire process. A potential applicant — such as a researcher or a policy department — first wants to discover what data on a given topic is available and under what conditions it can be used. This search takes place via a National catalogue of datasets. At European level, these national catalogues are made accessible through the central platform of HealthData@EU (hereafter: the central platform).[^1]

Publishing and managing a National catalogue of datasets is a task of the HDAB, as laid down in Article 57(1j) of the EHDS[^2].

!!! info "Data user versus data holder"

    In the use cases we deliberately use the term data holder instead of data owner. This creates a clear distinction between the responsibility of an organisation that holds health data (data owner) and an organisation that holds health data and is required to make it available (data holder). Article 50 of the EHDS identifies a number of exceptions under which data owners are not required to provide health data.

## 2.1.1. Overview of use cases

In the overview of the use cases, the actor time is shown to indicate that this use case is executed periodically. Within the National catalogue system for datasets, these periods are scheduled to retrieve the catalogue from data holders. Data holders have set up a data station on which the catalogue is published.

![](uc-vinden.drawio.svg)

///caption
**Figure 2.** Overview of the use cases for finding and discovering datasets.
///

The use cases from the diagram are briefly described in the following sections.

## 2.1.2. Register catalogue

Data holders compile a catalogue and publish it for at least the datasets they manage that fall under the categories of Article 51 of the EHDS. The holder then ensures that this catalogue is accessible to all participants in the data space via the data station.

The data holder only needs to register the catalogue once. In doing so, they provide the address (URL) of the data station on which the catalogue has been published. This step is mandatory in accordance with Article 60 of the EHDS. At least once a year, the data holder must renew the dataset descriptions.

## 2.1.3. Update National catalogue with catalogues from data holders

The system periodically checks whether the data holder's catalogue has been updated. The catalogue is then downloaded and integrated into the public National catalogue of datasets. Only the catalogue of a data holder that has registered will be checked.

As manager of the National catalogue of datasets, the HDAB will forward the National catalogue to the central platform of HealthData@EU. This takes place after the catalogues of all registered data holders have been processed. The catalogue is transmitted via the National contact point.

## 2.1.4. Search datasets

A researcher or other party can search the National or European catalogue for relevant datasets. The description of the datasets must contain sufficient information to determine which data can be used for one of the purposes mentioned in Article 53 of the EHDS. The format of the catalogue is described in (the supported version(s) of) HealthDCAT-AP.[^3]

!!! info "Which data is published in the catalogue"

    All categories of electronic health data in accordance with Article 51 of the EHDS must be available for secondary use. For data from electronic health records, we proceed as far as possible on the basis of data availability in one or more of the three most commonly used clinical information models, namely FHIR, OMOP and openEHR.[@tsafnat2024converge] For data for which that is not possible, such as administrative data in the field of healthcare (Article 51(1)(e)) and data relating to health workers (Article 51(1)(j)), no information model is prescribed in advance. In the KIK-V example, RDF was chosen as the standard, but this may differ for different categories. The FAIR principles are the most generic guideline for making these choices and achieving interoperability.[^4] The metadata is always in the HealthDCAT-AP standard, which is based on RDF.


[^1]: More about the architecture of HealthData@EU can be found on the [documentation website](https://acceptance.data.health.europa.eu/healthdata-central-platform/documentation?locale=en).

[^2]: European Parliament and Council. (2025). Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2025/327/

[^3]: Chouaiech, M., Derycke, P., Van Nuffelen, B. et al. (2025, September 22). HealthDCAT-AP Release 5. EC DG-SANTE. https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/ 

[^4]: Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. (2016, March 15). The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data. https://rdcu.be/eSNTr
