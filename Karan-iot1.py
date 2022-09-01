
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


# Install below packages
'''
sudo pip3 install azure-iot-device
sudo pip3 install azure-iot-hub
sudo pip3 install azure-iothub-service-client
sudo pip3 install azure-iothub-device-client
'''

# Run below on Azure CLI
'''
#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

'''

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=Karan-iot.azure-devices.net;DeviceId=mydevice;SharedAccessKey=7ldLEBvvatW0cKVsK9D31rOt8d9BUsiUjVgwYHpBhMY="

# Define the JSON message to send to IoT Hub.
PH = 6.5
TURBUDITY = 0.5
CHLORINE = 3
DISSOLVED_OXYGEN = 6.5
ORP=6.5
MSG_TXT = '{{"turbudity": {turbudity},"ph": {ph},"chlorine":{chlorine},"dissolved_oxygen": {dissolved_oxygen}, "orp"={orp}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with simulated telemetry values.
            #temperature = TEMPERATURE + (random.random() * 15)
            #co = CO + (random.random() * 15)
            #no2 = NO2 + (random.random() * 15)
            #nh3=NH3 + (random.random() * 15)
            turbudity=random. randint(0,3)
            ph=random. randint(0,20)
            chlorine=random. randint(0,8)
            dissolved_oxygen=random. randint(0,10)
            orp=random. randint(0,700)
            msg_txt_formatted = MSG_TXT.format(turbudity=turbudity, ph=ph, chlorine=chlorine, dissolved_oxygen=dissolved_oxygen, orp=orp)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if temperature > 30:
              #message.custom_properties["temperatureAlert"] = "true"
            #else:
              #message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()

