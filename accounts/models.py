from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField('주소', max_length=150)
    company_address = models.CharField('회사 위치', max_length=150)
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)