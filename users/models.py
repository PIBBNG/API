from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(help_text= "Nome do usuario", max_length=255, blank=True, default="")
    username = models.CharField(help_text='Identificador do usuario', max_length=100, blank=False, unique=True)
    permissions = ArrayField(models.CharField(max_length=255, blank=True), default=list)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','permissions']

    def __str__(self):
        return self.username