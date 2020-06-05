from django.shortcuts import render, redirect
from django.core import serializers
from .models import Detec
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def detecdados(request):
    detec = Detec.objects.all()
    dados = {
        'detec' : detec 
    }
    return render(request,'detecdados.html', dados)

def dadosjson(request):
    detec = serializers.serialize('json',Detec.objects.all())
    dados = {
        'detec' : detec 
    }
    return JsonResponse(detec, safe=False)

def oprojeto(request):
    return render(request,'oprojeto.html')

def github(request):
    return redirect("https://github.com/jpmsa27/APImosquito")