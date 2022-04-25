from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    project = models.CharField(max_length=64)
    is_staff = models.BooleanField(default=False)
    text = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField()
    user = models.CharField(max_lenght=64)
    active = models.BoleanField
    
    def __str__(self):
        return self.email
