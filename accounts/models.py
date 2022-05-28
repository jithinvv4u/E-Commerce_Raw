from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#created user model by extending default django User using AbstractUser
class UserData(AbstractUser):
    super_user=models.BooleanField()
    phone=models.IntegerField()