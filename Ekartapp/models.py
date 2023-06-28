from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userregister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=255)
    role=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    confirmpassword=models.CharField(max_length=255)

    def __str__(self):
        return self.firstname

class Products(models.Model):
    productname=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=255)
    productimage=models.ImageField(null=True,blank=True,upload_to="images/")
  
    def __str__(self):
        return self.productname

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()