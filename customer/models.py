from django.db import models
from common.models import Customer
from seller.models import Product

class Cart(models.Model) :
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)


