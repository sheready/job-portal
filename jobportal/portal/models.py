from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(models.Model):
   
    employeename = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length = 200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employeename

class Hr(models.Model): 
    
    companyname = models.CharField(max_length = 200,null=True)
    STATUS = (
        ('Job allocated','Job allocated'),
        ('Job pending','Job pending'),
        ('Job not allocated','Job not allocated'),
    )
    employee = models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,default ='Job not allocated' ,choices = STATUS)
   
    

    def __str__(self):
        return self.companyname


class Jobs(models.Model):

    jobpost = models.CharField(max_length=200,null=True)
    jobinstruction = models.CharField(max_length = 200,null=True)
    jobsample = models.CharField(max_length = 200,null=True)
    location = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    companyname = models.ForeignKey(Hr,null=True,on_delete=models.SET_NULL)
   
   

    def __str__(self):
        return self.jobpost



