import asyncio
import logging
import random
 

from asyncua import ua, uamethod, Server, Client


URL = "opc.tcp://10.0.2.15:4840/freeopcua/server/"


@uamethod
async def Start(parent):

    
    
    async with Client(url= URL) as client:
        
        namespace = "http://examples.freeopcua.github.io"
        nsidx = await client.get_namespace_index(namespace)
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:Mode"]
        )
    
        await var.write_value("STARTED")
        
        var2 = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:RPM"]
        )
    
        await var2.write_value(3000.0)
        
        
        var3 = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:EnergyConsumption_KWh"]
        )
    
        await var3.write_value(3.0)

        print ("Switched to: STARTED")
        
        
        

@uamethod       
async def Stop(parent):

    async with Client(url= URL) as client:
        
        namespace = "http://examples.freeopcua.github.io"
        nsidx = await client.get_namespace_index(namespace)
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:Mode"]
        )
    
        await var.write_value("STOPPED")
        
        
        var2 = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:RPM"]
        )
    
        await var2.write_value(0.0)
        
        var3 = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:EnergyConsumption_KWh"]
        )
    
        await var3.write_value(0.0)

        print ("Switched to: STOPPED")


@uamethod       
async def Increase_power(parent):

    async with Client(url= URL) as client:
        
        namespace = "http://examples.freeopcua.github.io"
        nsidx = await client.get_namespace_index(namespace)
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:Mode"]
        )
    
        await var.write_value("EMPOWERING")
        print ("Switched to: EMPOWERING")
        


@uamethod       
async def Decrease_power(parent):

    async with Client(url= URL) as client:
        
        namespace = "http://examples.freeopcua.github.io"
        nsidx = await client.get_namespace_index(namespace)
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Battery_Pack", f"{nsidx}:Mode"]
        )
    
        await var.write_value("DEPOWERING")
        print ("Switched to: DEPOWERING")
    
        

 


async def main():
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)
   
    # now setup our server
    server = Server()
    await server.init()
    # server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    server.set_endpoint(URL)
    server.set_server_name("FreeOpcUa Example Server")
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

 

   # setup our own namespace
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

 

   # get Objects node, this is where we should put our custom stuff
    objects = server.nodes.objects

 

   # populating our address space
    myobj = await objects.add_object(idx, "Battery_Pack")
    temp = await myobj.add_variable(idx, "Temperature_degC", float(20.5))
    await temp.set_modelling_rule(True)
    await temp.set_writable()  # Set MyVariable to be writable by clients
    IR = await myobj.add_variable(idx, "Curr_Internal_Resistance_Pack", float(150.0))
    await IR.set_modelling_rule(True)
    await IR.set_writable()  # Set MyVariable to be writable by clients
    above = await myobj.add_variable(idx, "Time_spent_above_temperature", float(0.0))
    await above.set_modelling_rule(True)
    await above.set_writable()  # Set MyVariable to be writable by clients
    below = await myobj.add_variable(idx, "Time_spent_below_temperature", float(0.0))
    await below.set_modelling_rule(True)
    await below.set_writable()  # Set MyVariable to be writable by clients

    
    
    
    async with server:
        print("Listening on 10.0.2.15:4840")
        
        while True:
            try:
                await asyncio.sleep(1)
                
                my_temp = await temp.get_value()
                my_IR = await IR.get_value()
                my_above = await above.get_value()
                my_below = await below.get_value()
                
                
                temp_delta = float(random.gauss(0, 3.3))
                new_temp = my_temp + temp_delta
                
                if new_temp > 80 or new_temp < -70:
                    new_temp = my_temp
                    
                new_IR = my_IR - float(temp_delta*0.15)
                
                if new_temp < -40.0:
                    new_below = float(my_below + 1)
                    await below.set_value(new_below)
                    
                if new_temp > 50.0:
                    new_above = float(my_above + 1)
                    await above.set_value(new_above)
                    
                await temp.set_value(new_temp)
                await IR.set_value(new_IR)
                
                   
  
                print("Values updated")
                await asyncio.sleep(1)
                
            except Exception as e:
                #await server.stop()
                print(e)
                print("Server Disconnected")
                break

 


if __name__ == "__main__":
    asyncio.run(main())


