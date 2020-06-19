from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile



# Create your views here.

def home(request):
    return render(request,'home.html')

# Profile 

def profile(request):
    profile=Profile.objects.all()
    context={'profile':profile}
    return render(request,'profile/profile.html',context)

# Sign Up

# def signup(request):
#     if request.method == 'POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             return redirect('home')
#     else:
#         error_message='Invalid Sign Up'
#     form=UserCreationForm()
#     context={'form':form}
#     return render(request,'registration/signup.html',context)

def signup(request):
    if request.method=='POST':
        username_form=request.POST['username']
        email_form=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password ==password2:

            if User.objects.filter(username=username_form).exists():
                context={'error':'User already exist'}
                return render(request,'home.html',context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context={'error':'Email already exist'}
                    return render(request,'home.html',context)
                else:
                    user=User.objects.create_user(

                        username=username_form,
                        email=email_form,
                        password=password

                    )
                user.save()
                return redirect('home')
        else:
            context={'error': 'Password Invalid'}
            return render(request,'home.html',context)
    else:
        
        return render(request,'home.html')




def login(request):
    if request.method == 'POST':
        username_form=request.POST['username']
        password_form=request.POST['password']
        user = auth.authenticate(username=username_form, password=password_form)