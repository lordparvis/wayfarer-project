from django.db import models

from datetime import date

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
  
    def __str__(self):
        return self.name
