from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erro404', views.erro404, name='erro404'),
]