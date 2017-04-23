# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 21:06
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0037_auto_20161003_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(max_length=30, verbose_name='M\xe9todo de pago'),
        ),
    ]