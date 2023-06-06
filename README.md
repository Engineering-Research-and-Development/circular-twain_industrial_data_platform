
<p align="center">
  <img  src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/48c05e6d-ccbc-488f-97f9-bce4cbde07f2">
</p>



# Circular TwAIn Industrial Data Platform (IDP) Architecture


The Circular TwAIn Industrial Data Platform is a technology infrastructure based on open source components enabling collection, exchange and monetization of large volumes of data generated within an industrial environment. It serves as a central hub for managing and integrating data from various sources, such as sensors, machines, devices, and production systems, ensuring data governance and sovereignty among different parties. The platform includes an identity and access management layer that ensures data can only be accessed by authorized parties. This layer enforces a policy-based access mechanism to the data broker component, based on previous transactions that occurred in the marketplace.
 

### Table of Content:
- [Industrial Data Platform Components](#industrial-data-platform-components)
- [Administration Setup](#administration-setup)
- [Data Producer Journeys](#data-producer-journeys)
- [Data Consumer Journeys](#data-consumer-journeys)


## Industrial Data Platform Components

<p align="center">
 <img width=845 heigth=460 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/7997ed5a-7fa9-4a82-baad-d428ee5b86fb">
  <br />
  <b>Fig. 1:</b> The Industrial Data Platform Architecture
</p>



The Industrial Data Platform architecture involves three types of entities:
- the **centralized IDP itself**: the entity who owns and maintain the technological stack, ensuring the secure data brokering among parties.
- The **data producer**: the entity in charge of pushing data to the centralized platform and making them available inside the marketplace. The data producer may correspond also to the role of data owner however, generally speaking, the data provider and data owner roles are considered separate. Referring to the Circular TwAIn reference architecture, they implement the physical layer from whose data are sourced.
- The **data consumer**: the entity who is able to browse different data service in the marketplace, selects the desided one and acquires the right to access data throught a marketplace transaction.

In this section it is provided a focused overview on the centralized IDP technological stack, explaining how each component fits with the other to implement the desided functionalities.


### Data Brokering Layer

The data brokering layer is covered by the [**FIWARE Orion Context Broker**](https://fiware-orion.readthedocs.io/en/master/) implementing the [**NGSI-LD APIs**](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf). Orion is a central component of the Industrial Data Platform and it is in charge of allowing users to query (in case of data consumers) or writing/update (in case of data producers) context information. By implementing the NGSI-LD standard, it is possible to link entities through relationships, provide property graphs and semantics thanks to the [JSON-LD](https://json-ld.org/) standard, thus leveraging the Smart Data Model Initiative.


### Digital Models and Vocabularies

The [**Smart Data Models Initiative**](https://www.fiware.org/smart-data-models/) implements the digital models and vocabulary vertical of the Circular TwAIn reference architecture. This initiative results particularly suitable in the digital twin context since it aims to standardize data models under common structures, hence improving data interoperability. Thanks to the smart data models, the data producer can refer to common structures for their digital twin, making available their *schema* (or a part of it) in Orion and the *specification* in the marketplace, highliting which of the attributes are available to consumers. Moreover, *example payloads* in NGSI-LD standard are available to producers to share those information correctly.


### Data Persistence Layer

A set of databases are implicitly implemented in the data persistence layer to support all components. In particular:
- [**mongoDB**](https://www.mongodb.com/docs/) is a non-realtional database that supports both the Marketplace and Orion-LD components
- [**MySQL**](https://dev.mysql.com/doc/) is a Relational Database Management System that supports the Keyrock components to store users, applications and policies
- [**elasticsearch**](https://www.elastic.co/guide/index.html) is a non-relational database based on Apache Lucene that implements a powerful search engine for the marketplace

Moreover, the following components are


### Human and Application Layer

The human and application layer in the centralized platform is implemented by the [**FIWARE Business API Ecosystem**](https://business-api-ecosystem.readthedocs.io/en/latest/) developed by FIWARE and TMForum. It enables data producers to generate offerings that expose their digital twin data. It also enables data consumers to explore and purchase data services. The marketplace includes the NGSI-LD Policies Plugin, which adds a product asset capable of creating access policies within the security layer components for consumers who have acquired a specific digital service. When the consumer acquires rights to access data, the marketplace will also provide him the access token necessary to make future queries in Orion.


### Identity and Access Management Layer

The identity and access management layer implements the security technological stack to control access to data. The following components are deployed in the Industrial Data Platform architecture:
- [**FIWARE Keyrock**](https://fiware-idm.readthedocs.io/en/latest/): Keyrock is the FIWARE component primarly responsible for Identity Management, thus offering a user the possibility to create an identity-providing account. Keyrock administrators are allowed to create multiple applications, each of which can be enriched with roles associated to particular permissions. In this context, two applications should be instantiated: the *Orion Context Broker* application with the "producer" and "consumer" roles, and the *Marketplace* application with the "seller" and "customer" roles. Those roles have grants, respectively, to read/write and read-only data in their corresponding application. By doing so, keyrock implements the Policy Decision Point (PDP) functionality, implementing PDP Access Control Level 1 (Authentication Access) and Level 2 (Basic Authorization) for the corresponding application.
- [**FIWARE AuthZForce**](https://authzforce-ce-fiware.readthedocs.io/en/latest/): AuthZForce completes the PDP functionality of the security layer, implementing the PDP access control Level 3 (Advanced Authorization) thanks to its fine-grained access policies written in XACML.
- [**FIWARE-PEP-PROXY WILMA**](https://fiware-pep-proxy.readthedocs.io/en/latest/): Wilma is an implementation of a PEP-proxy, used in the platform to come between the user and Orion so that it can intercept their requests and redirect them to the Policy Decision Point, implemented by the Keyrock and AuthZForce pair. 



## Administration Setup




## Data Producer Journeys

In this section it is explained how a data producer became allowed to push digital twin data in Orion Context Broker and publish its offering in the Marketplace:

### Prerequisites
- The user registered an account in the Identity Provider component (keyrock)
- The user knows the data structure of the digital twin or (preferrably) uses the data structure of the smart data model
- An empty Digital Twin entity was created by the platform administrator in Orion
- The user contacted the platform administrator, expressing its will to join the platform as a producer. The administrator enabled him the "Producer" role for Orion (expressing the desired entity) and the "Seller" role for the marketplace

### Journey 1: pushing new data

- The producer
- The producer uses the access token provided by Keyrock to push new data as a HTTP PATCH request to the context broker





## Data Consumer Journeys

