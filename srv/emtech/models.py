from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    address = models.CharField(max_length=128, null=False)
    name = models.CharField(max_length=128, null=False)
    postal_code = models.CharField(max_length=5, null=False)
    picked_up_times = models.IntegerField(default=0, null=False)


class Trash(models.Model):
    user = models.ForeignKey('Users', null=True)
    activated = models.BooleanField(default=False, null=False)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    activated_at = models.DateTimeField(null=True)
    remote = models.CharField(null=True, max_length=32)
    route_id = models.IntegerField(default=0)
