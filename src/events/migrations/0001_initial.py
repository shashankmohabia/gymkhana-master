# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0017_auto_20170625_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
                ('published', models.BooleanField(default=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Club')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
                ('published', models.BooleanField(default=True)),
            ],
        ),
    ]
