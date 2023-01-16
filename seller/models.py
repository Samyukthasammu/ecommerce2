from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    product_number = models.BigIntegerField()
    product_image = models.ImageField(upload_to='product/')
    product_price = models.FloatField()
    stock = models.IntegerField()
    
  

