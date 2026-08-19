from django.shortcuts import render

def index(request):
    return render(request, 'soporte/index.html')
from .models import Tecnico

def lista_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'soporte/tecnicos.html', {'tecnicos': tecnicos})