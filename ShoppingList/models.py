from django.db import models
from datetime import datetime

class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField()