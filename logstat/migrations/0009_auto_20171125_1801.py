# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0008_auto_20171125_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmlatt',
            name='xml_added_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 25, 16, 1, 20, 967848, tzinfo=utc)),
        ),
    ]
