# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0003_auto_20171030_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mattach',
            name='att',
        ),
        migrations.DeleteModel(
            name='Mattach',
        ),
    ]
