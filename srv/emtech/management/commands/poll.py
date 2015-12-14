__author__ = 'nux'

from django.core.management.base import BaseCommand, CommandError
from emtech.models import Trash
import requests

HOST = "hackathon.villatolosa.com"
SERVICE = "smartcity"
PATH = "/team2"
TOKEN = "09XXYXANSMAHZLVCPZVJ"
DEVICE = "myEdison"

class Command(BaseCommand):
    help = 'Polls trashes'
'''
    def handle(self, *args, **options):
        for trash in Trash.objects.all()
                '''