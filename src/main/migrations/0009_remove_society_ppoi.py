# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170622_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='society',
            name='ppoi',
        ),
    ]
