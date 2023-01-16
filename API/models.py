from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length = 100)
    password = models.CharField

    class Meta :
        db_table='student_tb'

