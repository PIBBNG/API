from django.db import models
from django.utils import timezone

# Create your models here.
class ClassRegister(models.Model):

    class Meta:
        db_table = 'class_register'

    date = models.DateTimeField(default=timezone.now)
    bible = models.BooleanField(default=False)
    lesson = models.BooleanField(default=False)
    presence = models.BooleanField(default=False)
    reading = models.BooleanField(default=False)
    visitor = models.BooleanField(default=False)
