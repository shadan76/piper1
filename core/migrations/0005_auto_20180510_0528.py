# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(default='+91123456789078', max_length=15, unique=True),
        ),
    ]