
<p align="center">
  <img  src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/48c05e6d-ccbc-488f-97f9-bce4cbde07f2">
</p>



# Circular TwAIn Industrial Data Platform (IDP) Architecture


The Circular TwAIn Industrial Data Platform is a technology infrastructure based on open source components enabling ingestion, transformation, mapping and brokering of digital twin data generated within an industrial environment. It serves as a *local hub* for managing and integrating data from etherogeneous sources, such as sensors, machines, devices, and production systems, ensuring data to converge in standardized models: the Industrial Data Platform is deployed at the ends of the industrial data platform network. Thanks to the Smart Data Models initiative, digital twin data could be easily exchanged with other Industrial Data Space participants through IDS Connectors.

 

### Table of Content:
- [Industrial Data Platform Components](#industrial-data-platform-components)
- [Setup](#setup)


## Industrial Data Platform Components


<p align="center">
 <img width=1200 heigth=820 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/d4fcc889-85a2-41ca-8ee2-cdcc93166acc">
 <br />
 <b>Fig. 1:</b> Industrial Data Platform mapped on Circular TwAIn Reference Architecture
</p>


The Industrial Data Platform architecture covers the following functionalities:
- the **Data Ingestion and Brokering**: the Industrial Data Platform is able to receive data from the physical world (Physical - Virtual Twinning), as well as to send commands to digital twins (Virtual - Physical Twinning). Meanwhile, the current state of the digital twin is made available to users thanks to the brokering function.
- the **Data Processing**: *transformation and mapping* techniques are applied to raw data, allowing users to work on raw sensor data from etherogeneous sources to build Standardized Data Models.
- The **Data Persistence**: whenever necessary, the Industrial Data Platform is designed to persist historical data, in particular when time-series data are involved in fast-changing digital twins.
- The **Data Models and Vocabularies**: finally, the Industrial Data Platform operators are provided with a comprehensive range of standardized data models and metadata vocabularies thanks to the *FIWARE Smart Data Models* initiative. This crucial provision enables the facilitation of seamless communication within an Industrial Data Space environment.

In this section it is provided a focused overview on the centralized IDP technological stack, explaining how each component fits with the other to implement the desided functionalities.

<p align="center">
 <img width=485 heigth=800 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/8fe0a076-c925-4051-a4f1-e55f715ff06e">
  <br />
  <b>Fig. 2:</b> The Industrial Data Platform Architecture (Digital Twin View)
</p>


### Data Ingestion and Brokering 

- [**FIWARE Orion Context Broker**](https://fiware-orion.readthedocs.io/en/master/) implementing the [**NGSI-LD APIs**](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf), in the Industrial Data Platform context, allows users to query and update context information. By implementing the NGSI-LD and [JSON-LD](https://json-ld.org/) standards, it is possible to link entities through relationships, provide property graphs and semantics, thus enabling the use of the Smart Data Model Initiative.
- [**Apache Kafka**](https://kafka.apache.org/documentation/) is an open-source distributed streaming platform designed for handling high-volume, real-time data streams. Kafka is based on a publish-subscribe messaging model, where data is organized into topics where data records are published to these topics to be consumed by other components. Kafka offers high throughput and low latency, making it ideal for use cases such as real-time analytics. Kafka integrates well with other big data frameworks and systems such as Apache Stremapipes, allowing seamless data integration and processing pipelines.
- [**IDAS Agents**](https://www.fiware.org/catalogue/) include a set of FIWARE generic enablers acting as an interface to the IoT world. They are able to gather data from ethereogeneous sources of data using different IoT protocols but also to send actuation commands back to the physical layer, hence enabling a bidirectional communication with the physical world.



### Data Processing

- [**Apache StreamPipes**](https://streampipes.apache.org/docs/docs/user-guide-introduction.html) is an open-source IoT Toolbox designed for building and managing real-time data pipelines in a simple and flexible manner. It provides a visual programming interface that allows users to easily create data pipelines by connecting various data sources, processors, and sinks. With StreamPipes, the Industrial Data Platform operator can design and implement pipelines useful to map streaming data from diverse Digital Twins to Smart Data Models. It offers a wide range of connectors, processors, and visualization components, making it suitable for various use cases of data integration. StreamPipes emphasizes interoperability, enabling users to efficiently handle streaming data workflows and derive valuable insights from their data streams.
- [**Python**](https://docs.python.org/3/) is one of the most popular programming language for data analysis and manipulation thanks to the large community support and library repository it provides. Common data analysis and manipulation libraries, such as *pandas*, *numpy*, *scipy* or *scikit-learn* are suitable for the Industrial Data Platform operators to write custom algorithms for transforming and mapping raw digital twin data into Smart Data Model structures.



### Data Persistence

A set of databases are implemented in the data persistence layer both as support tools for existing components and to store data:
- [**mongoDB**](https://www.mongodb.com/docs/) is a non-realtional database that supports the Orion-LD component.
- [**MySQL**](https://dev.mysql.com/doc/) is a relational Database Management System (DBMS) that supports the Keyrock components to store users, applications and policies.
Moreover, the following components are implemented to make historical data storage possible:
- [**FIWARE Mintaka**](https://github.com/FIWARE/mintaka) is an Orion-LD component implementing NGSI-LD temporal API, hence allowing the retrieval of past data.
- [**TimescaleDB**](https://docs.timescale.com/): a high performance PostgreSQL database designed to work with time-series data.



### Digital Models and Vocabularies

- The [**Smart Data Models Initiative**](https://www.fiware.org/smart-data-models/) implements the digital models and vocabulary vertical of the Circular TwAIn reference architecture. This initiative results particularly suitable in the digital twin context since it aims to standardize data models under common structures to improve data interoperability. Thanks to the Smart Data Models, a data producer can refer to common structures for their digital twin, making available their *schema* (or a part of it) in Orion. Moreover, *specifications* and *example payloads* in NGSI-LD standard are available to operators to facilitate transformation and mapping operations.
- The [**Asset Administration Shell (AAS)**](https://www.iec.ch/ords/f?p=103:38:614011165317679::::FSP_ORG_ID,FSP_APEX_PAGE,FSP_PROJECT_ID:1250,23,103536) serves as the standardized digital depiction of an asset, forming the foundation for the interoperability of components in Industrie 4.0 systems. The AAS can represent a simple component, a machine, or a plant at any level within the equipment hierarchy. Manufacturers provide their customers with standardized digital representations by creating AASs for each asset type and instance. Throughout the lifespan of an asset, the information within its AAS is updated by system designers, asset users, applications, processes, and the asset itself, until its eventual disposal.
- The [**Digital Product Passports (DPP)**](https://hadea.ec.europa.eu/calls-proposals/digital-product-passport_en) are tools under development proposed by the European Commission to create transparency and enable circularity in supply chains. They facilitate the sharing of comprehensive product information, including data on raw material extraction, production, and recycling. DPP will impact companies, and resources are available to understand the regulations and implications through reports provided by WBCSD and BCG. These passports offer a policy perspective, corporate guidance, and actionable steps to prepare for the future of value chains.




### Identity and Access Management Layer

The identity and access management layer implements the security technological stack to control access to data. The following components are deployed in the Industrial Data Platform architecture:
- [**FIWARE KeyRock**](https://fiware-idm.readthedocs.io/en/latest/) is the FIWARE component primarly responsible for Identity Management, thus offering a user the possibility to create an identity-providing account. Keyrock administrators are allowed to create multiple applications, each of which can be enriched with roles associated to particular permissions. In this context, organization might want the Orion-LD Context Broker to be protected from unauthorized access. By doing so, KeyRock would implement the Policy Decision Point (PDP) functionality with PDP Access Control Level 1 (Authentication Access).
- [**FIWARE-PEP-Proxy Wilma**](https://fiware-pep-proxy.readthedocs.io/en/latest/) implements a PEP-proxy, that could be used in the platform in conjunction with KeyRock to intercept user requests directed to Orion so that it can redirect them to the Policy Decision Point.
- [**Verifiable credentials**](https://www.w3.org/TR/vc-data-model/) are digital representations of physical credentials that contain information about the subject, issuing authority, credential type, asserted attributes, evidence of derivation, and constraints. They are made more secure and trustworthy through technologies like digital signatures. Holders of verifiable credentials can generate verifiable presentations to prove possession of specific credentials to verifiers. This digital format allows for rapid transmission and convenient establishment of trust over long distances.
- [**Self-sovereign identity (SSI)**](https://ec.europa.eu/futurium/en/system/files/ged/eidas_supported_ssi_may_2019_0.pdf) empowers individuals with control over their digital identity, allowing them to prove who they are online. It eliminates reliance on third parties large identity providers. Without SSI, users face fragmented web experiences or creating multiple accounts. SSI enables streamlined and secure access to services while maintaining control over personal identity information.



## Setup



