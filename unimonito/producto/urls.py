from django.urls import path
from django.conf import settings
from . import views
app_name = 'producto'

urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('verifCliente', views.verifCliente, name='verifCliente'),
]
