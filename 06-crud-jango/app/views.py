from django.shortcuts import render
from app.forms import CarrosForm

# Importaou o codigo abaixo
#from django.http import HttpResponse

# Criou o arquivo abaixo


def home(request):
    # return HttpResponse('Olá Mundo!')
    # Cria o Retorno abaixo
    return render(request, 'index.html')

# Criando a V


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)
