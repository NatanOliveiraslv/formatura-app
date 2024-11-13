from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('presenca.urls')),
    path('', include('presentes.urls')),
    path('', include('pagamento.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#handler404 = "presenca.views.handler404"