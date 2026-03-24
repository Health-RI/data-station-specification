# 2.3. Preparing data for processing (_data preparation_)

Data preparation begins once a data permit has been issued or a data request has been approved. After issuing the permit or approval, the HDAB sends a request to the data holders to prepare the data. Preparation covers the delivery of both personal data and non-personal data. Preparing the metadata description of datasets for the health data catalogue is not part of this process; it forms part of the data discovery process.

**Personal data**

When a data permit has been issued or a request has been approved, the health data must be made available in electronic form. This must happen within three months, with the possibility of extending this period once by a further three months if there are good reasons for doing so (Article 60(1) of the EHDS Regulation). The period starts when the HDAB informs the data holder of the permit or approved request, as described in Article 63(3).

In the case of data pooling, making data available means that health data from different data holders are brought together and combined into a single dataset, which is then used for data analysis in a secure processing environment. When the analysis is carried out in a federated manner, health data is not collected centrally but is made available for processing within the federated SPE. In that case, part of the data processing takes place on the data station (e.g. the first computation step or query), and the results of the computations are then combined in a second aggregation step. It is in this aggregation step that the privacy of data subjects must be safeguarded, for example by ensuring that results from data stations with few 'hits' — and thus a risk of re-identification — are nonetheless removed or masked.

**Non-personal data**

If an organisation holds non-personal electronic health data — such as anonymised data where individuals are no longer identifiable, synthetic datasets or data that does not concern individuals — these must be made available through public databases. These databases must meet standards for transparency, good governance and sustainable accessibility (Article 60(5)). No permit is required for these datasets and any interested party should in principle have free access to these data and be able to download them directly.

For health data that is subject to intellectual property rights or that contains trade secrets, it goes without saying that these are not included in a public database (Article 52). However, these data must still be made available for secondary use.

**Obligation**

Article 50 of the EHDS identifies a number of exceptions under which data owners are not required to provide health data. In the use cases, we therefore deliberately use the term data holder instead of data owner. This creates a clear distinction between the responsibility of an organisation that holds health data (data owner) and that of a party that must provide this data (data holder).

A data holder is obliged to make data available to the HDAB on the basis of a permit or an approved request. However, recital 80 of the EHDS emphasises the principle: "bring the questions to the data instead of moving the data". Therefore, the processes are based on a federated network in which data remains at the source as much as possible. This means that 'making data available' entails that, where possible, the data is made accessible to the data user at the source, without being transferred to the HDAB.

## 2.3.1. Overview of use cases

The HDAB uses a system for receiving and processing applications. Within the secondary use system, this system is called the Data Access Application Management System (DAAMS). From this system, the HDAB sends a request to make data available to the data station of a data holder. The data station is a system used for making data available for secondary use.

![](uc-klaarzetten.drawio.svg)

///caption
**Figure 5.** Overview of the use cases for preparing the extract from the datasets.
///

The use cases from the diagram are briefly described in the following sections.

## 2.3.2. Make data available for secondary use

The starting point is that the data holder has described all datasets for the health data catalogue. Making data available takes place on the basis of these described datasets.

When a data user (for example a researcher) applies for a permit, they select both the required datasets and a specific cohort — a group of people with a common characteristic — for which the research is to be conducted. On the basis of these choices, the data holder creates an extract of the dataset and makes it available to the data user.

The request to the HDAB (Health Data Access Body) must clearly specify how the data is to be made available. There are several ways this can be done:

1. Federated analysis: The data remains with the data holder and is made available for a federated analysis.

2. Federated learning: The data remains with the data holder and is made available for carrying out federated learning.

3. Data pooling (combined analysis): The data is made available for an analysis in which data from different data holders must first be combined.

In the case of data pooling, the data must be sent by the different data holders to the HDAB, where the combination of the datasets is made available.

For a data request, no extract is made; instead, the dataset is made available solely for the receipt of the request. A data request means that the data user asks a question, after which the data holder executes it in a secure processing environment. Only the answer to the question is then returned to the data user. The dataset itself is not made available to the data user.
