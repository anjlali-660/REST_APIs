from django.db import models

# Create your models here.
class User(models.Model):                                            #This is a User Table
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    company_name=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    email=models.CharField(max_length=50)
    web=models.CharField(max_length=50)
    age=models.IntegerField()
