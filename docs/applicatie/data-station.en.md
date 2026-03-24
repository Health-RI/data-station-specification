# 4.1. Data station

## 4.1.1. The data station at the heart of the hourglass

The third layer of the hourglass model consists of a network of nodes each with a data station. A data station is an abstract concept for the system that ensures that data can be made available for secondary use. The term data station is used in both primary and secondary use, but the function and requirements differ.

!!! info "Difference between data stations for primary and secondary use"

    In primary use, the function of the data station is not to make data available, but to make a patient record accessible to the data recipient, who then makes this data available to the end user: the care provider. To make this distinction clear, we speak of making data accessible in the context of primary use. The data station manages access to the patient record on the basis of agreed and statutory access rules.

    In secondary use, datasets — in which multiple patient records are included — are made available to data users. In this case, the data station not only makes data accessible on the basis of access rules, but also makes it available to the data user's algorithm. This takes place in accordance with the requirements for making data available for secondary use, including pseudonymisation. In other words, the data user's application, the algorithm, is executed on the data station. In primary use, this is never the case. The data recipient in this scenario plays the role of recipient of the algorithm's results, with which the data user can deliver the final results.

    In addition to executing algorithms, the data station can provide for the transport of data, for example in situations of data pooling, where data is brought together in a secure processing environment of the HDAB or of a trusted data holder. In this scenario, the HDAB and the trusted data holder are the data recipients. Because secondary use involves working with large datasets, different standards are required for transport than in primary use.

    In the text above, patient records are used as an example. Secondary use, however, is broader and encompasses more than just patient records. This also constitutes a difference from the primary use of data.

### 4.1.1.1. One data station per data holder

An important principle is that the data in a data station falls under the processing responsibility of a data holder. This data holder is a data owner who is obliged under the EHDS to make data available and is not exempted under Article 50. Therefore, each data holder in principle has its own data station.

The starting point is that data holders go through a process to become a participant in the data space and sign a participation agreement in which they commit to the agreements of the data space for secondary use. The HDAB is responsible for both making and enforcing these agreements.

!!! info "Agreement frameworks and data spaces"

    In the text, both the term agreement framework and data space are used. We define a data space as an agreement framework for data availability; it enables reliable data transactions between participants. A broad definition of data transaction is used: a transaction can be data exchange (data from participant A to participant B) or more complex scenarios such as _algorithm-to-the-data_, the basis of federated analysis. In other words, agreement frameworks can cover many topics; data spaces limit the topic to data transactions and data availability.

### 4.1.1.2. Model with service providers

In practice, data holders are not always able to implement a data station independently. They often do not have the necessary people, processes and technical capabilities to do so. This also regularly applies to data users.

To address this, the architecture is based on a so-called four-corner model. In this model, service providers act on behalf of data holders and data users and connect these parties to the data space for secondary use. Through this connection, data holders and data users are included in the network of participants via a node. In the primary use of data, organisations often fulfil both roles: data holder and data user. In secondary use, these roles are more often separated, because researchers and government bodies, for example, act exclusively as data users and are not data holders.

The four-corner model is applied in virtually all modern agreement frameworks. Agreements are made with all participants about their role, tasks and responsibilities within the framework.

![](datastation-4corner.drawio.en.svg)

///caption
**Figure 1.** Four-corner model, with service providers for data holders and users.
///

Not every healthcare provider needs to contract a service provider themselves. In the current landscape, we see that many healthcare providers collaborate within regional cooperative organisations to jointly contract a service provider for connection to a data space. Within this construction too, the principle remains that every data holder has its own data station. The service provider hosts this on behalf of the data holder.

In the four-corner model, a service provider can host nodes for both data holders and data users. For data holders, the service provider sets up a data station; for data users, a processing hub.

![](datastation-netwerk.drawio.en.svg)

///caption
**Figure 2.** Network of data stations and processing hub.
///

