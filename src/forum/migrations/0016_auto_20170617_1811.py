# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_topicfavourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='answer',
        ),
        migrations.AddField(
            model_name='tag',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Topic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.UserProfile', verbose_name='author of answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic', verbose_name='topic of answer'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.UserProfile', verbose_name='author of topic'),
        ),
    ]
