from django.contrib import admin
from .models import Pagamentos

class PagamentosAdmin(admin.ModelAdmin):
    # Lista os campos que serão exibidos na visualização de lista do admin
    list_display = ('nome', 'email','value','message','created_at','present_title')
    
    # Permite pesquisar por campos específicos
    search_fields = ('nome', 'email','value','message','created_at','present_title')
    
    # Configurações adicionais, como o ordering e o filtro lateral (opcional)
    list_filter = ('nome',)  # Exemplo de filtro por primeiro nome

# Registra o modelo com as configurações personalizadas
admin.site.register(Pagamentos, PagamentosAdmin)
