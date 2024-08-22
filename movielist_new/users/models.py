from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from movielist import settings


class User(AbstractUser):
    photo=models.ImageField(upload_to='users/%Y/%m/%d/',blank=True,null=True,verbose_name='Фото',default=settings.DEFAULT_USER_IMAGE)
    date_of_birth=models.DateTimeField(blank=True,null=True,verbose_name='Дата рождения')