# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0005_auto_20180423_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='word',
            name='published_date',
        ),
    ]