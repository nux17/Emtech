# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emtech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trash',
            name='remote',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='trash',
            name='route_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trash',
            name='activation_mode',
            field=models.SmallIntegerField(null=True),
        ),
    ]
