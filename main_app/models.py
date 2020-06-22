from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import date

# Create your models here.


class Profile(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profil_img", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100, blank=True)
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="profil_img", blank=True)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
>>>>>>> submaster

    def __str__(self):
        return f"{self.name} {self.user}"


class City(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cities = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user} on {self.created_date}"

    class Meta:
        ordering = ['-created_date']
