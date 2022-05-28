from django.db import models
# from django.contrib.auth.models import User
from accounts.models import UserData
# Create your models here.

#item model with fields
class Item(models.Model):
    name=models.CharField(max_length=45)
    description=models.CharField(max_length=45)
    rate=models.IntegerField()
    Currency=models.CharField(max_length=45)
    category=models.CharField(max_length=45)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name

'''cart model with foreign key connected to model Item and
    UserData of accounts model'''
class Cart(models.Model):
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)


