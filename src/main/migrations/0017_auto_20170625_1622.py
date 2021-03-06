# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20170612_1258'),
        ('main', '0016_auto_20170625_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='mentor',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='cmentor', to='oauth.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='gallery',
            field=models.ForeignKey(blank=True, help_text='Select a gallery to link to this club.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Gallery'),
        ),
        migrations.AlterField(
            model_name='society',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smentor', to='oauth.UserProfile'),
        ),
    ]
