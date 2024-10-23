from django.urls import path, include
from . import views

urlpatterns = [
    path('informacoes_pagamento', views.pagamento, name='pagamento'),
    path('realizar_pagamento', views.pagina_pix, name='pagina_pix'),
]