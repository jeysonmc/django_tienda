# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0023_productorder_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-status', '-pk'], 'verbose_name': '\xd3rden', 'verbose_name_plural': '\xd3rdenes'},
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Address', verbose_name='Direcci\xf3n de env\xedo'),
        ),
    ]
