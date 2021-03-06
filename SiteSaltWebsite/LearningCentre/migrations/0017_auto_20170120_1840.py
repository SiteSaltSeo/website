# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0016_articles_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='published',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1, verbose_name='Course status'),
        ),
        migrations.AddField(
            model_name='videos',
            name='published',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1, verbose_name='Video status'),
        ),
    ]
