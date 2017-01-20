# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCentre', '0009_auto_20170117_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Page Title')),
                ('content', models.TextField(verbose_name='Page Content')),
            ],
        ),
    ]
