# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-20 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_products', '0010_auto_20200320_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('DRINKS', 'Drinks'), ('SWEETENERS', 'Sweeteners'), ('SNACKS', 'Snacks'), ('SWEETS', 'Sweets'), ('FOOD', 'Food'), ('SUPPLEMENTS', 'Supplements')], max_length=50, null=True),
        ),
    ]