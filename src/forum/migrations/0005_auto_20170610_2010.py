# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20170610_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic'),
        ),
    ]
