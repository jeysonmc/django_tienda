# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0022_auto_20160601_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Impuesto'),
        ),
    ]
