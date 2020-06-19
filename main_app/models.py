from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
    
from datetime import date

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
  
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    city= models.ForeignKey(City, on_delete=models.CASCADE, relate_name='city')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class City(models.Model):
    city=models.CharField(max_length=200)


    def __str__(self):
        return self.city