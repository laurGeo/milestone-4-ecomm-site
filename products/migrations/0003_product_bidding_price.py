# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-30 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191029_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bidding_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
