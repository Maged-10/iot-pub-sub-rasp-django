from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TemperatureAndHumidityData(models.Model):
    timestamp = models.CharField(max_length=10)
    temperature = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    accelX = models.CharField(max_length=7)
    accelY = models.CharField(max_length=7)
    accelZ = models.CharField(max_length=7)
    latitude1 = models.CharField(max_length=10)
    longitude1 = models.CharField(max_length=10)
    '''lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)'''
    def __unicode__(self):
        return self.timestamp  

