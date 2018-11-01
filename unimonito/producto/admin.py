from django.contrib import admin
from .models import Productos, Tipos, Clientes_Productos, Productos_Franquicia, Recetas

admin.site.register(Productos)
admin.site.register(Tipos)
admin.site.register(Clientes_Productos)
admin.site.register(Productos_Franquicia)
admin.site.register(Recetas)
