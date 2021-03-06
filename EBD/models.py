from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from users.models import CustomUser


# class EBDUser(CustomUser):
class EBDUser(models.Model):

    class Meta:
        db_table = 'ebd_user'

    nickname = models.CharField(max_length=25, unique=True)
    name = models.CharField(null=False, max_length=50, default="--")
    ebd_class = models.ForeignKey("EBDClass", null=False, on_delete=models.CASCADE, related_name='ebd_class')
    teacher = models.BooleanField(default=False)

class EBDClass(models.Model):

    class Meta:
        db_table = 'ebd_class'

    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)


class ClassRegister(models.Model):

    class Meta:
        db_table = 'class_register'

    date = models.DateTimeField(default=timezone.now)
    bible = models.BooleanField(default=False)
    lesson = models.BooleanField(default=False)
    presence = models.BooleanField(default=False)
    reading = models.BooleanField(default=False)
    cult =  models.BooleanField(default=False)
    visitor = models.BooleanField(default=False)
    student = models.ForeignKey("EBDUser", null=True, on_delete=models.CASCADE, related_name='class_register')


class EBD(models.Model):

    class Meta:
        db_table = 'ebd'

    date = models.DateTimeField(default=timezone.now)
    lesson_class = models.ForeignKey("EBDClass", null=True, on_delete=models.CASCADE, related_name='lesson_class')
    lesson_theme = models.CharField(help_text= "Tema da EBD", max_length=255, blank=True, default="")
