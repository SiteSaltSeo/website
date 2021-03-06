# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0017_auto_20170120_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='articles',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courses',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courses',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videos',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videos',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', verbose_name='Article Featured Image', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', verbose_name='Course Featured Image', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', verbose_name='Video Featured Image', width_field='width_field'),
        ),
    ]
