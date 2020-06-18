from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html')

# Profile 

def profile(request):
    return render(request,'profile/profile.html')

