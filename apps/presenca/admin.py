from django.contrib import admin
from .models import Convidados

class ConvidadosAdmin(admin.ModelAdmin):
    # Lista os campos que serão exibidos na visualização de lista do admin
    list_display = ('first_name', 'last_name', 'email', 'phone')
    
    # Permite pesquisar por campos específicos
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    
    # Configurações adicionais, como o ordering e o filtro lateral (opcional)
    list_filter = ('first_name',)  # Exemplo de filtro por primeiro nome

# Registra o modelo com as configurações personalizadas
admin.site.register(Convidados, ConvidadosAdmin)
