# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0004_auto_20171101_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='attach',
            name='thumbnl',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
