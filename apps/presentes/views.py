from django.shortcuts import render
from presentes.models import Presentes
from django.contrib import messages
from django.shortcuts import redirect, render

def presentes(request):
    presentes = Presentes.objects.all()
    # Formatar o valor de 'value' com ponto decimal para cada presente
    for presente in presentes:
        presente.value = "{:.2f}".format(presente.value).replace(',', '.')  # Garante ponto ao invés de vírgula
        
    return render(request, 'presentes.html', {"presentes": presentes})