Within secondary use, the setup of a processing hub is reserved for the HDAB and trusted data holders. From each processing hub, both an approved data request and a (federated) algorithm can be executed on the basis of a data permit. In the figure above, only the processing hub of the HDAB is shown. In reality, multiple processing hubs may exist — one hub per trusted data holder.

## 4.1.2. Data station for secondary use

In a data space for secondary use, the data station is the counterpart of the processing hub. Where the processing hub is the component for the data recipient, the data station is that for the data holder. These components form a two-unit within the data space architecture: one core component is defined for each role.

The data station is a technical component included in a node of the data space. From the data station, the data holder makes data available for secondary use, under pre-established conditions. The data station supports functions such as exposing datasets, applying access and usage conditions, ensuring security and privacy, and facilitating interoperability with other nodes within the data space.

This division of roles creates a clear separation of responsibilities: the data holder retains control over the availability and use of data via the data station, while the data recipient can process and analyse the data via the processing hub within the agreed frameworks. Together, the data station and the processing hub form the foundations for a reliable, scalable and interoperable data space for secondary use.

!!! info "Definition of a data station"

    A data station is an environment managed by a service provider in which datasets and data services of a data holder are made accessible according to agreed standards, with explicit rules for access, authorisation, logging and use, so that data can be reliably and interoperably used and exchanged within a data space.

The data station as a system is involved in the processes for [preparing](../proces/klaarzetten.md) data and [analysing](../proces/analyseren.md) data. It supports these processes with the use cases shown in the diagram below.

The colour difference between the actors and the data station makes it clear that the data station interacts with the HDAB and with trusted data holders. The configuration, management and maintenance of the data station itself are not included in the use cases. The use case diagram is intended to make clear what value the data station has for realising the data space. Configuration, management and maintenance is valuable, but is not the reason why the data space needs a data station.


![](uc-datastation.drawio.en.svg)

///caption
**Figure 3.** Use case diagram of the data station for secondary use.
///

The following sections describe the requirements for a data station.

!!! info "A data space does not prescribe the architecture of a data station"

    The architecture of a data station is the responsibility of the service provider that offers the data station. A service provider must be able to realise and implement a data station autonomously; after all, each participant in the data space operates independently.

    For this reason, no detailed architecture is elaborated in this chapter. From the data space perspective, what matters most is that interoperability with the data station is ensured and that the trust and integrity of the data space as a whole are guaranteed across all autonomous components. The requirements for a data station therefore focus solely on interoperability and trust.


## 4.1.3. Manage dataset catalogue

Each data holder is itself responsible for cataloguing and publishing its datasets. This means that the data holder compiles and manages its own dataset catalogue. In this document we do not specify which datasets must be included in the catalogue, only which format is used. The catalogue must be drawn up in [HealthDCAT-AP](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/).

The catalogue must be accessible via the data station. The EHDS stipulates (Article 77) that the catalogue published by the Health Data Access Body (HDAB) is publicly accessible. In line with this, the catalogue on the data station may also be publicly accessible.

![](datastation-beheren.drawio.en.svg)

///caption
**Figure 4.** Components for managing the dataset catalogue.
///

For managing the catalogue, the assumption is that a service employee uploads the catalogue to the data station. This is, however, only an example: the data holder determines how this process is organised, manually or automated.

By releasing we mean that the data holder publishes a version of the data catalogue and thereby makes a new version available. This release can take place periodically, for example several times a year. Registering the catalogue, on the other hand, only needs to happen once.
After registration, the data holder's catalogue is registered in the HDAB's register for the National catalogue of datasets.

## 4.1.4. Periodically retrieve dataset catalogue

The Health Data Access Body (HDAB), with the National Catalogue component, is completely autonomous in determining the frequency with which the National Catalogue is updated. This means that the HDAB can plan when a data holder's catalogue is retrieved, rather than this happening ad hoc by all holders simultaneously.

![](datastation-ophalen.drawio.en.svg)

///caption
**Figure 5.** Components for retrieving the dataset catalogue.
///

