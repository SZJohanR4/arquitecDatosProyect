from django.urls import path
from django.conf import settings
from . import views
app_name = 'producto'

urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('verifCliente', views.verifCliente, name='verifCliente'),
    path('producto/<int:cliente_id>/<int:producto_id>', views.productoDetail, name='productoDetail'),
    path('receta/<int:receta_id>', views.recetaDetail, name='recetaDetail'),
    path('producto/<int:cliente_id>/comprarProducto/<int:producto_id_compra>', views.comprar, name='comprar'),
    path('producto/<int:cliente_id>/crearReceta/<int:receta_id_compra>', views.crearReceta, name='crearReceta'),
]
