# Vereisten van beveilige verwerkingsomgevingen

Hieronder staan de verschillende vereisten zoals in de TEHDAS2 consultatie _7.4 Draft technical, functional and security specifications of Secure Processing Environments | Appendix B_ zijn geformuleerd. Deze zijn gebruikt als ijkpunt in de verdere specificatie van de componenten. [TO DO: requirements vertalen naar het Nederlands.]

??? abstract "Sensitive data (SD) requirements"
    | ID | Requirements |
    |----|--------------|
    | SDR-1 | Unauthorised users MUST NOT be able to access sensitive data |
    | SDR-2 | Service administrators SHOULD NOT have access to sensitive data |
    | SDR-3 | Sensitive data MUST be in a protected format at rest and in transit |
    | SDR-4 | Sensitive data protection MUST be done with widely accepted, secure algorithms combined with effective isolation measures |

??? abstract "Secure Processing Environment (SPE) requirements"
    | ID | Requirements |
    |----|--------------|
    |SPER-1 | SPE MUST enable scientific research on sensitive data |
    |SPER-2 | There SHOULD be a diverse selection of SPEs for the varied needs of sensitive data research |
    |SPER-3 | It MUST be possible to transfer sensitive data between, in and out of SPEs |
    |SPER-4 | SPE MUST provide adequate protection against exposing sensitive data to unauthorised users |
    |SPER-5 | SPE design SHOULD promote collaboration among authorised users |
    |SPER-6 | Project-based user environments of SPE MUST be isolated from each other and open Internet |
    |SPER-7 | Authorised users MUST protect sensitive data they display |
    |SPER-8 | Authorised users MUST interact with their SPE project space only through secure protocols |
    |SPER-9 | All APIs connecting SPE components MUST be logged and monitored |


??? abstract "European Health Data Space (EHDS) SPE requirements"
    | ID | Requirements |
    |----|--------------|
    |EHDSR-1 | HDAB MUST grant access to EHD using a data permit |
    |EHDSR-2 | EHD MUST be accessed using an SPE |
    |EHDSR-3 | Natural persons listed in the data permit MAY access the identified EHD in SPE |
    |EHDSR-4 | TOMs MUST minimise the risk of unauthorised EHD access in SPEs |
    |EHDSR-5 | Authorised health data users MUST be strongly identified
    |EHDSR-6 | All access and operation logs of SPE MUST be available for verification and auditing |
    |EHDSR-7 | All SPE logs MUST identify the actor |
    |EHDSR-8 | All SPE logs MUST be kept at least for one year |
    |EHDSR-9 | TOMs of SPEs MUST be monitored for security |
    |EHDSR-10 | EHD MUST be identified in the data permit |
    |EHDSR-11 | Health data holder MUST upload the permitted EHD to be available in an SPE for the health data user |
    |EHDSR-12 | Health data user MAY download only non-personal EHD from SPE. Anonymised personal data is non-personal |
    |EHDSR-13 | HDAB MUST ensure by reviewing that no personal data is taken out of the SPE by the health data user |
    |EHDSR-14 | Regular internal and external security audits MUST be done on SPE TOMs |
    |EHDSR-15 | SPE TOMs MUST undergo risk assessments |
    |EHDSR-16 | HDABs MUST ensure that SPE TOMs audits are carried out and that risk assessments lead to risk mitigations |
    |EHDSR-17 | When SPEs mentioned in the EU Data Act are used for EHD, EHDS rules and requirements MUST be followed |
    |EHDSR-18 | SPEs MUST adapt to TOMs that the Commission will write into EHDS implementing acts |

