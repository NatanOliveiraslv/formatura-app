from django.shortcuts import render
from presentes.models import Presentes
from django.contrib import messages
from django.shortcuts import redirect, render

def presentes(request):
    ordenacao = request.GET.get('ordem')  # Padrão: A-Z pelo nome
    
    # Define a ordenação com base no parâmetro
    if ordenacao == 'valor_asc':
        presentes = Presentes.objects.order_by('value')  # Menor para maior
    elif ordenacao == 'valor_desc':
        presentes = Presentes.objects.order_by('-value')  # Maior para menor
    elif ordenacao == 'nome_asc':
        presentes = Presentes.objects.order_by('title')  # A-z
    elif ordenacao == 'nome_desc':
        presentes = Presentes.objects.order_by('-title')  # Z-A
    else: 
        presentes = Presentes.objects.all()
        
    # Formatar o valor de 'value' com ponto decimal para cada presente
    for presente in presentes:
        presente.value = "{:.2f}".format(presente.value).replace(',', '.')  # Garante ponto ao invés de vírgula
        
    return render(request, 'presentes.html', {"presentes": presentes})