This autonomy creates an efficient and controlled update procedure, preventing peak loads or "queuing" when multiple data holders want to update their catalogue simultaneously. Moreover, this arrangement contributes to the reliability and stability of the National Catalogue, because updates take place in a spread and predictable manner. This gives both the HDAB and the data holders more control over the process and helps to ensure consistent and up-to-date information in the data space.

## 4.1.5. Make data available for secondary use

The HDAB sends a request to make a dataset available for secondary use. This request may be based on a data permit issued by the HDAB or on an approved data request.

The starting point is that a data holder has obtained or collected data and has organised it into a number of datasets in order to publish these via a catalogue. In the figure below, these prerequisite steps are shown. In the datasets that are compiled/prepared on the basis of a permit, those persons for whom an opt-out has been registered at that time must be removed, indicating they do not wish to be part of secondary use under the EHDS (Article 71 EHDS). The principle of data minimisation must also be applied, meaning only a subset of the data that is relevant to the permit is made available to the data user.

![](datastation-organiseren.drawio.en.svg)

///caption
**Figure 6.** Overview of organising and preparing the data for federated analysis.
///

Making data available may entail:

1. Access to a dataset from the catalogue being granted.
2. Data needing to be prepared and then made available in the data station (federated).
3. Data needing to be prepared and then made available centrally (data pooling).

Re 1: Secondary use is often about conducting research on the basis of health data of individuals. But not always. It is therefore possible that making data available means that access can be granted to a dataset, for example for making data available for a data request. Granting access means that access rules are established for the algorithm or request of the data user. Only when these access rules are met does the algorithm gain access to the dataset. Examples of access rules include that the algorithm must be able to authenticate itself and must be able to demonstrate that it has a valid permit or approval for the data request.

Re 2: To comply with a permit or a data request, it may be necessary to prepare the data. By preparation we mean that an extract of a dataset is made, for example to include only a specific cohort, or that data is pseudonymised according to an algorithm established by the data user and approved by the HDAB.

In a federated setup, the prepared data is made available in the local data station, so that algorithms have access to the datasets without the data being brought together centrally.

Re 3: When datasets are made available centrally, the prepared datasets are securely transported to a central processing hub. In this hub, datasets can be brought together, integrated and analysed, so that researchers and algorithms have access to the combined datasets within the applicable conditions of the permit. Transport to the central hub takes place via secure connections, with the integrity and confidentiality of the data guaranteed at all times.

!!! info "Horizontally versus vertically partitioned data"

    The process of making data available depends on how the data is partitioned. Making horizontally partitioned data available is relatively straightforward: each data holder has a complete row (record) for a data subject and prepares this in the data station.
    
    For vertically partitioned data, the process is more complex. At the time of drawing up this specification, federated analysis techniques are not sufficiently mature for large-scale use with vertically partitioned data. To combine different data points (columns) for one data subject across different data holders, for example, each data holder would need to provide the data with a uniform pseudonym, enabling the data to be linked across the data stations. The data would then need to be (temporarily) forwarded to a central SPE, where it must be linked before it is actually available to the data user.

In the figure below, scenarios 2 and 3 are shown.

![](datastation-klaarzetten.drawio.en.svg)

///caption
**Figure 7.** Process for making data available for secondary use, with alternative scenarios for executing data pooling (central) and federation.
///

With the data made available, the data station is ready to receive an algorithm or a data request.

## 4.1.6. Process algorithm and return result

A data station can be used, among other things, to execute a federated analysis or for federated learning, or in short for executing an algorithm. The data user, via the processing hub, issues an instruction to execute an algorithm on a number of data stations. The diagram below shows the steps that are executed on the data station after the instruction has been received.

!!! info "Definition of an algorithm"

    An algorithm is a set of rules and instructions that a computer executes. Algorithms help, for example, to analyse problems but also to make decisions. (source: [Digitale Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/algoritmes/))

![](datastation-analyseren.drawio.en.svg)

///caption
**Figure 8.** Process for executing an algorithm in a federated manner.
///

**Receiving and executing an algorithm on the data station**

