from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Client(models.Model):
    fullname=models.CharField(max_length=255)
    email=models.EmailField(max_length=300,unique=True)
    phonenumber=PhoneNumberField(null=False,blank=False,unique=True)


    def __str__(self):
        return self.fullname



class OCCUPATIONS(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE , null=True)
    occupations = models.CharField(max_length=700, null=True, blank=True)
    detailes = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.occupations


class HireNeed(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    Hiring_Needs = [
        ('oneTime', 'OneTime'),
        ('PartTime', 'PartTime'),
        ('FullTime', 'Fulltime'),
    ]
    Experience=[
        ('Experience(0-2)years','Experience(0-2)years'),
        ('Experience(2-5)years','Experience(0-2)years'),
        ('Experience(more than 5)years','Experience(0-2)years'),
    ]
    hiring=models.CharField(max_length=250,choices=Hiring_Needs)
    Experience=models.CharField(max_length=250,choices=Experience)

    web_link=models.URLField(max_length=300,null=True,blank=True)


    def __str__(self):
        return f"{self.client.fullname} - {self.hiring}"