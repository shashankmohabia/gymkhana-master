# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170630_0020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date'], 'verbose_name_plural': 'news'},
        ),
    ]