import django
import username as username
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.timezone import now


class CustomUser(AbstractUser):
    gender_select = (
        ('男', '男'),
        ('女', '女')
    )
    gender = models.CharField(max_length=50, choices=gender_select)

    def __str__(self):
        return str(self.username)


class PostModel(models.Model):
    text = models.CharField(max_length=248)
    created_date = models.DateTimeField(default=django.utils.timezone.now())

    def created(self):
        self.created_date = django.utils.timezone.now()
        self.save()

    def __str__(self):
        return self.text
