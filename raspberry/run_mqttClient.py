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

MQTTHOST = "192.168.5.20"
CLIENT_NAME = "IoTXY"
PORT=1883
KEEPALIVE=600
QOS_LEVEL=0

MQTT_SUBSCRIBE_TOPIC = "pi/26/actuators/led/set"
MQTT_PUBLISH_TOPIC   = "pi/26/actuators/led/get"
MQTT_LED_STATE_ON    = "On"
MQTT_LED_STATE_OFF   = "Off"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    print "\nBegin: Publish data ..."
    try:
        MQTT_PUBLISH_PAYLOAD = json.dumps({'Led': MQTT_LED_STATE_OFF})
        client.publish(MQTT_PUBLISH_TOPIC, MQTT_PUBLISH_PAYLOAD)
    except:
        print("There was an error while publishing the data!")


def on_message(client, userdata, message):
    print("message received:    " + str(message.payload.decode("utf-8")))
    print("message topic:       " + message.topic)
    decodedMessage = json.loads(str(message.payload.decode("utf-8")))
    if decodedMessage['Led']=="On":
        GPIO.output(11,1)
        #Publish the JSON encoded message "MQTT_LED_STATE_ON" as an acknowledgement;
        try:
            MQTT_PUBLISH_PAYLOAD = json.dumps({'Led': MQTT_LED_STATE_ON})
            client.publish(MQTT_PUBLISH_TOPIC, MQTT_PUBLISH_PAYLOAD)
        except:
            print("There was an error while publishing the data!")
    if decodedMessage['Led']=="Off":
        GPIO.output(11,0)
        #Publish the JSON encoded message "MQTT_LED_STATE_OFF" as an acknowledgement;
        try:
            MQTT_PUBLISH_PAYLOAD = json.dumps({'Led': MQTT_LED_STATE_OFF})
            client.publish(MQTT_PUBLISH_TOPIC, MQTT_PUBLISH_PAYLOAD)
        except:
            print("There was an error while publishing the data!")


def on_log(client, userdata, level, buf):
    print("log: " + buf)


try:

    client = mqtt.Client(CLIENT_NAME)               #create new instance
    #client.username_pw_set(username=THINGS_DEVICE_USERNAME, password=THINGS_DEVICE_PASSWORD)    #set username and password
    client.on_connect = on_connect                      #attach function to callback
    client.on_message = on_message                      #attach function to callback

    client.connect(MQTTHOST, port=PORT)  #connect to broker
    client.subscribe(MQTT_SUBSCRIBE_TOPIC)
    client.loop_forever()


except KeyboardInterrupt:
    GPIO.cleanup()
    print "Exiting"
    sys.exit(0)
