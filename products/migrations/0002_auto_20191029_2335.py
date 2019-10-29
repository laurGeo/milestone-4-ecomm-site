# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-29 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='event1',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='event2',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='event3',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=254),
        ),
    ]
