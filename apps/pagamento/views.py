from django.shortcuts import render
from pagamento.models import Pagamentos
from presentes.models import Presentes
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, render
from pagamento.payload_pix import Payload
from django.utils import timezone
import os
from django.conf import settings
import shutil
from decouple import config

def limpar_pasta_qrcode():
    # Verifica se a pasta existe
    pasta = os.path.join("media", "QRcode")
    
    if os.path.exists(pasta):
        # Exclui todos os arquivos dentro da pasta
        for filename in os.listdir(pasta):
            file_path = os.path.join(pasta, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Exclui o arquivo
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Exclui o diretório
            except Exception as e:
                print(f"Erro ao excluir {file_path}: {e}")

def pagamento(request):
    if request.method == "POST":    
        presente_id = request.POST.get('presente_id')
        total = request.POST.get('total')
        
        presente = get_object_or_404(Presentes, id=presente_id)

        return render(request, "pagamento.html", {'presente': presente,
                                                  'valor_total': total})
    else:
        return redirect("presentes")
    
def processando_pagamento(request):
    if request.method == "POST":
        
        nome = config("NOME")
        chavepix = config("CHAVE_PIX")
        valor = request.POST.get("valor-total")
        cidade = config("CIDADE")
        txtId = "Formatura Rian"
        
        #limpar_pasta_qrcode()
        
        pasta_qrcode = os.path.join(settings.MEDIA_ROOT, "qrcode_pix")
        
         # Certifique-se de que a pasta existe
        if not os.path.exists(pasta_qrcode):
            os.makedirs(pasta_qrcode)
                
        pagamento = Pagamentos.objects.create(
            status = "PENDENTE",
            nome = request.POST.get("presenteadores"),
            email = request.POST.get("email"),
            value = request.POST.get("valor-total"),
            message = request.POST.get("mensagem"),
            present_title = request.POST.get("titulo-presente"),
            )
        
        pagamento.save()
        
        fileNameQrcode = f"{pagamento.id}.png"
        
        # Certifique-se de que a pasta existe
        
        pagamento.qr_code = os.path.join("pagamentos\\qrcode_pix", fileNameQrcode)
        pagamento.save()
        
        pix = Payload(nome, chavepix, valor, cidade, txtId, fileNameQrcode)
        pagamento.code_pix = pix
        pagamento.save()
        
        return redirect('pagina_pix',pagamento.id)
        
    else:
        return redirect('presenca')

def pagina_pix(request, pagamento_id):
    pagamento = get_object_or_404(Pagamentos, pk=pagamento_id)
    return render(request, "pagina_pix.html", {"pagamento": pagamento})