# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170705_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
    ]
