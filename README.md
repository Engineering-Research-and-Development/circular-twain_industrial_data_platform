
<p align="center">
  <img  src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/48c05e6d-ccbc-488f-97f9-bce4cbde07f2">
</p>



# Circular TwAIn Industrial Data Platform (IDP) Architecture


The Circular TwAIn Industrial Data Platform is a technology infrastructure based on open source components enabling ingestion, transformation, mapping and brokering of digital twin data generated within an industrial environment. It serves as an optional *local hub* for managing and integrating data from heterogeneous sources, such as sensors, machines, devices, and production systems, ensuring data to adhere to defined models. The Industrial Data Platform is designed to be deployed at the ends of the industrial data space network to acting as a *Man-in-the-Middle* between digital twins and the Data Space itself. 
Hence, the Industrial Data Platform fits well in the following contexts:
- **Brownfield Integration**: the Industrial Data Platform can extend existing digital twins with new technologies thanks to its flexibility.
- **Integration of several data sources**: the platform allows the integration of heterogeneous data sources through Extraction Transformation and Loading (ETL) operations.
- **Cognition enabling**: the IDP enables digital twins with cognition thanks to batch and real-time data processing.
- **Data Space connection**: thanks to deployment of data space connectors, data providers can connect with other data space actors and share their data.
 

