# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-11-21 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='prod_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
