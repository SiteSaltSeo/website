# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0003_auto_20170117_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='short_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='simillar',
            field=models.ManyToManyField(blank=True, related_name='_courses_simillar_+', to='LearningCentre.Courses'),
        ),
    ]
