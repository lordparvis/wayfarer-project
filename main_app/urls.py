
from django.urls import path

from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/', views.profile_edit, name='edit'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('post/', views.post, name='post'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='delete'),
    # path('city/', views.city, name='city'), no longer needed
    path('city/<int:city_id>/', views.detail_city, name='detail'),
    path('profile/<int:post_id>/', views.post_detail, name='post_detail')

]
