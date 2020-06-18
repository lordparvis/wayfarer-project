from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile



# Create your views here.

def home(request):
    return render(request,'home.html')

# Profile 
@login_required
def profile(request):
    profile=Profile.objects.all()
    context={'profile':profile}
    # return render(request,'profile/profile.html',context)

# Sign Up

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            # return redirect('home')
    else:
        error_message='Invalid Sign Up'
    form=UserCreationForm()
    context={'form':form}
    return render(request,'home.html',context)