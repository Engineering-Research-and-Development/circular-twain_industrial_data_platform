## IDP Demo Deployment

This is a minimal deployment of the Industrial Data Platform. It contains the following components:
- A OPCUA Server code with a simulated battery working environment
- The FIWARE IoT Agent for OPCUA
- The FIWARE PyPpark Connector with a custom algorithm injected in Apache PySpark
- The FIWARE Orion Context Broker
- A MySQL database


### Requirements for demo:

You need to install python3, [Spark](https://www.virtono.com/community/tutorial-how-to/how-to-install-apache-spark-on-ubuntu-22-04-and-centos/) and [PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) to correcly launch the demo.

for ubuntu users:
```
apt-get install python3
pip install pyspark
```

### How to configure and launch the Demo:

- In the Connector/ServerOPCUA.py file search for the URL on the top of the file and change it to your local IP
- In the docker-compose.yml file, search for the ENV variable *IOTA_OPCUA_ENDPOINT* and change the endpoint to match the previous one
- In the Connector/connectorconf.py file change the *HTTPADDRESS*, *HTTP_PORT* and *SOCKET_PORT* to match respectively your local IP and available ports

Once configured correctly, go in the main folder and type
```
cd Connector
python3 ServerOPCUA-py
```

```
docker-compose up 
```

The demo is now set up!


### How to launch the algorithm

Go in the Connector folder and launch the starting script:
```
cd Connector
python3 start.py
```

Then subscribe the entity created in Orion by the IoT Agent to the PySpark connector:

```
curl -L -X POST 'http://localhost:1026/v2/subscriptions/' -H 'Content-Type: application/json' \
- H 'Fiware-Service: idpdemo' -H 'Fiware-ServicePath: /demo' \
--data-raw '{
  "description": "Subscription to IDP",
  "subject": {
    "entities": [
      {
        "id": "age01_Battery_Pack",
        "type": "Device"
      }
    ],
    "condition": {
      "attrs": ["Battery_PackTemperature_degC"]
    }
  },
  "notification": {
    "http": {
      "url": "http://PYSPARK_CONNECTOR_HTTP_ADDRESS:PYSPARK_CONNECTOR_HTTP_PORT"
    },
    "attrs": ["Battery_PackTemperature_degC", "Battery_PackCurr_Internal_Resistance_Pack", "Battery_PackTime_spent_above_temperature", "Battery_PackTime_spent_below_temperature"]
  },
  "expires": "2099-01-01T14:00:00.00Z"
}'
```

And then you should see the pyspark code computing when new data arrive
