from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    user_interest_brands=models.CharField(max_length=500,null=True,blank=True)
    user_recommend_brands=models.CharField(max_length=500,null=True,blank=True)
   
