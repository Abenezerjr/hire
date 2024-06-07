from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Client(models.Model):
    Hiring_Needs = [
        ('oneTime', 'OneTime'),
        ('PartTime', 'PartTime'),
        ('FullTime', 'Fulltime'),
    ]
    fullname=models.CharField(max_length=255)
    email=models.EmailField(max_length=300,unique=True)
    phonenumber=PhoneNumberField(null=False,blank=False,unique=True)
    occupations=models.CharField(max_length=700,null=True,blank=True)
    detailes=models.TextField(null=True,blank=True)
    hiring=models.CharField(max_length=250,choices=Hiring_Needs)

