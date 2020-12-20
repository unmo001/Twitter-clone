import django
import username as username
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.timezone import now


class CustomUser(AbstractUser):
    text = models.CharField(max_length=200,unique=False)
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    gender_select = (
        ('男', '男'),
        ('女', '女')
    )
    gender = models.CharField(max_length=50, choices=gender_select)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.username)



class Test_model(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(django.utils.timezone.now())

    def __str__(self):
        return self.name



