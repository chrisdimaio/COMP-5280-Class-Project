# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_auto_20180423_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
