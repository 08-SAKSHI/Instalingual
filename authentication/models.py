from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RegisterUser(models.Model):
    new_user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)#choicefield
    phone_number = models.IntegerField()
    mother_tongue = models.CharField(max_length=20,null=False)#choicefield
    DOB = models.DateField()
    occupation = models.CharField(max_length=100)
    Future_goals= models.CharField(max_length=100)
    
    
    
