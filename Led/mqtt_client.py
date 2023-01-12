#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os
import sys
import requests
import json
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

MQTTHOST = "192.168.0.1"
CLIENT_NAME = "IoTXY"
PORT=1883
KEEPALIVE=600
QOS_LEVEL=0

MQTT_SUBSCRIBE_TOPIC = "pi/actuators/led/set"
MQTT_PUBLISH_TOPIC   = "pi/actuators/led/get"
MQTT_LED_STATE_ON    = "On"
MQTT_LED_STATE_OFF   = "Off"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    print "\nBegin: Publish data ..."
    try:
		MQTT_PUBLISH_PAYLOAD = json.dumps({'Led': MQTT_LED_STATE_OFF})
		#Insert your code here! 
		#Publish JSON encoded message "MQTT_PUBLISH_PAYLOAD" { "Led" : Off }
        #....
    except:
        print("There was an error while publishing the data!")


def on_message(client, userdata, message):
    print("message received:    " + str(message.payload.decode("utf-8")))
    print("message topic:       " + message.topic)
    decodedMessage = json.loads(str(message.payload.decode("utf-8")))
    if decodedMessage['Led']=="On":
		pass
		#Remove the "pass" instruction and insert your code here:
		#Switch on the led: 
		#...
		#Publish the JSON encoded message "MQTT_LED_STATE_ON" as an acknowledgement;
		#(see function on_connect):
		#...
    if decodedMessage['Led']=="Off":
		pass
		#Remove the "pass" instruction and insert your code here:
		#Switch off the led: 
		#...
		#Publish the JSON encoded message "MQTT_LED_STATE_OFF" as an acknowledgement;
		#(see function on_connect):
		#...


def on_log(client, userdata, level, buf):
    print("log: " + buf)


try:
    # Remove the following instruction!!
    GPIO.cleanup()
    
    #Insert your code here:
    #use the predefined parameters;
    #create a mqtt paho client;
    #attach functions "on_connect", "on_message" and "on_log" to callback;
    #connect to the "MQTTHOST";
    #subscribe to "MQTT_SUBSCRIBE_TOPIC";
    #and "loop_forever()";


except KeyboardInterrupt:
    GPIO.cleanup()
    print "Exiting"
    sys.exit(0)