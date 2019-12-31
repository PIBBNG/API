from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from users.models import CustomUser


class EBDUser(CustomUser):
    
    class Meta:
        db_table = 'ebd_user'

    ebd_class = models.ForeignKey("EBDClass", null=False, on_delete=models.CASCADE, related_name='ebd_class')


class EBDClass(models.Model):

    class Meta:
        db_table = 'ebd_class'

    name = models.CharField(max_length=100, null=False, blank=False, unique=True)


class ClassRegister(models.Model):

    class Meta:
        db_table = 'class_register'

    date = models.DateTimeField(default=timezone.now)
    bible = models.BooleanField(default=False)
    lesson = models.BooleanField(default=False)
    presence = models.BooleanField(default=False)
    reading = models.BooleanField(default=False)
    visitor = models.BooleanField(default=False)
    student = models.ForeignKey("EBDUser", null=True, on_delete=models.CASCADE, related_name='class_register')
