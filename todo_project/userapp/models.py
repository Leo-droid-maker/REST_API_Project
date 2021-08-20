from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        verbose_name='логин', max_length=64, unique=True)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    email = models.EmailField(verbose_name='имейл', unique=True)
