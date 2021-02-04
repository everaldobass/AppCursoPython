from django.shortcuts import redirect, render
from app.forms import CarrosForm
from app.models import Carros

# Importaou o codigo abaixo
#from django.http import HttpResponse

# Criou o arquivo abaixo


def home(request):
    # return HttpResponse('Olá Mundo!')
    # Cria o Retorno abaixo
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

# Criando a V


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request):
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)
