from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import Profile
from .models import Post
from .models import City

from .forms import EditProfileForm
from .forms import Post_Form
from .forms import Profile_Form

# Create your views here.

# Home


def home(request):

    return render(request, 'home.html')

# Profile


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = Profile_Form(request.POST)
        if profile_form.is_valid() and request.user.is_authenticated:
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
    else:
        profile_form = Profile_Form()
    user = request.user
    post = Post.objects.filter(user=request.user)
    # profile=Profile.objects.filter(user=request.user)
    context = {'profile_form': profile_form, 'user': user, 'post': post}
    return render(request, 'profile/profile.html', context)


# Normal Post
@login_required
def post(request):
    if request.method == "POST":
        post_form = Post_Form(request.POST)
        if post_form.is_valid and request.user.is_authenticated:
            new_post_form = post_form.save(commit=False)
            new_post_form.user = request.user
            new_post_form.save()
        return redirect('profile')
    else:
        post_form = Post_Form()
    post = Post.objects.all()
    context = {'post_form': post_form, 'post': post}
    return render(request, 'posts/post.html', context)


# Profile Edit & & Update

# @login_required
def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile_form = Profile_Form()
    user = request.user
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = Profile_Form(request.POST, instance=profile)
    if profile_form.is_valid() and user_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('profile')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = Profile_Form(instance=profile)
    context = {'profile': profile,
               'profile_form': profile_form, 'profile_id': profile_id, 'user_form': user_form}
    return render(request, 'profile/edit.html', context)

# change password


# def change_password(request, profile_id):
#     profile = Profile.objects.get(id=profile_id)

#     if request.method == 'POST':
#         form = PasswordChangeForm(
#             data=request.POST, profile=profile, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('change_password')
#         else:
#             return redirect('profile')
#     else:
#         form = PasswordChangeForm(user=request.user)
#     context = {'form': form}
#     return render(request, 'profile/password.html', context)

 # Post Detail or Show Page


@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

# Post Edit


@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form = Post_Form()
    user = request.user
    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect('post_detail', post_id=post_id)
    else:
        post_form = Post_Form(instance=post)
    context = {'post': post,
               'post_form': post_form, 'post_id': post_id}
    return render(request, 'posts/edit.html', context)


# Post Delete
@login_required
def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('profile')


# City


def city(request):
    city = City.objects.all()
    context = {'city': city}
    return render(request, 'city.html', context)


# City Show Page
def detail_city(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid() and request.user.is_authenticated:
            new_post_form = post_form.save(commit=False)
            new_post_form.city = city_id
            new_post_form.user = request.user
            new_post_form.save()
        return redirect('detail', city_id=city_id)
    else:
        post_form = Post_Form()
    # the cities is referring to the fk on post model
    cities = City.objects.all()
    post = Post.objects.filter(cities=city)
    context = {'city': city, 'post_form': post_form,
               'post': post, 'cities': cities}
    return render(request, 'city_detail.html', context)

# Sign Up


pass_err_msg = ''
email_err_msg = ''
username_err_msg = ''


def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        city = request.POST['city']
        signUp_error = False
        if password == password2:

            if User.objects.filter(username=username_form).exists():
                # signUp_error = True
                context = {'username_err_msg': 'Username already exists',
                           'signUp_error': 'signUp_error', 'username_err_msg': 'Username already in use'}
                return render(request, 'home.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    signUp_error = True
                    context = {
                        'email_err_msg': 'Email already linked to account', 'signUp_error': 'signUp_error'}
                    return render(request, 'home.html', context)
                else:

                    signUp_error = False

                    user = User.objects.create_user(

                        username=username_form,
                        email=email_form,
                        password=password,
                        first_name=first_name,
                        last_name=last_name

                    )
                    user.save()

                    profile = Profile.objects.create(
                        name=username_form,
                        city=city,
                        user_id=user.id
                    )
                    profile.save()
                return redirect('home')
        else:
            # signUp_error = True
            context = {'pass_err_msg': 'Passwords Do Not Match',
                       'signUp_error': 'signUp_error', 'pass_err_msg': 'Passwords do not match'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)

# LOGIN


def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        # authenticating user
        user = auth.authenticate(
            username=username_form, password=password_form)
        login_error = False
        if user is not None:
            login_error = False
            # login
            auth.login(request, user)
            # redirect
            return redirect('profile')
        else:
            login_error = True
            print(f"{login_error}")
            context = {'login_err_msg': 'Invalid Credentials',
                       'login_error': 'login_error'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
