# 7.4. Relation to data space initiatives

Data stations for secondary use of health data within the European Health Data Space (EHDS) do not emerge in isolation. Various generic data space initiatives, including the [International Data Spaces Association (IDSA)](https://internationaldataspaces.org/), the [Eclipse Dataspace Working Group](https://dataspace.eclipse.org/) and [Gaia-X](https://gaia-x.eu/), also focus on interoperable data exchange. This page explores what data stations/EHDS share with these generic frameworks and where they differ.

At an abstract level, data stations and EHDS share many architectural principles with generic data spaces. Federation, data sovereignty, metadata-driven design and authorisation form the common foundation. Whereas generic initiatives and architectures focus on broad applicability, the EHDS is specifically designed for the requirements of health data.

At a detailed level, however, significant differences exist that mean automatic interoperability does not arise of itself. The most important similarities and differences are discussed below.

## 7.4.1. The authorisation model

A fundamental difference lies in how decisions about data access are made. In the EHDS, the Health Data Access Body (HDAB) plays a central role: each EU member state designates an HDAB that issues, refuses and monitors data permits. This centralisation is deliberate. It ensures uniform assessment of data requests against sector-specific criteria and the public interest, and provides enforcement powers via digital health authorities.

Generic data spaces follow a different pattern: peer-to-peer negotiation. Autonomous participants negotiate directly with one another about data use. Trust frameworks handle identification and the possibility of building trust, but they do not perform authorisation. Data holders determine their own policy based on available information as to whether to honour a data request.

This difference is not trivial. The EHDS model provides stronger protection against misuse of sensitive health data and ensures that public interests are not irresponsibly sacrificed to market mechanisms. The generic model offers more flexibility and scales more easily across sectors.

In the implementation of generic data spaces, one can choose to place more responsibility with a central party, but this is a design choice that must be made explicitly. It is not automatically part of the generic frameworks.

## 7.4.2. Domain specificity vs. generic approach

EHDS and data stations are designed for electronic health data, with all that entails. They define priority data categories (patient records, electronic prescriptions, medical images) with phased implementation. They impose specific requirements on SPEs, more than generic data spaces do. They use HealthDCAT-AP, a sector-specific extension of DCAT.

Generic initiatives are sector-agnostic and designed for reuse. This makes them flexible but less targeted. In specific data spaces, domain-specific modifications can be made, but this will come at the cost of interoperability with other sectors. Requirements such as those imposed by the EHDS on SPEs will be more a matter of rules agreed between data holders and users than of the underlying architecture.

## 7.4.3. Legal and governance framework

EHDS is EU legislation, directly binding in all member states. This creates obligations for data holders and enforcement powers for authorities. This guarantees a level playing field and creates a very tight governance structure with little room for deviations.

Generic initiatives are often structured as associations and foundations that parties can join. But specific implementations of data spaces are also often based on voluntary cooperation and contracts between parties. This means that legal enforceability and governance structures can vary between different data spaces.

## 7.4.4. Interoperability

At the level of interoperability there are both similarities and differences. Both approaches use metadata standards such as DCAT to describe datasets. Within the EHDS there are extensions such as HealthDCAT-AP to support health-specific metadata. This can also be applied in generic data spaces and requires minimal effort to ensure compatibility.

In the area of authorisation, as mentioned earlier, greater differences exist. EHDS uses a centrally issued data permit model, while generic data spaces use peer-to-peer contract negotiation. Translating an EHDS data permit into an ODRL policy (used in generic data spaces) is possible, but requires explicit mapping and understanding of the underlying semantics. The translation of ODRL policies into EHDS data permits is more complex, given the more generic nature of ODRL. Systems developed for EHDS and generic data spaces will also have different interfaces and workflows for requesting, issuing and enforcing access.

For actual data exchange — whether exchanging source data or executing calculations in an SPE — there are also differences that are not easily bridged. Given the dependency on authorisation models, the protocols and orchestration of data exchange will differ.

## 7.4.5. Co-existence

Fully mutually compatible systems are unlikely. Convergence at certain layers is possible, however, so that as many of the same concepts as possible are used. In this way, the underlying organisation can be set up comparably, with different implementations attached for different purposes.

This convergence can be sought in the following areas:

1. Use of common metadata standards (DCAT, HealthDCAT-AP) to describe datasets. This allows different systems to interpret each other's metadata and determine whether exchange is possible.
2. Use of common identification and authentication mechanisms (e.g. via eIDAS, EU Digital Identity Wallets and EU Business Wallets) to identify entities in both systems.
3. Prevent lock-in by keeping the interfaces between source systems and data stations/data spaces as generic as possible. This allows source systems to be used with multiple architectures.
