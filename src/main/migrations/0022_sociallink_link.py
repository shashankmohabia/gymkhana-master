# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170625_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='link',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
    ]
