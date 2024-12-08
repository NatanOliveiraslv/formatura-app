from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render


#Pagina inicial
def index(request):
    return render(request, 'index.html')

def erro404(request):
    return render(request, '404.html')

def local(request):
    return render(request, 'local.html')