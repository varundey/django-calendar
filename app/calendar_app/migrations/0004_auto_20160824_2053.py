# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_auto_20160824_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(23, 53, 31)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(20, 53, 31)),
        ),
    ]