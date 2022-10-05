from django.shortcuts import render, HttpResponse
from .models import Paslauga, Uzsakymas, Automobilis
# Create your views here.
#
# def index(response):
#     return HttpResponse("Labadiena")

def index(request):
    paslaugu_sk = Paslauga.objects.all().count()

    uzsakymu_sk = Uzsakymas.objects.all().count()
    automobiliu_sk = Automobilis.objects.all().count()

    context ={
        'paslaugu_sk':paslaugu_sk,
        'uzsakymu_sk':uzsakymu_sk,
        'automobiliu_sk':automobiliu_sk,
    }

    return render(request, 'index.html', context=context)
