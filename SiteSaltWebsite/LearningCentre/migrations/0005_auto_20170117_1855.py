# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0004_auto_20170117_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_posted',
            field=models.DateField(verbose_name='Posted on date'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_posted',
            field=models.DateField(verbose_name='Posted on date'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='date_posted',
            field=models.DateField(verbose_name='Posted on date'),
        ),
    ]
