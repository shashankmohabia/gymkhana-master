# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170629_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='created_at',
        ),
    ]
