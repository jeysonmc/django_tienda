# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-14 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20160414_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
    ]
