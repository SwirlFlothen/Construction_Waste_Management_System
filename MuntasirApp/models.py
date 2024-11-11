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




class project(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE,blank=True,null=True)
    project_name = models.CharField(max_length=200)
    duration = models.DateField(auto_now_add=True,auto_now=False)
    estimated_waste = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.project_name



class WasteReport(models.Model):
        report_id = models.IntegerField(blank=True, null=True)
        project_id = models.ForeignKey(project, on_delete=models.CASCADE, blank=True, null=True)
        waste_generated = models.FloatField(blank=True, null=True)
        waste_recycled = models.FloatField(blank=True, null=True)
        waste_disposed = models.FloatField(blank=True, null=True)
        environmental_impact = models.CharField(max_length=200)

        def __str__(self):
            return str(self.report_id)



