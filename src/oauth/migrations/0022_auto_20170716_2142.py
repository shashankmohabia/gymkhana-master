# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0021_auto_20170716_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(blank=True, default=None, help_text='Enter your skills, separated by comma.', max_length=1024, null=True),
        ),
    ]
