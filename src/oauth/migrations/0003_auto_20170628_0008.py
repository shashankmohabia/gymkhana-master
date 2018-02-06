# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20170612_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='cover'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(default='', help_text='Enter your skills, separated by comma.', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
