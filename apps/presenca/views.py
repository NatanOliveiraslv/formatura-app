from django.shortcuts import render
from presenca.models import Convidados
from django.contrib import messages
from django.shortcuts import redirect, render

#Pagina inicial
def index(request):
    return render(request, 'index.html')

def erro404(request):
    return render(request, '404.html')

def presenca(request):
    if request.method == "POST":
        
        first_name = request.POST.get("nome")
        last_name = request.POST.get("sobrenome")
        email = request.POST.get("email")
        phone = request.POST.get("telefone")
        
        lista_convidados = Convidados.objects.all()
        
        # Verifica se já existe um convidado com o mesmo first_name e last_name
        if not lista_convidados.filter(first_name=first_name, last_name=last_name).exists():
               
            convidados = Convidados.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone = phone,
                )
            
            convidados.save()
            
            messages.success(request, 'Presença confirmada!')
            return redirect('presenca')
        
        else:
            messages.error(request, 'Sua presença já está confirmada')
            return redirect('presenca')
        
    else:
        return render(request, 'presenca.html')
    