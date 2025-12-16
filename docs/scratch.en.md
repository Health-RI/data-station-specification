## Data stations as foundational building blocks for a network of secure processing environments

The hourglass model is a powerful framework for achieving widespread data interoperability by balancing flexibility with standardization. [cite_start]It draws inspiration from the architecture of the internet, which successfully connects countless different applications (the wide top) over numerous physical network technologies (the wide bottom) by forcing all traffic through a minimal, universal standard—the "waist" of the hourglass (TCP/IP)[cite: 19, 212, 248]. Similarly, a data interoperability hourglass allows for a wide variety of domain-specific data creation tools and analytical applications, while ensuring they can all connect through a common, machine-readable format.

[cite_start]The FAIR Hourglass model provides a socio-technical framework that organizes data activities into two main phases—**FAIRification** (top) and **FAIR Orchestration** (bottom)—connected by a narrow, standardized center[cite: 14, 134]. [cite_start]The width of the hourglass represents the "freedom to operate," which is greatest at the top and bottom where users create and analyze data using their preferred methods, and most constrained at the center to ensure interoperability[cite: 68, 71].

***

### The Five Layers of the FAIR Hourglass

The model is broken down into five distinct layers that guide data from its raw state to a reusable asset. 
## FAIRification (Top)

**Layer 1: Raw Data Creation**
[cite_start]This top layer represents the creation and capture of raw data and metadata[cite: 73, 77]. [cite_start]At this stage, researchers and domain experts have maximum freedom, using established community practices and their preferred tools, from handwritten notes to specialized software[cite: 69, 119].

---

**Layer 2: Harmonization**
In this layer, the raw data begins its journey toward standardization. [cite_start]It is a "funneling" process where tools are used to harmonize the data and metadata, converting them into more structured formats using machine-readable vocabularies and schemas[cite: 89, 122].

## Center of the Hourglass

**Layer 3: FAIR-Ready Data (The "Waist")**
[cite_start]This is the narrowest, most critical part of the model, acting as the bridge between the two phases[cite: 67]. [cite_start]Here, data and metadata are rendered as **machine-actionable information** according to a minimal, open, and technology-independent standard[cite: 81, 82, 90]. [cite_start]This standardized format, or "spanning layer," ensures that data from any source can be understood and processed by various automated services[cite: 250]. [cite_start]In the context of health data, a standard like FHIR is well-suited to function as this spanning layer[cite: 255].

## FAIR Orchestration (Bottom)

**Layer 4: Automated Services**
[cite_start]Once data is FAIR-ready, it is exposed to the internet through gateways like FAIR Data Points or APIs[cite: 91, 127]. [cite_start]This allows automated services to perform operations like indexing, searching, semantic resolution, and data integration[cite: 92, 128]. [cite_start]This layer puts the FAIR data into action[cite: 57].

---

**Layer 5: Data Reuse and Analytics**
[cite_start]At the bottom of the hourglass, the "freedom to operate" is restored[cite: 69, 88]. [cite_start]End-users can now leverage high-level applications to perform complex data analytics, conduct data landscape surveys, or run distributed learning models on the integrated, interoperable data, leading to new insights[cite: 93, 129].
