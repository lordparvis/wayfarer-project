from django.forms import ModelForm
from .models import Post, Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class Profile_Form(ModelForm):
    class Meta:
        model=Profile
        fields=['city']


class Post_Form(ModelForm):
    class Meta:
        model=Post
        fields=['title','content','cities']

class EditProfileForm(UserChangeForm):
    class Meta:
      model = User
      fields=('email',
      'first_name',
      'last_name',)