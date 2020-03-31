# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_products', '0002_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionvalue',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='all_products.Product'),
        ),
    ]