??? abstract "Operational (OP) EHDS SPE requirements"
    | ID | Requirements |
    |----|--------------|
    |OPR-1 | The SPE operator MUST have procedures in place to enforce user authentication and access restrictions based on the data permit associated with the processing of health data |
    |OPR-2 | SPE Operator MUST limit the number of authorised staff and any subcontractors who have high-privileged access enabling them to access or process health data and MUST implement effective procedures for managing and monitoring such access within the SPE infrastructure |
    |OPR-3 | SPE Operator SHOULD maintain a Service Portfolio including all services |
    |OPR-4 | SPE Operator SHOULD maintain a configuration management database (CMDB) |
    |OPR-5 | SPE Operator MUST implement mechanisms to terminate the secure processing environment upon expiration of the data permit | All electronic health data within the environment MUST be deleted or rendered unrecoverable within six months of permit expiry, including any backups or redundant copies | Procedures MUST be formally documented, monitored, and aligned with risk assessments and confidentiality requirements | |
    |OPR-6 | SPE Operator MUST undergo regular internal and external security audits to assess compliance with security, data protection, and operational requirements |
    |OPR-7 | SPE Operator MUST retain logs and access records to ensure traceability of all operations and enable audits or investigations when needed |
    |OPR-8 | The SPE operator MUST maintain up-to-date documentation of all relevant technical, organisational, and security processes |
    |OPR-9 | The SPE operator SHOULD assign a Compliance Officer or designate responsibilities to ensure adherence to legal, ethical, and technical obligations |
    |OPR-10 | SPE Operator MUST have an operating information security management system (ISMS) |
    |OPR-11 | SPE Operator SHOULD establish a Service Management System |
    |OPR-12 | SPE operators MUST conduct regular Data Protection Impact Assessments (DPIAs) |
    |OPR-13 | SPE Operator MUST maintain policies to ensure security around procurement systems and development and operation of systems | |
    |OPR-14 | SPEs SHOULD adopt change management process with impact and risk assessment |
    |OPR-15 | SPE Operator SHOULD adopt a release and deployment management process |
    |OPR-16 | SPE Operator MUST track and log actions of each authorised project member, including instances of data access, processing, viewing and output |
    |OPR-17 | SPE Operator MUST implement a secure storage process to retain logs of user access to the SPE for a minimum period of one year |
    |OPR-18 | A reporting process MUST be in place to notify HDABs and relevant authorities of security incidents or non-compliance findings including data breaches or misuse |
    |OPR-19 | SPE Operator SHOULD adopt and enforce defined timelines for communicating and reporting incidents to the HDAB: Early warning notification: within 24 hours of incident detection. Detailed incident notification: within 72 hours of incident detection. Final incident report: no later than one month after the incident |
    |OPR-20 | SPE Operator MUST be able to promptly halt access and processing activities within the SPE when misuse or data breaches are identified |
    |OPR-21 | SPE Operator MUST have disaster recovery procedures in place to restore the availability and integrity of the SPE services, including critical system components, configurations, and platform-level functionality, from clean backups, and to resume normal service operations following an incident |
    |OPR-22 | SPE operator MUST adopt robust security measures to protect data, including the use of firewalls, encryption, and intrusion detection systems, in order to prevent unauthorised access, modification, or removal of sensitive information |
    |OPR-23 | Health data users, HDAB staff and SPE Operator staff who interact with the SPE MUST receive detailed, role-specific information or training covering health data processing, EHDS compliance requirements and security best practices coming from GDPR |
    |OPR-24 | The SPE Operator MUST implement strategies for backup management, disaster recovery, and crisis management |
    |OPR-25 | The SPE Operator MUST implement cybersecurity procedures to regularly evaluate the effectiveness of risk-management measures and promote fundamental cybersecurity practices and provide necessary training |
    |OPR-26 | SPE Operator SHOULD define SLAs that include: uptime guarantees, response/resolution times for incidents include security SLAs, such as data encryption guarantees, incident response times, and audit logging |
    |OPR-27 | The SPE Operator SHOULD regularly restore backups to the platform as part of standard feature development and operational activities, ensuring preparedness for incident response |
    |OPR-28 | The SPE operator MUST implement a formal patch management policy to identify, evaluate, and apply security patches in a timely manner based on severity |
    |OPR-29 | SPE Operator MUST establish a system update process to ensure timely and secure updates of software, OS, and firmware, tested prior to deployment |
    |OPR-30 | A change management process SHOULD be used for assessing the impact of patches and updates before applying them to the production environment |
    |OPR-31 | SPE Operator MUST provide dedicated technical support with clearly defined SLAs and escalation paths for addressing incidents and technical issues |
    |OPR-32 | SPE Operator support staff SHOULD be trained in information security and privacy procedures, with roles and responsibilities clearly defined |
    |OPR-33 | A knowledge base and support documentation SHOULD be maintained to assist in common issue resolution and improve incident response times |

