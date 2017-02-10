# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_auto_20170120_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='google_handle',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, unique=True, verbose_name='Google +'),
        ),
        migrations.AddField(
            model_name='settings',
            name='youtube_handle',
            field=models.CharField(blank=True, default=None, max_length=300, null=True, unique=True, verbose_name='Youtube channel'),
        ),
    ]
