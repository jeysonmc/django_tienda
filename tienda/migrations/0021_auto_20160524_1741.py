# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_auto_20160524_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[(b'contraentrega_efectivo', b'Contra entrega efectivo'), (b'contraentrega_tarjeta', b'Contra entrega tarjeta')], max_length=30, verbose_name='M\xe9todo de pago'),
        ),
    ]
