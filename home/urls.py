from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from home.views import *
from users.views import UserRegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('language/create', LanguageCreateView.as_view(), name='language-create'),
    path('register/', UserRegisterView.as_view(template_name='users/user_form.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]