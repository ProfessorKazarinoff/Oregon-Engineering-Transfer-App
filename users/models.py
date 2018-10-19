# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    university = models.CharField(max_length=30, null="", blank=True)
    job = models.CharField(max_length=30, null="", blank=True)
