# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0018_auto_20170120_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, height_field='height_fieldpx', null=True, upload_to='', verbose_name='Article Featured Image', width_field='width_fieldpx'),
        ),
    ]
