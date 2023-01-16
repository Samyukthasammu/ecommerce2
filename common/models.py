from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Seller(models.Model):
    seller_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    company_name = models.CharField(max_length = 30)
    acc_holder_name = models.CharField(max_length = 20)
    ifsc = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 30)
    acc_number = models.BigIntegerField()
    seller_pic = models.ImageField(upload_to='seller/')
    user_name = models.CharField(max_length = 20, default = "")
    password = models.CharField(max_length= 20,  default = "")