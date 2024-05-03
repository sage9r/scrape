from django.contrib import admin
from django.urls import path
from home.views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('data/', DataCreateView.as_view(), name='datas'),
    path('with_celery', views.with_celery, name='with_celery'),

]