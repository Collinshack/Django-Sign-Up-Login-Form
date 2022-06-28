from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewUsers(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)
    password2 = models.CharField(max_length=40)

class meta:
    models = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']