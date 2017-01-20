# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0005_auto_20170117_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='read_time',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_time',
            field=models.CharField(default=None, max_length=10, unique=True, verbose_name='Course duration'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='short_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
