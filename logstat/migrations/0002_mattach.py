# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logstat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mattach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(default=None, max_length=300, null=True)),
                ('att', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logstat.Attach')),
            ],
        ),
    ]