??? abstract "Federated (FSPE) requirements"
    | ID | Requirements |
    |----|--------------|
    |FSPER-1 | Legal or contractual agreement MUST cover the SPE federation across organisations |
    |FSPER-2 | Federation use identities MUST match over services |
    |FSPER-3 | SPE federation environment MUST fulfil sensitive data processing requirements defined for stand-alone SPEs |
    |FSPER-4 | All interactive user actions on sensitive data in the federation MUST be through SPE |
    |FSPER-5 | Federation governance structure MUST cover secure, shared data access and export from SPE |
    |FSPER-6 | Federation user identities SHOULD be shared |
    |FSPER-7 | Federation of SPEs MUST share technical and semantic interoperability needed for shared processing |
    |FSPER-8 | Federation of SPEs MUST use shared secure communication and data transfer protocols |
    |FSPER-9 | The federation MUST support distributed processing through authorisation and accounting services |
    |FSPER-10 | A federation SPE MAY fulfil federated processing requirements |

???+ abstract "Federated computing (FC) requirements"
    | ID | Requirements |
    |----|--------------|
    |FCR-1 | SPE MUST support common data models, such as OMOP CDM and applicable GA4GH standards, to enable technical and semantic interoperability |
    |FCR-2 | The HDAB MUST have in place (internally or in collaboration with SPE operators) required processes to deploy additional data models required by data users |
    |FCR-3 | SPE MUST support the deployment and execution of software components needed to carry out federated computing as described and authorised in the data permit, subject to applicable security controls |
    |FCR-4 | The HDAB MUST have in place required processes to authorise the use of software components needed in federated computing |
    |FCR-5 | SPE MUST enable a data user application to retrieve anonymous results from the SPE to be merged with results retrieved from other SPEs |
    |FCR-6 | SPE MUST include functionality for ensuring the anonymity of results, with applicable methods such as: (1) pre-assessment of software components producing the results, (2) automated anonymity assessment, (3) additional privacy protection mechanisms (such as differential privacy) and (4) manual inspections |
    |FCR-7 | The HDAB MUST have established processes for approving computerised access permissions for data user applications in the context of data permit authorisation |
    |FCR-8 | SPE MUST provide an open and standardised interface needed to exchange information with other trusted SPEs as needed to accomplish federated learning computations |
    |FCR-9 | SPE SHOULD support the use of privacy protection methods (such as differential privacy) for federated learning |


