from django.db import models


class Franquicias(models.Model):
    Nombre=models.CharField(max_length=50)
    Director=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Localidades(models.Model):
    Nombre=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=50)

    idFranquicia=models.ForeignKey(Franquicias, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre
