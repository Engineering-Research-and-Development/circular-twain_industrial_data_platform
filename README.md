
<p align="center">
  <img  src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/48c05e6d-ccbc-488f-97f9-bce4cbde07f2">
</p>


# Circular TwAIn Industrial Data Platform Architecture


The Circular TwAIn industrial data platform facilitates seamless and secure data sharing among various parties. It achieves this by implementing a centralized software architecture that collects data from ethereogeneus digital twin sources and makes it discoverable to consumers through a digital services marketplace. The platform includes an identity and access management layer that ensures data can only be accessed by authorized parties. This layer enforces a policy-based access mechanism to the data broker component, based on previous transactions that occurred in the marketplace.
 

### Table of Content:
- [Industrial Data Platform Components](#industrial-data-platform-components)
- [Data Producer Journey](#data-producer-journey)
- [Data Consumer Journey](#data-consumer-journey)


## Industrial Data Platform Components

<p align="center">
 <img width=845 heigth=460 src="https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/assets/103200695/c10fc91a-90b1-4c02-b25f-6376e34181f7">
  <br />
  <b>Fig. 1:</b> The industrial Data Platform Architecture
</p>

The industrial data platform architecture involves three types of entities:
- the **centralized IDP itself**: the entity who owns and maintain the technological stack, ensuring the secure data brokering among parties.
- The **data producer**: the entity in charge of pushing data to the centralized platform and making them available inside the marketplace. The data producer may correspond also to the role of data owner however, generally speaking, the data provider and data owner roles are considered separate. Referring to the Circular TwAIn reference architecture, they implement the physical layer from whose data are sourced.
- The **data consumer**: the entity who is able to browse different data service in the marketplace, selects the desided one and acquires the right to access data throught a marketplace transaction.

In this section it is provided a focused overview on the centralized IDP technological stack, explaining how each component fits with the other to implement the desided functionalities.


### Data Brokering Layer

The data brokering layer is covered by the [**FIWARE Orion Context Broker**](https://fiware-orion.readthedocs.io/en/master/) implementing the [**NGSI-LD APIs**](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf). Orion is a central component of the industrial data platform and it is in charge of allowing users to query (in case of data consumers) or writing/update (in case of data producers) context information. By implementing the NGSI-LD standard, it is possible to link entities through relationships, provide property graphs and semantics thanks to the [JSON-LD](https://json-ld.org/) standard, thus leveraging the Smart Data Model Initiative.


### Digital Models and Vocabularies

The [**Smart Data Models Initiative**](https://www.fiware.org/smart-data-models/) implements the digital models and vocabulary vertical of the Circular TwAIn reference architecture. This initiative results particularly suitable in the digital twin context since it aims to standardize data models under common structures, hence improving data interoperability. Thanks to the smart data models, the data producer can refer to common structures for their digital twin, making available their *schema* (or a part of it) in Orion and the *specification* in the marketplace, highliting which of the attributes are available to consumers. Moreover, *example payloads* in NGSI-LD standard are available to producers to share those information correctly.




## Data Producer Journey

## Data Consumer Journey

