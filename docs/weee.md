# WEEE Blueprint

![image](https://github.com/Engineering-Research-and-Development/circular-twain_industrial_data_platform/blob/main/docs/imgs/WEEE.png)

## Scenario

The WEEE Pilot focuses on enhancing de-manufacturing processes for electronic waste via human-robot collaboration. It integrates a **Product Digital Twin** and a **Process Digital Twin** to optimize throughput. The **Product Digital Twin** provides static information (e.g., CAD files, specifications, component market value), while the **Process Digital Twin** captures dynamic, real-time production line data. Interaction between these twins ensures efficient workflows, updating machinery with product data and recording dismantling operations in real time.

The **Integrated Data Platform (IDP)** aggregates data from both twins to enable on-site cognition. Data flows from:  
- **Eclipse BaSyx**: Source of the Product Digital Twin.  
- **NOVAAS**: Source of the Process Digital Twin.  
- **EMQX MQTT Broker**: Ingests twin data into the IDP.  
- **Elastic Stack**: Routes and stores data using Logstash and Elasticsearch.  

The combined data supports real-time AI predictions in **TensorFlow**, enabling robotics (e.g., camera-guided arms) to improve dismantling efficiency. Data sharing is facilitated by **Data Space technologies** integrated via the **EDC Connector**.

---

## Technical Details

### Architecture Overview
The architecture integrates multiple services to support Digital Twin interaction, data aggregation, and AI-powered automation. Key components include:  
- **BaSyx AAS Components**: Registry, GUI, and AAS server for managing the Product Digital Twin.  
- **NOVAAS Framework**: Provides Process Digital Twin data.  
- **EMQX MQTT Broker**: Handles data ingestion.  
- **Elastic Stack**: Elastic Logstash for pre-processing, Elasticsearch for storage and analytics.  
- **TensorFlow**: Real-time AI model predictions for robotic efficiency.  
- **EDC Connector**: Facilitates secure data exchange in Data Spaces.  

### Core Services
- **Kafka**: Manages messaging with configurable replication, brokers, and listeners (ports 9092, 9093).  
- **Elastic Stack**: Elasticsearch v8.7.1 for storage and Kibana for visualization, secured via CA certificates.  
- **TensorFlow**: Jupyter notebook environment for AI development (port 8888).  
- **BaSyx Components**:  
  - **Registry**: Hosts AAS metadata (port 4000).  
  - **AAS Server**: Exposes API for AAS management (port 4001).  
  - **GUI**: Web-based interface for managing AAS (port 3000).  
  - **PostgreSQL**: Database for registry (port 5432).  
  - **MongoDB**: Database for AAS server (port 27017).  

### Networking and Persistence
- Custom Docker network `weee` for isolated communication.  
- Volumes for persistent data storage: certs, esdata01, kibanadata, and others.  
- Secure inter-service communication enabled by encryption keys and CA certificates.

### AI Integration
- **TensorFlow**: Processes real-time data for predictive analytics.  
- **Robotic Arms**: Leverage camera vision and Digital Twin data to enhance dismantling operations.

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
   docker-compose up -f docker-compose-weee.yaml -d
   ```

4. **Access Servicese**
- *BaSyx GUI:* http://localhost:3000
- *Jupyter Notebook (TensorFlow):* http://localhost:8888
- *Kibana:* http://localhost:5601

5. **Stop Services**
   ```bash
   docker-compose down
   ```

6. **Persist Data**
- Volumes are automatically configured to store service data for reuse across container restarts.