??? abstract "Technical Interoperability (TIR) requirements"
    | ID | Requirements |
    |----|--------------|
    |TIR-1 | The API services MUST be accessed via data user and data holder applications, which can be dedicated client applications or browser-based applications.|
    |TIR-2 | The API MUST follow a web services architecture (e.g., RESTful, GraphQL), enabling stateless request/response interactions and supporting secure file transfer protocols. The implementation MUST adhere to common architectural and security practices, including resource grouping and, where appropriate, the use of microservices to isolate sensitive services.|
    |TIR-3 | The API MUST operate over HTTPS, ensuring compatibility with standard web clients and server implementations. Additionally, it MUST support secure file transfer protocols (e.g. HTTPS, SFTP or FTPS for file operations) where applicable.|
    |TIR-4 | The API MUST use JSON as the primary data format for requests and responses with support for other formats where needed, ensuring secure data transfer via HTTPS or other secure protocols.|
    |TIR-5 | The API MUST be capable of uploading and downloading files of all standard file types. It MUST be possible to set restrictions on allowed file types and transfer direction (upload/download) through configuration settings separately for each API and workspace. The API must support efficient handling of large files, including resumable transfers, asynchronous processing where necessary, and configurable timeout settings to accommodate long-lasting operations.|
    |TIR-6 | API SHOULD have clear, machine-readable documentation (e.g., OpenAPI/Swagger).|
    |TIR-7 | All requests to data user and data holder API functions MUST be authenticated and authorised using standard methods (e.g., OAuth 2.0 with JWT, API keys). The system MUST enforce role-based access control, limiting access based on user roles and privileges.|
    |TIR-8 | API communication MUST use encryption (e.g., TLS) to protect data in transit. Additionally, it MUST be possible to enforce application-level encryption (e.g., AES-256) before transmission to provide an extra layer of security. If content encryption is used, keys MUST be securely managed and stored according to industry best practices (e.g., using a dedicated key management system).|
    |TIR-9 | The API MUST validate all incoming data to prevent injection attacks (e.g., SQLi, XSS) and malformed requests, responding only to predefined and approved requests with valid parameters.|
    |TIR-10 | Error responses MUST avoid exposing sensitive details (e.g., stack traces, internal error codes) while providing meaningful messages for debugging.|
    |TIR-11 | API access MAY be restricted based on network-level controls, including firewall rules, IP whitelisting, or Virtual Private Network (VPN) restrictions.|
    |TIR-12 | Requests, responses, and errors MUST be logged for monitoring and compliance.|
    |TIR-13 | API usage, failures, performance metrics and service availability MUST be monitored, with alerts for anomalies.|
    |TIR-14 | Mechanisms MUST be in place for approving and deploying new API versions and phasing out old API versions.|
    |TIR-15 | The API SHOULD meet defined latency and response time SLAs.|
    |TIR-16 | The system SHOULD handle expected and peak loads efficiently, with rate limiting and throttling mechanisms in place if necessary.|
    |TIR-17 | The API SHOULD ensure the accuracy and consistency of requests and responses by applying relevant format validators and other appropriate validation mechanisms, thereby preventing the delivery of erroneous, corrupted or inconsistent data.|
    |TIR-18 | The remote desktop interface MUST enable the data user to interactively access and process data with a remote desktop application|
    TIR-19 | The data user MAY use a standard browser or a dedicated client to access the remote desktop environment.|
    |TIR-20 | The remote desktop solution MUST support remote desktop clients running on standard operating systems including (e.g., Windows, macOS, Linux).|
    |TIR-21 | The remote desktop solution MUST use a secure remote access protocol (e.g., RDP, VNC, or SSH with X11 forwarding) to establish a connection between the client and server. The communication protocol MUST support encryption to protect data in transit.|
    |TIR-22 | Access MUST require multifactor authentication (MFA). The system MUST enforce role-based access control, limiting remote access based on user roles and privileges.|
    |TIR-23 | Access MAY be restricted based on network-level controls, including firewall rules, IP whitelisting, or VPN restrictions.|
    |TIR-24 | Idle sessions MUST be automatically terminated after a predefined time to prevent unauthorised access. Users MUST be logged out or locked after a period of inactivity.|
    |TIR-25 | Clipboard sharing and file transfers MUST be restricted by default to prevent unauthorised export of data from the SPE. Changes to or removal of these restrictions MUST be configurable at the discretion of the HDAB.|
    |TIR-26 | All remote sessions MUST be logged, including authentication attempts, connection times, and actions performed during the session.|
    |TIR-27 | Service usage, failures, performance metrics and service availability MUST be monitored, with alerts for anomalies.|
    |TIR-28 | The service endpoint MUST enable communication between trusted SPEs to support federated learning.|
    |TIR-29 | The interface MUST support protocols needed to support client-server and bidirectional streaming communication (gRPC with HTTP/2 or an equivalent). Connections MUST be secured using TLS.|
    |TIR-30 | All connections MUST be authenticated using appropriate methods such as mutual TLS (mTLS) or token-based authentication while ensuring all data is transmitted over an encrypted channel.|
    |TIR-31 | Only pre-approved clients with valid certificates MUST be allowed to connect.|
    |TIR-32 | The interface MAY be configured to restrict access using firewall rules, IP whitelisting, VPN access, other network-level policies and holistic approaches such as virtual closed networks.|
    |TIR-33 | All requests, responses, and streaming events MUST be logged securely.|
    |TIR-34 | Real-time monitoring of streaming sessions, errors, latency, and security threats MUST be implemented. Alerts shall be generated based on anomalous activity (e.g., failed authentication attempts, unusual data patterns).|
    |TIR-35 | The interface MUST meet defined latency and response time SLAs.|
    |TIR-36 | The system MUST implement flow control to manage varying loads and prevent overloads, using rate limiting, throttling, and adaptive resource allocation as needed.|