from django.urls import path, include
from . import views

urlpatterns = [
    path('informacoes_pagamento', views.pagamento, name='pagamento'),
    path('processando_pagamento', views.processando_pagamento, name='processando_pagamento'),
    path('realizar_pagamento/<int:pagamento_id>', views.pagina_pix, name='pagina_pix'),
]