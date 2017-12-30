# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-03 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0017_auto_20171126_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standalone',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 12, 3, 17, 54, 42, 829921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='xmlatt',
            name='xml_added_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 3, 17, 54, 42, 830921, tzinfo=utc)),
        ),
    ]
