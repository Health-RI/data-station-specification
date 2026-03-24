# 6.1.1. KIK-V implementation: process

## 6.1.1.1. Functional description of the question-and-answer process

![](https://kik-v-publicatieplatform.nl/api/gitblob?repositoryUrl=https%3A%2F%2Fgitlab.com%2Fkik-v%2Fafsprakenset&branchOrTag=3.0.0&path=Documentatie%2Fafspraken_gegevensuitwisseling_datastations%2Ffunctionele_beschrijving_vraag_en_antwoordspel.png)

The way in which data users (consumers) and data providers (data holders) shape the KIK-V question-and-answer process depends in part on the degree of digitalisation of the parties involved. The agreements and specifications within KIK-V describe the question-and-answer process using data stations by care providers and the KIK-Starter by consumers. Based on these agreements and specifications, providers can implement a data station for KIK-V use and for exchange with the KIK-Starter for consumers. Consumers can reference the agreements and specifications in their exchange profiles.

In practice, KIK-V supports what in the EHDS are called data requests, using federated analytics in a decentralised network of data stations.

## 6.1.1.2. Principles

The general principles of the KIK-V Agreement Set apply to data exchange between the KIK-Starter and data stations. These include the application of the Principles for the Healthcare Information System (P12) and the FAIR data principles (P10).

In addition, the agreements are built on the following three principles:

1. Scalable decentralised model;
2. Healthcare infrastructure-independent;
3. Correct implementation is the own responsibility of the consumer/provider.

These principles are elaborated below.

### Principle 1. Scalable decentralised model
The potential of the KIK-V approach for the multiple use of data is substantial. Because data — including the interrelationships and meaning of that data — is standardised and stored in providers' data stations, it is possible to answer a wide range of questions using the same data. The technical exchange with data stations must offer the same potential for scalability. For this reason, the question-and-answer process has been designed so that both consumers and care providers can participate in this exchange easily, regardless of type or number.

For generating verifiable cryptographic proofs, the W3C standard Verifiable Credentials is applied. This standard defines three roles: issuer, holder and verifier. The issuer is a third party that holds authority over certain information and issues a declaration in the form of a verifiable cryptographic proof. The holder receives this verifiable proof and is the party about whom the declaration pertains. The holder applies the technical proof in the direct, decentralised process with the verifier. To be able to trust the information in the proof, the verifier checks the authenticity of the issuer's declaration against an underlying shared trust registry (verifiable data registry). Issuer, holder and verifier are all technically connected to this verifiable data registry.

See also the figure below for the relationships between the roles.

![](https://kik-v-publicatieplatform.nl/api/gitblob?repositoryUrl=https%3A%2F%2Fgitlab.com%2Fkik-v%2Fafsprakenset&branchOrTag=3.0.0&path=Documentatie%2Fafspraken_gegevensuitwisseling_datastations%2Fprincipe_1.png)

### Principle 2. Healthcare infrastructure-independent
KIK-V does not create or manage healthcare infrastructure and reuses existing field agreements on this matter. The KIK-V question-and-answer process via data stations with the KIK-Starter, using the Verifiable Credentials standard, should in principle be applicable via any underlying healthcare infrastructure.

#### Provisional delineation of healthcare infrastructures

The aim of working infrastructure-independently creates several practical issues in the short term. If individual consumers and providers make different choices for the infrastructure on which they base their interfaces, this results in an interoperability issue within KIK-V. Interfaces from different infrastructures do not automatically understand one another. Although KIK-V works infrastructure-independently, a short-term delineation of the application of healthcare infrastructures is necessary. This is to prevent interoperability issues from converging within KIK-V. The KIK-V chain partners asked the programme to shape this delineation as follows:

1. By elaborating the implementation of the KIK-V question-and-answer process using the KIK-Starter via Nuts in specifications;
2. By working towards interoperability agreements between Nuts and nID to arrive at the most cost-efficient solution for all parties (nID is used within iWLZ by care offices as healthcare infrastructure).

In 2023, the intention was to test both types of agreements in the data station exchange pilot from this delineation. However, the pilot ultimately did not lead to the implementation of interoperability agreements between Nuts and nID. In early 2023, the Nuts-nID Interoperability Working Group advised against working towards interoperability between Nuts and nID in the short term. Instead, it was advised that Nuts and nID should continue in parallel towards a shared future vision based on similar standards (including Verifiable Credentials, DIDs) and principles (including DIZRA). At the end of 2023, the working group appeared to be resuming informally, with work continuing between Nuts and nID/iWLZ on an interoperability solution. This solution is based on a limited number of standards and does not yet cover all aspects required for the KIK-V question-and-answer process. For example, working with verifiable credentials is not yet in scope. KIK-V has therefore agreed with iWLZ to remain involved from the sidelines in these developments and, once solutions become available via Nuts, to investigate the impact on the current Nuts specifications. In the meantime, the programme applies the Nuts specifications successfully tested in the pilot for data exchange between the KIK-Starter for consumers and the data stations for providers.

### Principle 3. Correct implementation is the own responsibility of the consumer/provider
KIK-V, like other use cases for data exchange in healthcare, builds as much as possible on (national) agreements in the area of healthcare infrastructure and information security. KIK-V's conviction is that repeatedly shaping verification of these agreements within different initiatives is not the most scalable solution in the Netherlands. KIK-V therefore does not provide for separate verification of the correct implementation of agreements that transcend KIK-V (NEN7510/7512/7513, interfaces of healthcare infrastructures, etc.). Where there is a broader need for this, verification of a correct implementation of these broader agreements could be shaped beyond KIK-V. As far as KIK-V implementation is concerned, the correct implementation of these agreements is regarded as the own responsibility of consumers and providers. The KIK-V Management Organisation bears that responsibility for the KIK-V KIK-Starter and the credentials platform.

The KIK-V management organisation does, however, provide a reporting point for problems in data exchange. This reporting point primarily serves to identify patterns in reports and to refer these to the relevant problem owner.
