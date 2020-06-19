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
        signUp_error = False
        if password ==password2:

            if User.objects.filter(username=username_form).exists():
                # signUp_error = True
                context={'username_err_msg':'Username already exists', 'signUp_error':'signUp_error'}
                return render(request,'home.html',context)
            else:
                if User.objects.filter(email=email_form).exists():
                    signUp_error = True
                    context={'email_err_msg':'Email already exists', 'signUp_error':'signUp_error'}
                    return render(request,'home.html',context)
                else:
                    signUp_error = False
                    user=User.objects.create_user(

                        username=username_form,
                        email=email_form,
                        password=password

                    )
                user.save()
                return redirect('home')
        else:
            # signUp_error = True
            context={'pass_err_msg': 'Passwords Do Not Match', 'signUp_error':'signUp_error'}
            return render(request,'home.html',context)
    else:
        
        return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        username_form=request.POST['username']
        password_form=request.POST['password']
        # authenticating user
        user = auth.authenticate(username=username_form, password=password_form)
        login_error = False
        if user is not None:
            login_error = False
            #login
            auth.login(request, user)
            #redirect
            return redirect('profile')
        else:
            login_error= True
            print(f"{login_error}")

            context = {'login_err_msg': 'Invalid Credentials', 'login_error': 'login_error'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')