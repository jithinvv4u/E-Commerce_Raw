from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserData(AbstractUser):
    super_user=models.BooleanField()
    phone=models.IntegerField()