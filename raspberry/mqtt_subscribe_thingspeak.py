#!/usr/bin/env python

import time
import os
import requests
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:	
	print("Connected to broker")
    else:
	print("Connection failed")


def on_message(client, userdata, message):
    print("message topic:       " + message.topic)
    print("message received:    " + str(message.payload.decode("utf-8")))
    msg = json.loads(str(message.payload.decode("utf-8")))

    channel =      msg['channel_id'] 
    creationDate = msg['created_at']
    entryNumber =  msg['entry_id']
    humidity =     msg['field1']
    temperature =  msg['field2']
    accelx =       msg['field3']
    accely =       msg['field4']
    accelz =       msg['field5']
    latitude =     msg['field6']
    longitude =    msg['field7']


def on_log(client, userdata, level, buf):
    print("log: " + buf)

# ThingSpeak MQTT Broker: do not change
THINGS_DEVICE_MQTTSERV = "mqtt3.thingspeak.com"

#Channel ID: Enter your channel id!
CHANNELID = "1936894"

#ThingSpeak Device user name: Enter your personal user name!
THINGS_DEVICE_USERNAME = "DxszICsqFg43Ni0XIDkxDTI"

#ThingSpeak Device password: Enter your password!
THINGS_DEVICE_PASSWORD = "ZStgNez+kLx5GWyw0XOGoZmc"

#ThingSpeak Device client id: Enter the client id!
CLIENT_NAME = "DxszICsqFg43Ni0XIDkxDTI"

#ThingSpeaks standard MQTT port number: do not change
PORT=1883

#Some additional parameters: leave these values unchanged
KEEPALIVE=600
QOS_LEVEL=0

client = mqtt.Client(CLIENT_NAME)               #create new instance
client.username_pw_set(username=THINGS_DEVICE_USERNAME, password=THINGS_DEVICE_PASSWORD)    #set username and password
client.on_connect = on_connect                      #attach function to callback
client.on_message = on_message                      #attach function to callback

client.connect(THINGS_DEVICE_MQTTSERV, port=PORT)  #connect to broker
client.subscribe("channels/" + CHANNELID + "/subscribe")
client.loop_forever()