### Table of Content:
- [Industrial Data Platform Components](#industrial-data-platform-components)
- [Setup](#setup)


## Industrial Data Platform Components



<p align="center">
 <img width=485 heigth=800 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/61032760-37b0-4ce4-b3e6-e464d4b77363">
  <br />
  <b>Fig. 1:</b> The Industrial Data Platform Architecture (Digital Twin View)
</p>




The Industrial Data Platform architecture covers the following functionalities:
- the **Data Ingestion and Brokering**: the Industrial Data Platform is able to receive data from existing entities, such as physical products, processes, humans and/or their digital twin representation, enabling a bi-directional communication with them. The platform is also able to integrate in a flexible way with other systems such as NOVAAS or FAAAST. In the end, the brokering components are in charge to provide both the state of digital twins and the results coming from the processing layer. 
- the **Data Processing**: *transformation and mapping* techniques are applied to data, allowing users to work on data from heterogeneous data sources while adhering to data models. This layer also enables cognition to digital twins, enabling batch and real-time processing on their data.
- The **Data Persistence**: whenever necessary, the Industrial Data Platform is designed to persist historical data, in particular when time-series data are involved in fast-changing entities.
- The **Data Models and Vocabularies**: finally, the Industrial Data Platform operators are provided with a comprehensive range of standardized data models and metadata vocabularies thanks to both *Asset Administration Shell* and *FIWARE Smart Data Models* initiative. This crucial provision enables the facilitation of seamless communication within an Industrial Data Space environment.

In this section it is provided a focused overview on the centralized IDP technological stack, explaining how each component fits with the other to implement the desided functionalities.


### Data Ingestion and Brokering 

- [**FIWARE Orion Context Broker**](https://fiware-orion.readthedocs.io/en/master/) implementing the [**NGSI-LD APIs**](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf), in the Industrial Data Platform context, allows users to query and update context information. By implementing the NGSI-LD and [JSON-LD](https://json-ld.org/) standards, it is possible to link entities through relationships, provide property graphs and semantics, thus enabling the use of the Smart Data Model Initiative.
- [**Apache Kafka**](https://kafka.apache.org/documentation/) is an open-source distributed streaming platform designed for handling high-volume, real-time data streams. Kafka is based on a publish-subscribe messaging model, where data is organized into topics where data records are published to these topics to be consumed by other components. Kafka offers high throughput and low latency, making it ideal for use cases such as real-time analytics. Kafka integrates well with other big data frameworks and systems such as Apache Stremapipes, allowing seamless data integration and processing pipelines.
- [**IDAS Agents**](https://www.fiware.org/catalogue/) include a set of FIWARE generic enablers acting as an interface to the IoT world. They are able to gather data from ethereogeneous sources of data using different IoT protocols but also to send commands back to the observabnle layer, hence enabling a bidirectional communication with both digital twins and physical entities.
- [**FIWARE O2K**](https://github.com/Engineering-Research-and-Development/o2k-connector) The O2K-Connector, developed in Python, is a lightweight connector that facilitates the sharing of context data from the Orion Context Broker to Apache Kafka. This connector operates by subscribing to the Orion Context Broker and subsequently publishing the received context data to a dedicated Kafka topic integrated within the connector itself.
- **Custom DT Connectors** can be deployed to connect with digital twins in a flexible way, allowing the integration of other DT systems and services such as NOVAAS or FAAAST.



### Data Processing

- [**Apache StreamPipes**](https://streampipes.apache.org/docs/docs/user-guide-introduction.html) is an open-source IoT Toolbox designed for building and managing real-time data pipelines in a simple and flexible manner. It provides a visual programming interface that allows users to easily create data pipelines by connecting various data sources, processors, and sinks. It offers a wide range of connectors, processors, and visualization components, making it suitable for various use cases of data integration. StreamPipes emphasizes interoperability, enabling users to efficiently handle streaming data workflows and derive valuable insights from their data streams.
- [**Apache Spark**](https://spark.apache.org/) is a powerful engine suitable for processing batch and real time data in a scalable way. Thanks to its Python API, [PySpark](https://spark.apache.org/docs/latest/api/python/), it is possible to integrate efficient python algorithms to enable digital twin cognition.
- [**FIWARE PySpark Connector**](https://github.com/Engineering-Research-and-Development/fiware-orion-pyspark-connector) is a generic enabler receiving notification from context brokers such as Orion, parsing and injecting incoming data into PySpark algorithms. It helps processing real-time data incoming from southbound layers, returning results directly to the broker.
- **XAI Open Source Libraries** such as [**LIME**](https://github.com/marcotcr/lime) or [**SHAP**](https://shap.readthedocs.io/en/latest/) can be used to add explainability to AI algorithms. Explainability enhances human understanding of AI predictions and gives further insights on the analyzed context.
- The [**Suite5 AI Engine**] is a tool that facilitates the creation of complex AI and XAI pipelines connecting data processing algorithms encapsulated in modules. In the Industrial Data Platform environment it can also implement collaboration functionality, allowing heterogeneously-skilled teams to implement Digital Twins cognition.



### Data Persistence

A set of databases are implemented in the data persistence layer both as support tools for existing components and to store data:
- [**mongoDB**](https://www.mongodb.com/docs/) is a non-realtional database that supports the Orion-LD component.
- [**MySQL**](https://dev.mysql.com/doc/) is a relational Database Management System (DBMS) that supports the Keyrock components to store users, applications and policies.
Moreover, the following components are implemented to make historical data storage possible:
- [**FIWARE Mintaka**](https://github.com/FIWARE/mintaka) is an Orion-LD component implementing NGSI-LD temporal API, hence allowing the retrieval of past data.
- [**TimescaleDB**](https://docs.timescale.com/): a high performance PostgreSQL database designed to work with time-series data.



### Digital Models and Vocabularies

- The [**Smart Data Models Initiative**](https://www.fiware.org/smart-data-models/) implements the digital models and vocabulary vertical of the Circular TwAIn reference architecture. This initiative aims to standardize data models under common structures to improve data interoperability. Thanks to the Smart Data Models, a data producer can refer to common structures for their digital twin, making available their *schema* (or a part of it) in Orion. Moreover, *specifications* and *example payloads* in NGSI-LD standard are available to operators to facilitate transformation and mapping operations.
- The [**Digital Product Passports (DPP)**](https://hadea.ec.europa.eu/calls-proposals/digital-product-passport_en) are tools under development proposed by the European Commission to create transparency and enable circularity in supply chains. They facilitate the sharing of comprehensive product information, including data on raw material extraction, production, and recycling. DPP will impact companies, and resources are available to understand the regulations and implications through reports provided by WBCSD and BCG. These passports offer a policy perspective, corporate guidance, and actionable steps to prepare for the future of value chains.




### Identity and Access Management Layer

The identity and access management layer implements the security technological stack to control access to data. The following components are deployed in the Industrial Data Platform architecture:
- [**FIWARE KeyRock**](https://fiware-idm.readthedocs.io/en/latest/) is the FIWARE component primarly responsible for Identity Management, thus offering a user the possibility to create an identity-providing account. Keyrock administrators are allowed to create multiple applications, each of which can be enriched with roles associated to particular permissions. In this context, organization might want the Orion-LD Context Broker to be protected from unauthorized access. By doing so, KeyRock would implement the Policy Decision Point (PDP) functionality with PDP Access Control Level 1 (Authentication Access).
- [**FIWARE-PEP-Proxy Wilma**](https://fiware-pep-proxy.readthedocs.io/en/latest/) implements a PEP-proxy, that could be used in the platform in conjunction with KeyRock to intercept user requests directed to Orion so that it can redirect them to the Policy Decision Point.
- [**Verifiable credentials**](https://www.w3.org/TR/vc-data-model/) are digital representations of physical credentials that contain information about the subject, issuing authority, credential type, asserted attributes, evidence of derivation, and constraints. They are made more secure and trustworthy through technologies like digital signatures. Holders of verifiable credentials can generate verifiable presentations to prove possession of specific credentials to verifiers. This digital format allows for rapid transmission and convenient establishment of trust over long distances.
- [**Self-sovereign identity (SSI)**](https://ec.europa.eu/futurium/en/system/files/ged/eidas_supported_ssi_may_2019_0.pdf) empowers individuals with control over their digital identity, allowing them to prove who they are online. It eliminates reliance on third parties large identity providers. Without SSI, users face fragmented web experiences or creating multiple accounts. SSI enables streamlined and secure access to services while maintaining control over personal identity information.



## Setup



