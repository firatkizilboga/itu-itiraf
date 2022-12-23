from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    instagram = models.CharField(max_length=100, blank=False, null=False, unique=True)