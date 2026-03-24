# 2.4. Analysing data (_use of data_)

The process starts when a data user wants to perform an analysis on data that has been made available by data holders. To carry out the analysis, the data user makes use of a processing hub, or of a secure processing environment (SPE) of the HDAB or of a trusted data holder (Article 72 of the EHDS). Where this text refers to the SPE of the HDAB, the SPE of a trusted data holder is also implied.

The HDAB's SPE is used only when the analysis cannot be carried out in a federated manner. Recital 80 of the EHDS emphasises the principle: "_bring the questions to the data instead of moving the data_". For this reason, a federated analysis is preferred.

An analysis can be carried out in three ways:

1. Federated analysis: the data remains with the data holder and is made available for a federated analysis.
2. Federated learning: the data remains with the data holder and is made available for carrying out federated learning.
3. Data pooling (combined analysis): the data is made available for an analysis in which data from multiple data holders must first be combined.

In addition to performing an analysis, a data request can also be made within this process. The starting point is that such a data request can be carried out multiple times during the validity period of the approval. Unlike an analysis, with a data request the data user does not gain access to the underlying data on which the answers are based.

Before these activities can take place, the HDAB must first grant a permit or approval.

## 2.4.1. Overview of use cases

The Processing Hub is a portal of the HDAB and, depending on the policy of the Member State, of one or more trusted data holders. Together, these portals form a decentralised network of Processing Hubs. Via this portal, data users can launch algorithms to perform analyses or train models. After execution, they receive the results, which they can consult and download within the hub.

In addition to performing analyses, the Processing Hub offers the ability to send data requests to the connected data stations of data holders. In this way, the hub acts as an intermediary between data users and data holders within the network.

For analyses requiring data pooling, the HDAB provides a Secure Processing Environment (SPE). In this situation, data from different sources must be physically brought together to perform the analysis. The SPE is integrated into the Processing Hub, so that this hub serves both as a portal for decentralised analyses — where the data remains with the holder — and for centralised analyses in a secure environment where pooled data is processed. The way in which users gain access to the Processing Hub is determined and managed by the HDAB.

![](uc-analyseren.drawio.en.svg)

///caption
**Figure 6.** Overview of the use cases for analysing or learning from data.
///

The use cases from the diagram are briefly described in the following sections.

## 2.4.2. Register algorithm

An analysis or learning process is carried out by an algorithm, for example a script written in Python or another programming language. The algorithm is packaged in a container so that it can be executed in isolation. Isolated means that the code only has an effect within the container itself and has no effect on the environment outside it. In this way, a secure processing environment is created on the data station in which multiple algorithms, each in their own container, can be executed. Working with containers is a worldwide standard that ensures consistency, security and scalability when running algorithms, with the [Cloud Native Computing Foundation](https://www.cncf.io/) overseeing the further development and management of the [Open Container Initiative](https://opencontainers.org/) as a standard.

The data user develops the algorithm, tests it and then registers it in an algorithm registry. The conditions for registration still need to be elaborated. A possible condition for registration is, for example, conducting a code review.

## 2.4.3. Execute an algorithm in a federated manner

In a federated analysis or federated learning, the data remains securely at the locations where it is stored. Instead of moving the data, the algorithm is distributed to the data stations where the data is available. Each data station executes the algorithm and then sends the results back to the central processing hub. During the validity period of the permit, the data user can run these analyses repeatedly, for example to perform multiple test runs. A test run is a trial execution in which the goal is not the final result but to check whether the analysis works correctly both technically and substantively.

To gain access to the processing hub, a data user must log in at a high assurance level. This means that the identity of the user is carefully verified and must be linked to a valid permit for access to health data. The processing hub forms part of a secure processing environment, as described in the EHDS, and ensures that both the identity of the user and the associated permit are securely transmitted with a request to perform a federated analysis or learning process.

The other component of this secure environment is the execution of the algorithm on the data station. When a data station receives a request, it first checks the identity of the user and the permit. The algorithm is then retrieved from the algorithm registry and is given access to the data specified in the permit. Execution takes place in an isolated environment, with all activities closely monitored and logged to ensure security and compliance. After the algorithm has been executed, the results are securely sent back to the processing hub.

In the processing hub, the data user can then download and use the results for further analysis. A release process has been set up for this purpose, in which the results are first checked for sensitive information, such as privacy-sensitive data or trade secrets. This satisfies the requirements of Article 73(2) of the EHDS and ensures the privacy and security of the data.

## 2.4.3. Execute a data request

A data request begins with assessment and approval by the HDAB. After approval, the HDAB converts the request into a technical query in a standardised language, which may differ by information domain. For example, different standards may apply to questions about business operations or care quality than for medical data. Answers to data requests are always provided in an anonymised statistical format, as prescribed in Article 69(1).

Once the request has been approved and translated, it can actually be executed. The data user initiates the request, which is then sent to the data stations of the selected data holders. There, the technical query is executed and answered on the relevant data. The results are sent back to the processing hub, where the data user can download them for further analysis or use. The processing hub must have functionality available that aggregates the individual results from each data station into a whole and checks them for traceability. This aggregation function would, for example, apply k-anonymity techniques before the answer is released to the applicant.

Access to the processing hub is only possible for data users who have a valid approval for a data request. To gain this access, the data user must be authenticated at a high assurance level. This means that the identity of the user is carefully verified and is always linked to a valid approval of the relevant data request, so that only authorised persons have access to the data.

## 2.4.5. Make data available in a central secure processing environment

The HDAB has sent a request to data holders to make data available for the central execution of an algorithm in a Secure Processing Environment (SPE). This request is received by the data station of the data holder and then forwarded to the Processing Hub.

## 2.4.6. Execute an algorithm in a centralised manner

The algorithms for a centralised analysis or federated learning are executed within the secure processing environment (SPE) of the HDAB. Within this environment, the HDAB makes available the data for which a permit has been obtained, so that the data user can use it. Access to the SPE requires the data user to log in at a high assurance level and their identity must be linked to a valid permit. This ensures that only authorised users have access to the data and can carry out analyses within the secure environment.

After the analysis has been carried out, the data user can download the results. As with a federated analysis, a release process is required for this, in which the results are first checked.

## 2.4.7. Release results

Before a data user can download the results, these must be released by an assessor from the HDAB (or from a trusted data holder).
