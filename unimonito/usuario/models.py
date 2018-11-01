from django.db import models
from django.contrib.auth.models import User
from franquicias.models import Franquicias


class Empleados(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Cedula=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=50)
    Fecha_contrato=models.CharField(max_length=50)
    Salario=models.CharField(max_length=50)
    Empleado=models.CharField(max_length=50)

    idFranquicia=models.ForeignKey(Franquicias, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

class Clientes(models.Model):
    Nombre=models.CharField(max_length=50)
    Cedula=models.CharField(max_length=50)
    Ciudad=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre
