from django.urls import path
from django.conf import settings
from . import views
app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
]
