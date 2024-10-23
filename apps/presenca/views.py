from django.shortcuts import render
from presenca.models import Convidados
from django.contrib import messages
from django.shortcuts import redirect, render

#Pagina inicial
def index(request):
    return render(request, 'index.html')

def presenca(request):
    if request.method == "POST":
        print(request.POST.get("nome"))          
        convidados = Convidados.objects.create(
            first_name = request.POST.get("nome"),
            last_name = request.POST.get("sobrenome"),
            email = request.POST.get("email"),
            phone = request.POST.get("telefone"),
            )
        
        convidados.save()
        
        messages.success(request, 'Presença confirmada!')
        return redirect('presenca')
    else:
        return render(request, 'presenca.html')