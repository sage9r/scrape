from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView

from .models import Data
from .tasks import mock_action

import requests

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"


class DataCreateView(CreateView):
    model = Data
    fields = '__all__'
    success_url = reverse_lazy('homes')

    def form_valid(self, form):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

        headers = {
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "d7bd448827msh543438a1ff3d923p1eaa2cjsna2d4e269a2ce",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        print(99999999999999999999999999999)
        jsonObject = response.json()
        for itm in jsonObject["data"]["languages"][:10]:
            print(8888888,itm)
            lang = Data()
            lang.name = itm["language"]
            lang.save()
        return super().form_valid(form)


def with_celery(request):
    res = mock_action.delay()
    return render(request, 'general/home.html')


