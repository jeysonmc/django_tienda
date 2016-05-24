# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_auto_20160523_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_from',
            field=models.CharField(default='Principal', max_length=50, verbose_name='Or\xedgen'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='tienda.Order'),
        ),
    ]
