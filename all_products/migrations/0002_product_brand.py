# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-18 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=254),
        ),
    ]
