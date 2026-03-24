# 2.2. Requesting data (_data access_)

The application process starts when the required health data has been found in the European or national health data catalogue, or when the data user suspects that data holder(s) hold data that is relevant even though it has not yet been published in a catalogue.

An application can then be submitted via two channels: via the central platform of HealthData@EU or via the system of the national body responsible for health data access (HDAB). All applications submitted via the central platform always arrive first at the National Contact Point for secondary use (NCP-SU). The NCP-SU acts as a connection point in the infrastructure, specifically designed to enable the secure exchange of health data between the different Member States of the European Union.[^1] It makes no difference to the applicant whether the application is submitted centrally or via the national body. It is worth noting that there is no direct communication between the HDAB and the central platform; everything goes through this NCP-SU.

The EHDS[^2] distinguishes between two types of applications:

- Applications for access to health data [Article 68](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_68), and
- Requests for health data [Article 69](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_69).

When an application is assessed positively, this leads to the issuance of a data permit for access to the data or an approval of the request. In the diagram, these steps are represented as "Issue data permit or approval to request" and "Apply for access to health data."

On the basis of an application, an HDAB can issue a data permit, and on the basis of a request, an approval can be granted. Both the data permit and the approval are electronic attestations of attributes (our assumption and requirement for a federated operation of the system, but not guaranteed in THEDAS2), in line with the European framework for digital identity[^3][^4] and the proposals for European business wallets[^5]. This attestation can also be revoked at any time if necessary.

To be transparent (open and clear) about how health data is used, all applications are published immediately upon receipt. This means that an application is made public before it has been checked for completeness.

## 2.2.1. Overview of use cases

The HDAB uses a system for receiving and processing applications. Within the secondary use system, this system is called the Data Access Application Management System (DAAMS). The diagram below shows the main use cases of this system. The name of each use case indicates what a user can do with the system.

In the use case methodology, a use case can be extended with another use case. In the diagram, this is applied to make clear that issuing a data permit or approval precedes applying for access to health data. This means that an applicant can start with the use case for applying for data, and that this automatically includes the steps required for granting the permit or approval.

![](uc-aanvragen.drawio.en.svg)

///caption
**Figure 3.** Overview of the use cases for applying for (access to) health data.
///

The use cases from the diagram are briefly described in the following sections.

## 2.2.2. Apply for (access to) health data

An applicant, such as a researcher or a government organisation, can request access to health data for a specific purpose. To do so, the applicant must first log in with a means of authentication recognised in the Netherlands under the Digital Government Act (Wdo). Examples include DigiD, the European Digital Identity Wallet (from 2027) and eHerkenning for organisations.

After logging in, the applicant can fill in the application, save it at an intermediate stage, and submit it definitively at a later time.

During the completion of the application, the applicant must indicate which datasets are required. This means that the applicant selects which datasets access is being requested for, or — in the case of a data request — from which datasets an answer in anonymised statistical format must be provided. All information about available datasets is in the National catalogue for datasets. This catalogue can be thought of as a card index of all datasets that can be used. Using a kind of shopping cart, the applicant can easily select and add datasets to the application.

## 2.2.3. Issue permit or approval

The HDAB grants a permit or an approval for an application. Which of the two it will be depends on the type of application submitted:

- The HDAB grants a permit if the application concerns access to health data (pursuant to [Article 68](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_68)).
- The HDAB grants an approval if it concerns a request for health data (pursuant to [Article 69](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_69)).

This section (the use case) explains which steps must be followed to reach this permit or approval.

The use case starts when an application is submitted, either via the central platform or via the HDAB's own system. The diagram below illustrates the various statuses that an application goes through from submission to the final decision: approval, rejection or withdrawal by the applicant. Each status represents a completed process step, which is briefly described in this use case.

![](uc-aanvragen-state.drawio.en.svg)


///caption
**Figure 4.** Overview of the status transitions during the handling procedure of the application.
///

### 2.2.3.1. Receipt and intake

Once an application has been received, processing begins. Applications from government bodies are handled more quickly via an expedited process. In addition, all applications are subject to statutory maximum time limits, as laid down in Articles 68 and 69 of the EHDS:

