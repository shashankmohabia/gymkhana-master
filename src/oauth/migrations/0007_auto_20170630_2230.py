# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 17:00
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0006_auto_20170630_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(upload_to='avatar'),
        ),
    ]
