# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emtech', '0002_auto_20151214_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trash',
            name='activation_mode',
        ),
    ]
