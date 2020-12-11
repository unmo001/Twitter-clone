from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    gender_select = (
        ('男', '男'),
        ('女', '女')
    )
    gender = models.CharField(max_length=2, choices=gender_select)

    def __str__(self):
        return str(self.gender)
