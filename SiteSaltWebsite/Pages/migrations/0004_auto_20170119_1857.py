# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_auto_20170119_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Page Featured Image'),
        ),
        migrations.AddField(
            model_name='page',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Youtube Video id'),
        ),
    ]
