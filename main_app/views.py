from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile



# Create your views here.

def home(request):
    return render(request,'home.html')

# Profile 
@login_required
def profile(request):
    if request.user.is_authenticated:
        user=User.objects.all()
        profile=Profile.objects.all()
        context={'profile':profile,'user':user}
        return render(request,'profile/profile.html',context)
    else:
        return redirect('home')

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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
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
                        password=password,
                        first_name=first_name, 
                        last_name=last_name
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
        # authenticating user
        user = auth.authenticate(username=username_form, password=password_form)
        if user is not None:
            #login
            auth.login(request, user)
            #redirect
            return redirect('profile')
        else:
            context = {'error': 'Invalid Credentials'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'registration/login.html')

