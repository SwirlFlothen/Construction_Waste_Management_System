from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class users(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    user_name= models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)


    def __str__(self):
        return self.user_name
