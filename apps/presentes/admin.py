from django.contrib import admin
from .models import Presentes

class PresentesAdmin(admin.ModelAdmin):
    # Lista os campos que serão exibidos na visualização de lista do admin
    list_display = ('title', 'value')
    
    # Permite pesquisar por campos específicos
    search_fields = ('title',)
    
    # Configurações adicionais, como o ordering e o filtro lateral (opcional)
    list_filter = ('title',)  # Exemplo de filtro por primeiro nome

# Registra o modelo com as configurações personalizadas
admin.site.register(Presentes, PresentesAdmin)