- A permit must be issued within three months, calculated from the moment the application is complete.
- The same three-month period applies to a request for data.

Therefore, processing always begins with a check to ensure the application is complete before the substantive assessment begins.

### 2.2.3.2. Investigation

When an application is taken into processing, it is first checked for completeness. If information is missing, the applicant is given the opportunity to supplement the application. If the applicant does not do so in time, the application may be rejected. Once the application is complete, the substantive assessment can begin.

### 2.2.3.3. Assessment

During the substantive assessment, it is checked whether the application meets the requirements. It is also examined whether the application is technically feasible. To this end, the application is forwarded to the data holders, who assess whether the requested data can be provided. The data holders also prepare a cost estimate for processing and delivery.

If the application is feasible, it proceeds to the next step. Sometimes an application is partially approved or converted into a simpler data request, for example when anonymised statistical data is already sufficient.

### 2.2.3.4. Providing a cost indication

Once it is clear which data can be provided, the fixed and recurring costs are calculated, including the costs of the data holders, any SPE providers and those of the HDAB. The applicant receives an overview of these costs and must indicate whether they agree. If agreed, the application proceeds. If the applicant does not respond or does not accept the costs, the application may be terminated.

### 2.2.3.5. Issuing the attestation (permit or approval)

When an applicant accepts the costs, a permit or approval can be granted. Obtaining this acceptance requires trust, which is guaranteed by the European regulation on digital identity and trust services. This regulation distinguishes three assurance levels[^6]: low, substantial and high.

For special categories of personal data, such as medical records data, a high assurance level is required to guarantee secure availability. Therefore, both the permit and the approval must be granted at a high level and presented in a reliable manner to the parties responsible for secure access to and processing of the data, such as the data holders and the providers of secure processing environments.

When the requirements for issuing a data permit are not met, but the requirements for providing an answer in an anonymised statistical format under Article 69 are met, the HDAB may, following assessment, decide to convert an application for access to health data into a request for health data.

### 2.2.3.6. Sending the request

Once the permit or approval has been granted, a request is sent to the data holders to make the requested data available to the applicant, either within a secure processing environment, or by delivering the data as requested.

## 2.2.4. Revoke attestation

On the basis of [Article 63](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_63) of the EHDS, the HDAB must monitor compliance with the conditions attached to the permit or approval. If this monitoring reveals that an applicant is not complying with these conditions, the HDAB may intervene and revoke the permit or approval. In the future, it will need to be described in more detail how, in addition to revoking the approval or permit, the process of renewing or supplementing the permit will be organised.

## 2.2.5. Consult submitted applications

The EHDS stipulates that the HDAB must make an application public immediately upon receipt ([Article 57](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500327#art_57)), even if it later turns out that the application is incomplete and still needs to be amended. This means that publication takes place before the application is checked for completeness. In addition, Article 57 states that applications must be made available electronically.

[^1]: More about the architecture of HealthData@EU can be found on the [documentation website](https://acceptance.data.health.europa.eu/healthdata-central-platform/documentation?locale=en).

[^2]: European Parliament and Council. (2025). Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2025/327/

[^3]: European Parliament and Council. (2014). Regulation (EU) No 910/2014 of the European Parliament and of the Council of 23 July 2014 on electronic identification and trust services for electronic transactions in the internal market and repealing Directive 1999/93/EC. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2014/910

[^4]: European Parliament and Council. (2024). Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards the establishment of the European framework for digital identity. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2024/1183/

[^5]: European Commission. (2025, November 19). Proposal for a Regulation on the establishment of European Business Wallets. https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets

[^6]: European Commission. (2015, September 8). Commission implementing regulation (EU) 2015/1502 of 8 September 2015 on setting out minimum technical specifications and procedures for assurance levels for electronic identification means pursuant to Article 8(3) of Regulation (EU) No 910/2014 of the European Parliament and of the Council on electronic identification and trust services for electronic transactions in the internal market. https://eur-lex.europa.eu/eli/reg_impl/2015/1502/