After receiving an instruction via the processing hub, the data station starts the process of executing an algorithm. As a first step, the authenticity and validity of the identity of the data recipient, the identity of the data user and the permit are verified on the basis of submitted credentials at a high assurance level, in conformity with the eIDAS Regulation. Only when this verification has been successfully completed is the instruction processed further.

The data station then retrieves the algorithm, which forms part of the permit, from the algorithm registry. In the current implementation, algorithms are available in the form of Docker images. After retrieval, the integrity of the algorithm is checked, for example by means of checksums or digital signatures, to establish that the algorithm has not been modified and originates from a trusted source.

After a successful integrity check, the algorithm is incorporated into the container management environment of the data station. In doing so, the algorithm is configured according to the instruction, including setting the necessary parameters, access rights to data and any runtime restrictions. The algorithm is then started and executed within an isolated container environment, so that execution takes place safely and in a controlled manner.

**Communicating the results**

Once the algorithm has finished executing, the data station notifies the processing hub. From that moment, the algorithm can communicate the results to the processing hub, in accordance with the agreed interfaces and protocols.

It is possible that the algorithm remains active within the data station for an agreed period after the initial execution. During this period, the algorithm can be restarted periodically to perform repeated analyses or to perform federated learning based on newly available data. After this period, the algorithm is terminated and removed from the container management environment, unless otherwise agreed.

![](datastation-leveren.drawio.en.svg)

///caption
**Figure 9.** Overview of executing a federated analysis and delivering the results.
///

The overview above shows how results are delivered on the basis of a federated analysis or federated learning. The combination of processing hub and data station functions as a whole as a secure processing environment, compliant with the requirements of the EHDS and TEHDAS2. The responsible parties must guarantee that all data processing takes place securely, in a controlled manner and in compliance with regulations.

Among other things, the following aspects must be ensured:

- **Governance**: clear responsibilities and agreements between the processing hub and the data station, including procedures for the approval of algorithms and data requests.
- **Access control**: strict control over who has access to datasets, including authentication at a high assurance level and verification of valid permits. Only authorised and validated queries and algorithms may access the datasets.
- **Monitoring and logging**: all access to datasets and all activities carried out within the processing environment are logged and monitored, so that every action is traceable and deviations can be detected.
- **Data isolation and results management**: processing takes place in isolated container environments, so that datasets and algorithms remain separated from other processes.
- **Integrity and security of algorithms**: all algorithms that are executed have been checked for integrity and authenticity, for example by means of digital signatures or checksums.

With regard to the results, a decision must be made as to whether they may leave the secure environment of the processing hub. A release process must be defined for this purpose in which strict rules for export and transfer apply.

## 4.1.7. Answer data request

The above section describes one way of fulfilling a data permit in the sense of the EHDS. A data station can also, as an application, support a data request. The way in which this is executed is very similar to the process described above, albeit simpler. When a data request is received via the processing hub, the data station starts the processing procedure. As a first step, the authenticity and validity of the identity of the data recipient, the identity of the data user and the agreement to the data request are verified on the basis of submitted credentials at a high assurance level, in conformity with the eIDAS Regulation. Only after a successful verification is the data request processed further.

The data station then retrieves the associated algorithm from the algorithm registry. In this context, the registry contains a collection of reusable queries that have been approved for use within the data space. After retrieval, the integrity of the algorithm is checked, for example by means of digital signatures or checksums, to ensure that the algorithm is authentic and unmodified.

The algorithm is then started and executed on the data station. During execution, the algorithm is processed in isolation, so that data security and privacy are maintained. After execution is complete, the results are reported back to the processing hub, in accordance with the agreed protocols and interfaces.

![](datastation-dataverzoek.drawio.en.svg)

///caption
**Figure 10.** Process for executing a data request in a federated manner.
///

The algorithm can be invoked again during the duration and validity period of the data request. This makes it possible to perform analyses periodically or generate repeated results without a new data request being necessary. Once the validity period of the data request has expired, further execution of the algorithm is stopped, unless explicitly extended.
