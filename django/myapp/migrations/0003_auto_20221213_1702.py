# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2022-12-13 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20221211_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperatureandhumiditydata',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='temperatureandhumiditydata',
            name='lon',
        ),
    ]
