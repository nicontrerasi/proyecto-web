from django.db import models

class User(models.Model):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=100)
    pwd = models.CharField(max_length=20)
