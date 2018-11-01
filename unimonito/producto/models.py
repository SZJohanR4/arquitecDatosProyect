from django.db import models
from franquicias.models import Franquicias
from usuario.models import Clientes


# Create your models here.
class Productos(models.Model):
    Nombre=models.CharField(max_length=50)
    Fecha_Compra=models.CharField(max_length=50)
    Fecha_Consumo=models.CharField(max_length=50)
    Observacion=models.CharField(max_length=50)
    Precion_Consumo=models.CharField(max_length=50)
    Fecha_Compra=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Tipos(models.Model):
    Nombre=models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=50)
    Fecha_Caducidad=models.CharField(max_length=50)
    Ingredientes=models.CharField(max_length=50)

    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Recetas(models.Model):
    Nombre=models.CharField(max_length=50)
    ingrediente1=models.CharField(max_length=50)
    cant_ingrediente1=models.CharField(max_length=50)
    ingrediente2=models.CharField(max_length=50)
    cant_ingrediente2=models.CharField(max_length=50)
    ingrediente3=models.CharField(max_length=50)
    cant_ingrediente3=models.CharField(max_length=50)
    preparacion=models.CharField(max_length=50)

    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)
    idClientes=models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Clientes_Productos(models.Model):
    idClientes=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)

class Productos_Franquicia(models.Model):
    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)
    idFranquicia=models.ForeignKey(Franquicias, on_delete=models.CASCADE)
