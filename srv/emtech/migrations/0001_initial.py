# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=False)),
                ('activation_mode', models.SmallIntegerField()),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('activated_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=5)),
                ('picked_up_times', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='trash',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emtech.Users'),
        ),
    ]
