import os
import requests
import json
import paho.mqtt.publish as publish
import ssl # we want to use secured web sockets

#from django_unixdatetimefield import UnixDateTimeField
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from myapp.models import *
from django.template import RequestContext

# Create your views here.
def index(request):

    # Connection method: use SSLWebsockets --->
    #tTransport = "websockets"
    #tPort = 443
    #tTSL = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    # <---

    THINGSAPIGETKEY = "CPGZ7QE40HYBKZ6B"
    CHANNELID = "1936894"
    MQTT_HOST = "api.thingspeak.com"

    # Get the most actual channel feed
    '''PAYLOAD_STRING = "{'api_key': '" + THINGSAPIGETKEY + "', 'results': '1'}"
    JSON_PAYLOAD_STRING = PAYLOAD_STRING.replace("'", "\"")
    GET_PAYLOAD = json.loads(JSON_PAYLOAD_STRING)
    GET_REQUEST = "https://" + MQTT_HOST + "/channels/" + CHANNELID + "/feeds.json"
    r = requests.get(GET_REQUEST , data=GET_PAYLOAD)

    text = json.loads(r.text)
    feed = text['feeds'][0]
    channel = text['channel']
    sensorName = channel['name']
    creationDate = feed['created_at']
    entryNumber = feed['entry_id']
    temperature = feed['field2']
    humidity = feed['field1']
    accelX = feed['field3']
    accelY = feed['field4']
    accelZ = feed['field5']
    latitude1 = feed['field6']
    longitude1 = feed['field7']
    latitude = 48.40885
    longitude = 9.95301'''


    # Create a new database entry
    '''table = TemperatureAndHumidityData()
    table.temperature = temperature
    table.humidity = humidity
    table.accelX = accelX
    table.accelY = accelY
    table.accelZ = accelZ
    table.latitude1 = latitude1
    table.longitude1 = longitude1
    table.lat = latitude
    table.lon = longitude
    table.save()'''

    # Get most actual database entry
    tempData = TemperatureAndHumidityData.objects.order_by('-id')[0]
    temperature = tempData.temperature
    humidity = tempData.humidity
    accelX = tempData.accelX
    accelY = tempData.accelY
    accelZ = tempData.accelZ
    latitude1 = tempData.latitude1
    longitude1 = tempData.longitude1
    '''lat = tempData.lat
    lon = tempData.lon'''

#    return HttpResponse("Myapp says hey there partner!")
    return render_to_response('index.html',{'temperature': temperature, 'humidity': humidity, 'accelX': accelX , 'accelY': accelY , 'accelZ': accelZ,'latitude1': latitude1, 'longitude1': longitude1}, context_instance=RequestContext(request))
