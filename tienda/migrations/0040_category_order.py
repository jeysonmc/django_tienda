# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-23 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0039_auto_20161011_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]