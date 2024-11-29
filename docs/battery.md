# Battery Pilot

![image](https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/blob/main/docs/imgs/Battery.png)

## Scenario

The Battery Pilot aims to create a **Digital Battery Passport (DBP)** for automotive batteries, compliant with the **RAMI 4.0 AAS standard**. The DBP consolidates data across the battery lifecycle, from material sourcing to recycling. It is based on the [**BatteryPass Data Model**](https://github.com/batterypass/BatteryPassDataModel) and requires integration of heterogeneous data (e.g., logs, tables, CAD files) from distributed stakeholders like suppliers, manufacturers, and recyclers. Sensitive data must be securely accessed and shared.

Stakeholders act in two roles:  
1. **Data Provider**: Integrate and share data through a common DBP structure in the Data Space.  
2. **Data Consumer**: Access shared data for analytics.

In the first scenario, providers process battery-related data (e.g., EIS test results, usage logs) using **Pandas** and **PySpark**, structure it according to RAMI 4.0 standards, and share it via a **Data Space Connector** like TRUE Connector. In the second scenario, consumers retrieve data from the Data Space via connectors (e.g., Eclipse Dataspace Connector), update the DBP in the **AASX Server**, and use FIWARE tools for advanced analytics.

The DBP supports traceability, transparency, and secure data sharing in battery lifecycle management.

---

## Technical Details

### Architecture Overview
The DBP uses a containerized architecture with services for data integration, sharing, and analytics. Core components:  
- **AASX Server**: Hosts DBP data structured per RAMI 4.0.  
- **Data Space Connectors**: Enable secure data exchange (TRUE Connector, Eclipse Dataspace Connector).  
- **FIWARE Ecosystem**: Provides analytics (FIWARE AAS Agent, Orion Context Broker).  
- **Apache Spark Cluster**: Processes and analyzes data.

### Data Provider Workflow
1. Process data (EIS test results, logs) in Python using **Pandas** and **PySpark**.  
2. Structure data per RAMI 4.0 DPP standards.  
3. Store structured data in AASX Server.  
4. Share data via TRUE Connector in Data Space.

### Data Consumer Workflow
1. Retrieve data from Data Space using TRUE Connector.  
2. Update DBP in AASX Server.  
3. Sync with FIWARE Orion using FIWARE AAS Agent.  
4. Process data in PySpark for analytics (e.g., SparkML).

### Dockerized Setup
- **AASX Server**: Uses `adminshellio` image, runs on port 5001.  
- **MongoDB**: Provides storage for FIWARE Orion, connects via `mongodb://mongo`.  
- **FIWARE Orion**: Context Broker on port 1026.  
- **Apache Spark**: Spark master and worker nodes configured via PySpark images, connected through `pyspark_net`.  

### Networking and Configurations
- Custom bridge network (`pyspark_net`) with IP subnet 172.28.0.0/16.  
- Logging capped at 200 MB per file for Spark services.  

The architecture supports distributed data processing, secure sharing, and advanced analytics. Designed for modularity and scalability.
