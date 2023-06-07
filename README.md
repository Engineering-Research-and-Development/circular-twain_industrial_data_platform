
<p align="center">
  <img  src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/48c05e6d-ccbc-488f-97f9-bce4cbde07f2">
</p>



# Circular TwAIn Industrial Data Platform (IDP) Architecture


The Circular TwAIn Industrial Data Platform is a technology infrastructure based on open source components enabling ingestion, transformation, mapping and brokering of digital twin data generated within an industrial environment. It serves as a local hub for managing and integrating data from etherogeneous sources, such as sensors, machines, devices, and production systems, ensuring data to converge in standardized models. Thanks to the Smart Data Models initiative, digital twin data could be easily exchanged with other Industrial Data Space participants through IDS Connectors.

 

### Table of Content:
- [Industrial Data Platform Components](#industrial-data-platform-components)
- [Setup](#setup)


## Industrial Data Platform Components

<p align="center">
 <img width=845 heigth=460 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/7997ed5a-7fa9-4a82-baad-d428ee5b86fb">
  <br />
  <b>Fig. 1:</b> The Industrial Data Platform Architecture
</p>


The Industrial Data Platform architecture covers the following functionalities:
- the **Data Ingestion and Brokering**: the Industrial Data Platform is able to receive data from the physical world (Physical - Virtual Twinning), as well as to send commands to digital twins (Virtual - Physical Twinning). Meanwhile, the current state of the digital twin is made available to users thanks to the brokering function.
- the **Data Processing**: *transformation and mapping* techniques are applied to raw data, allowing users to standardize raw sensor data from etherogeneous sources to *Smart Data Models*.
- The **Data Persistence**: whenever necessary, the Industrial Data Platform is designed to persist historical data, in particular when time-series data are involved in fast-changing digital twin.
- The use of **Smart Data Models and Vocabularies**: finally, the Industrial Data Platform operators are provided with a comprehensive range of standardized data models and metadata vocabularies. This crucial provision enables the facilitation of seamless communication within an Industrial Data Space environment.

In this section it is provided a focused overview on the centralized IDP technological stack, explaining how each component fits with the other to implement the desided functionalities.


### Data Ingestion and Brokering 

The data brokering layer is covered by the [**FIWARE Orion Context Broker**](https://fiware-orion.readthedocs.io/en/master/) implementing the [**NGSI-LD APIs**](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf). Orion is a central component of the Industrial Data Platform and it is in charge of allowing users to query (in case of data consumers) or writing/update (in case of data producers) context information. By implementing the NGSI-LD standard, it is possible to link entities through relationships, provide property graphs and semantics thanks to the [JSON-LD](https://json-ld.org/) standard, thus leveraging the Smart Data Model Initiative.


### Data Processing
**Streampipes??**


### Data Persistence

A set of databases are implicitly implemented in the data persistence layer to support all components. In particular:
- [**mongoDB**](https://www.mongodb.com/docs/): a non-realtional database that supports both the Marketplace and Orion-LD components.
- [**MySQL**](https://dev.mysql.com/doc/): a Relational Database Management System that supports the Keyrock components to store users, applications and policies.
- [**elasticsearch**](https://www.elastic.co/guide/index.html): a non-relational database based on Apache Lucene that implements a powerful search engine for the marketplace.


Moreover, the following components are implemented to make historical data storage possible:
- [**FIWARE Mintaka**](https://github.com/FIWARE/mintaka): a Orion-LD component implementing NGSI-LD temporal API.
- [**TimescaleDB**](https://docs.timescale.com/): a high performance PostgreSQL database designed to work with time-series data.


### Digital Models and Vocabularies

The [**Smart Data Models Initiative**](https://www.fiware.org/smart-data-models/) implements the digital models and vocabulary vertical of the Circular TwAIn reference architecture. This initiative results particularly suitable in the digital twin context since it aims to standardize data models under common structures, hence improving data interoperability. Thanks to the smart data models, the data producer can refer to common structures for their digital twin, making available their *schema* (or a part of it) in Orion. Moreover, *specifications* and *example payloads* in NGSI-LD standard are available to operators to facilitate transformation and mapping operations.




### Identity and Access Management Layer

The identity and access management layer implements the security technological stack to control access to data. The following components are deployed in the Industrial Data Platform architecture:
- [**FIWARE Keyrock**](https://fiware-idm.readthedocs.io/en/latest/): Keyrock is the FIWARE component primarly responsible for Identity Management, thus offering a user the possibility to create an identity-providing account. Keyrock administrators are allowed to create multiple applications, each of which can be enriched with roles associated to particular permissions. In this context, two applications should be instantiated: the *Orion Context Broker* application with the "producer" and "consumer" roles, and the *Marketplace* application with the "seller" and "customer" roles. Those roles have grants, respectively, to read/write and read-only data in their corresponding application. By doing so, keyrock implements the Policy Decision Point (PDP) functionality, implementing PDP Access Control Level 1 (Authentication Access) and Level 2 (Basic Authorization) for the corresponding application.
- [**FIWARE AuthZForce**](https://authzforce-ce-fiware.readthedocs.io/en/latest/): AuthZForce completes the PDP functionality of the security layer, implementing the PDP access control Level 3 (Advanced Authorization) thanks to its fine-grained access policies written in XACML.
- [**FIWARE-PEP-PROXY WILMA**](https://fiware-pep-proxy.readthedocs.io/en/latest/): Wilma is an implementation of a PEP-proxy, used in the platform to come between the user and Orion so that it can intercept their requests and redirect them to the Policy Decision Point, implemented by the Keyrock and AuthZForce pair. 



## Setup



