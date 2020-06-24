from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import date

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    # be more specific with date properties i.e. date_joined
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profil_img", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.user}"

    # you can create custom methods with your models
    # in your template you can just use {{ profile.get_fullname }}
    def get_fullname(self):
        return f"{self.user.firstname} {self.user.lastname}"

    # {{ profile.get_posts }}
    def get_posts(self):
        return self.user.posts_set.all()


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
    # with a foreign key it should be singular
    cities = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user} on {self.created_date}"

    class Meta:
        ordering = ['-created_date']
