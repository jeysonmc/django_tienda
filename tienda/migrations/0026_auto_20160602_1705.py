# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0025_auto_20160602_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[(b'test', b'TEST')], max_length=30, verbose_name='M\xe9todo de pago'),
        ),
    ]
