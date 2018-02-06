# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20170625_1315'),
        ('main', '0030_auto_20170705_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='gallery',
            field=models.ForeignKey(blank=True, help_text='Select a carousel gallery to link to this society.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Gallery'),
        ),
    ]
