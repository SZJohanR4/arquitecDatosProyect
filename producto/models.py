from django.db import models
from franquicias.models import Franquicia
from usuario.models import Clientes


# Create your models here.
class Productos(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Fecha_Compra=models.CharField(max_length=50)
    Fecha_Consumo=models.CharField(max_length=50)
    Observacion=models.CharField(max_length=50)
    Precion_Consumo=models.CharField(max_length=50)
    Fecha_Compra=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Tipos(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Descripcion=models.CharField(max_length=50)
    Fecha_Caducidad=models.CharField(max_length=50)
    Ingredientes=models.CharField(max_length=50)

    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Clientes_Productos(models.Model):
    idClientes=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)

class Productos_Franquicia(models.Model):
    idProductos=models.ForeignKey(Productos, on_delete=models.CASCADE)
    idFranquicia=models.ForeignKey(Franquicias, on_delete=models.CASCADE)
