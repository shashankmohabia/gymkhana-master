# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20170610_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='owner',
        ),
    ]
