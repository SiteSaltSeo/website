# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tools', '0002_auto_20170118_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='short_description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Short description(max length 400 charachters)'),
        ),
    ]