from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('homes')


