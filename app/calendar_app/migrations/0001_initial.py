# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('all_day', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
