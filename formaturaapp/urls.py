from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('presenca/', include('presenca.urls')),
    path('presentes/', include('presentes.urls')),
    path('pagamento/', include('pagamento.urls')),
    path('', include('paginas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#handler404 = "presenca.views.handler404"