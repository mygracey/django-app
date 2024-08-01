from django.db import models

# Create your models here.

class SchoolModel(models.Model):
    username=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    
    def __str__(self):
        return self.username
