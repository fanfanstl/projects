# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-06 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20181004_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='a_username',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='orderaddress',
            name='o_username',
            field=models.CharField(default='', max_length=32),
        ),
    ]
