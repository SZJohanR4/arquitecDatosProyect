from django.contrib import admin
from .models import Productos, Tipos, Facturas, Productos_Franquicia, Recetas

admin.site.register(Productos)
admin.site.register(Tipos)
admin.site.register(Productos_Franquicia)
admin.site.register(Recetas)
admin.site.register(Facturas)
