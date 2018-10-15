from django.db import models
from franquicias.models import Franquicia

class Franquicias(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Director=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Localidades(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Direccion=models.CharField(max_length=50)

    idFranquicia=models.ForeignKey(Franquicias, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre
