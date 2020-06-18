from django.shortcuts import render

from .models import Profile


# Create your views here.

def home(request):
    return render(request,'home.html')

# Profile 

def profile(request):
    profile=Profile.objects.all()
    context={'profile':profile}
    return render(request,'profile/profile.html',context)

