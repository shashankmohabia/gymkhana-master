# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0012_auto_20170702_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='social_media',
            field=models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('LI', 'LinkedIn'), ('GP', 'Google Plus'), ('IG', 'Instagram'), ('GH', 'GitHub'), ('YT', 'YouTube')], max_length=2),
        ),
    ]
