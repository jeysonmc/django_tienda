# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0033_auto_20160702_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(max_length=30, verbose_name='M\xe9todo de pago'),
        ),
    ]
