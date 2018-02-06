# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 08:55
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0015_auto_20170710_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default='static/assets/others/missing.png', upload_to='avatar'),
        ),
    ]
