from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ApiUser(AbstractUser):
    ...


class Courier(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    address = models.CharField(max_length=64)


class Mail(models.Model):
    user = models.ForeignKey(ApiUser, blank = False, auto_created=True, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(default="")
