# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 09:05
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0018_auto_20170710_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(blank=True, upload_to='avatar'),
        ),
    ]
