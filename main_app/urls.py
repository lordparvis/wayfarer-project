
from django.urls import path

from .import views


urlpatterns=[
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('accounts/signup/',views.signup,name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('post/',views.post, name='post'),
    path('city/',views.city, name='city'),
    path('city/<int:city_id>/',views.detail_city,name='detail')

]