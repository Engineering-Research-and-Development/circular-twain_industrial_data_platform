import orion_pyspark_connector as connector
import subscribing_tool as sub
from pyspark import SparkContext, SparkConf, StorageLevel
from datetime import datetime


import os
import psutil
import time
import numpy as np
import json



#sub.SubscribeToEntity("http://localhost:1026/v2/")


conf = SparkConf().setAppName("FIWARE Orion-PySpark Connector Demo").set("spark.hadoop.yarn.resourcemanager.address", "local[2]")
sc = SparkContext(conf=conf)



def MonitorAndAct(iter):
    #"2:Temperature_degC", "2:RPM", "2:EnergyConsumption_KWh", "2:Mode"
    for entity in iter:

        temp = float(entity.attrs['Battery_PackTemperature_degC'].value)
        resist = float(entity.attrs['Battery_PackCurr_Internal_Resistance_Pack'].value)
        above = float(entity.attrs['Battery_PackTime_spent_above_temperature'].value)
        below = float(entity.attrs['Battery_PackTime_spent_below_temperature'].value)
        
        api = "http://localhost:1026/v2/entities/age01_Battery_Pack/attrs/"
        
        print("Incoming data are... Temperature: {}, Internal Resistance: {}, Time spent overheating: {}, Stime spent below temperature threshold : {}".format(temp, resist, above, below))
        
        max_sec = 10000
        tot_sec_spent = above+below
        rem_sec = max_sec - tot_sec_spent
        percnt = np.round((rem_sec/max_sec*100), 2)
        
        body = '{"Battery_Status" : {"value" :' +f'{percnt}' +', "type":"Number"}}'
        print(body)
        r = connector.UnstructuredReplyToBroker(body)
        print(r)
        
        
            
    return


    



event, ssc = connector.Prime(sc, 1 , StorageLevel.MEMORY_AND_DISK_2)
entity = event.flatMap(lambda x: x.entities)
entity.foreachRDD(lambda rdd: rdd.foreachPartition(MonitorAndAct))


print("Reading Technical data from MySQL")
time.sleep(0.5)
print("Technical data read")
        
        
ssc.start()


while True:
	try:
		time.sleep(600)
	except Exception as e:
		#f.close()
		sys.exit(0)
#ssc.awaitTermination()
