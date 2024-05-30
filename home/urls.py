from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('language/create', LanguageCreateView.as_view(), name='language-create'),
    ]