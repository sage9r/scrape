from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Language

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = "/login/"
    redirect_field_name = "homes"

class LanguageCreateView(CreateView):
    model = Language
    fields = '__all__'
    success_url = reverse_lazy('homes')