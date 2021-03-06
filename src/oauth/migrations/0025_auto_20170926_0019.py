# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0024_auto_20170726_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CH', 'Chemistry'), ('MA', 'Mathematics'), ('PHY', 'Physics'), ('HSS', 'Humanities and Social Sciences'), ('BBE', 'Biosciences and Bioengineering'), ('BISS', 'BISS'), ('SS', 'SS')], max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prog',
            field=models.CharField(choices=[('BT', 'B.Tech'), ('MT', 'M.Tech'), ('MSc', 'M.Sc'), ('PhD', 'PhD')], default='BT', max_length=5, verbose_name='programme'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year'), ('5', 'Fifth Year')], default='1', max_length=1),
        ),
    ]
