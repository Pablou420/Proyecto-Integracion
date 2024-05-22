from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'App/index.html', {})

def inicio(request):
    return render(request, 'App/inicio.html', {})

def entrantes(request):
    return render(request, 'App/entrantes.html',{})

def platos(request):
    return render(request, 'App/platos.html',{})

def postres(request):
    return render(request, 'App/postres.html', {})

def acompañantes(request):
    return render(request, 'App/acompañantes.html', {})

def carrito(request):
    return render(request, 'App/carrito.html',{})