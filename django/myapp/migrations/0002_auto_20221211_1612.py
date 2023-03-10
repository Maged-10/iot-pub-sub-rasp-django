# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2022-12-11 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperatureandhumiditydata',
            name='accelX',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperatureandhumiditydata',
            name='accelY',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperatureandhumiditydata',
            name='accelZ',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperatureandhumiditydata',
            name='latitude1',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperatureandhumiditydata',
            name='longitude1',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
