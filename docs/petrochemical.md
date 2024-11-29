# Petrochemical Blueprint

![image](https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/blob/main/docs/imgs/Petro.png)


## Scenario

The **Petrochemical Pilot** focuses on leveraging AI-driven predictions to reduce material waste, optimize production, and support the circular economy within petrochemical production. The pilot’s core objective is to enhance sustainability throughout the petrochemical lifecycle by improving resource efficiency and reducing waste. To achieve this, a **Hybrid Circular Twin** is being developed, an **Asset Administration Shell (AAS)** implementation that digitally represents both the physical plant and its production process. This digital twin enables real-time monitoring and optimization of plant operations.

The **Integrated Data Platform (IDP)** is focused on the data provider side, facilitating two main objectives: 
1. **Integrating data** into the Hybrid Circular Twin. 
2. **Preparing data for AI analysis** in remote environments.

The IDP handles data from two main sources:
- **Real-time data** from the PHD Uniformance system, ingested via the OPCUA standard.
- **Historical data** in CSV format, processed in a Python environment.

The data flow begins with real-time data, captured via the **PHD Uniformance OPCUA interface**, and ingested into the **FIWARE ecosystem**. This is achieved using the **OPCUA Agent** and the **Orion Context Broker**. Then, the data is transferred to the **PySpark environment** via the **FIWARE PySpark Connector**, where it is merged with historical data and pre-processed to remove outliers and fill missing values. The pre-processed data is then transferred into the AAS model via the **AASX Server**, forming the **Hybrid Circular Twin**.

A key goal of the pilot is **Edge-side data quality improvement**, ensuring that only clean and reliable data is used for the AAS model. This data quality approach facilitates the **cloud-edge continuum** and supports collaboration with remote stakeholders for analyzing the **Hybrid Circular Twin**. The **TRUE Connector** ensures secure, bi-directional data sharing within the **Data Space**, enabling collaboration with remote analytics systems.

---

## Technical Details

### Architecture Overview
The system integrates various services to manage and optimize data flow, support IoT devices, and enable big data processing:
- **Hybrid Circular Twin**: Combines real-time and historical data for digital twin creation and optimization.
- **FIWARE Ecosystem**: Ingests and processes real-time data (via OPCUA) and integrates it into the overall system for analysis.
- **AASX Server**: Manages asset administration shells, creating the digital representation of physical assets and production processes.
- **Data Pre-Processing**: Combines real-time data with historical data for advanced analytics in PySpark.
- **AI Integration**: Real-time predictions in a remote environment for optimized decision-making and process improvements.

### Core Services
- **aasx-server**: A containerized version of the **AdminShell AASX Server** provides asset administration for managing and interacting with the digital twin. It is exposed on port 5005.
- **mongo**: A MongoDB service used as a database for storing context and AAS-related data. It uses the `--nojournal` flag to reduce I/O overhead for development use.
- **orion**: The **Fiware Orion Context Broker** handles context information, managing real-time data streams and exposing the service on port 1026.
- **opcua**: An **IoT Agent** for Fiware, integrating OPC UA data streams into the ecosystem, providing real-time monitoring and analytics.
- **spark-master & spark-worker-a**: Apache Spark services based on the **Fiware PySpark connector image**, managing distributed data processing and computation. The setup includes a custom network (`pyspark_net`) for isolated communication between the nodes.

### Networking and Persistence
- **pyspark_net**: Custom Docker network with a subnet (172.28.0.0/16) for isolated Spark communication.
- **Volumes**: Data persistence across container restarts, including for MongoDB, Spark, and other services.
- **Environment Configuration**: Each service is configured with environment variables for flexibility, including options for OPCUA subscription management and Spark resource allocation.

---

## Setup & Deployment

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform.git
   cd src/use-cases/
   ```

2. **Ensure Required Tools**
- Docker (latest version)
- Docker Compose

3. **Run Docker Compose**
   ```bash
   docker-compose up -f docker-compose-petro.yaml -d
   ```

4. **Access Servicese**
- *AASX Server:* http://localhost:5005
- *FIWARE Orion Context Broker:* http://localhost:1026
- *Jupyter Notebook:* http://localhost:8888

5. **Stop Services**
   ```bash
   docker-compose down
   ```

6. **Persist Data**
- Volumes are automatically configured to store service data for reuse across container restarts.
