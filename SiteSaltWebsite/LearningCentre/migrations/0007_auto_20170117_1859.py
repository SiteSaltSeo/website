# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0006_auto_20170117_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='video', to='LearningCentre.Videos'),
        ),
    ]
