from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True, default="")
    notification_token = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username