from django.db import models

# Create your models here.

class register(models.Model):
    FIRSTNAME = models.CharField(max_length=20)
    LASTNAME = models.CharField(max_length=20)
    USERNAME = models.CharField(max_length=20)
    PASSWORD = models.CharField(max_length=20)
    GENDER = models.CharField(max_length=20)
    MAIL = models.CharField(max_length=20,default='mail')
    DESIGNATION = models.CharField(max_length=30,default='designation')
    PICTURE = models.FileField(default='PICTURE')
    Status = models.BooleanField(default=False)