from django.shortcuts import render
from pagamento.models import Pagamentos
from presentes.models import Presentes
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, render
from pagamento.payload_pix import Payload
from django.utils import timezone
import os
import shutil

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
    
def pagina_pix(request):
    
    nome = "Natan Oliveira da Silva"
    chavepix = "60037382004"
    valor = '1.00'
    cidade = "Porto Alegre"
    txtId = "Pix para teste"
    fileNameQrcode = "teste"
    
    limpar_pasta_qrcode()
    
    pix = Payload(nome, chavepix, valor, cidade, txtId, fileNameQrcode)
    return render(request, 'pagina_pix.html', {"pix": pix,
                                               "fileNameQrcode": fileNameQrcode})
    