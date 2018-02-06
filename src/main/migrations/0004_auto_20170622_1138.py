# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170622_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='year',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='society',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='society',
            name='year',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
