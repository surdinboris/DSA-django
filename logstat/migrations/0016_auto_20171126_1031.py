# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0015_auto_20171126_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standalone',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 8, 31, 50, 197476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='standalone',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logstat.Source'),
        ),
        migrations.AlterField(
            model_name='xmlatt',
            name='xml_added_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 8, 31, 50, 198977, tzinfo=utc)),
        ),
    ]
