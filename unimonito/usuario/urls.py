from django.urls import path, include
from django.conf import settings
from . import views
app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    #path('pedidos', include('producto.urls')),
]
