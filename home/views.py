from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Language

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class LanguageCreateView(CreateView):
    model = Language
    fields = '__all__'
    success_url = reverse_lazy('homes')