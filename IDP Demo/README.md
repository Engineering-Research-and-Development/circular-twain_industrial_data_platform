## IDP Demo Deployment

This is a minimal deployment of the Industrial Data Platform. It contains the following components:
- A OPCUA Server code with a simulated battery working environment
- The FIWARE IoT Agent for OPCUA
- The FIWARE PyPpark Connector with a custom algorithm injected in Apache PySpark
- The FIWARE Orion Context Broker
- A MySQL database


### Requirements for demo:

You need to install python3 and pyspark to correcly launch the demo.


### How to configure and launch the Demo:

- In the Connector/ServerOPCUA.py file search for the URL on the top of the file and change it to your local IP
- In the docker-compose.yml file, search for the ENV variable *IOTA_OPCUA_ENDPOINT* and change the endpoint to match the previous one
- In the Connector/connectorconf.py file change the *HTTPADDRESS*, *HTTP_PORT* and *SOCKET_PORT* to match respectively your local IP and available ports

Once configured correctly, go in the main folder and type
```
cd Connector
python3  
```


```
docker-compose up 
```

The demo is set up and works!
