from django.shortcuts import render
from .forms import getClienteFORM
from django.contrib.auth.decorators import login_required

from usuario.models import Clientes, Empleados


def pedidos(request):
    sesion=request.user
    return render(request,'pedidos.html',{"getCliente":getClienteFORM,"username":sesion})


def verifCliente(request):
    sesion=request.user
    clienteForm=getCliente(request.POST or None)
    if clienteForm.is_valid():
        datos=clienteForm.cleaned_data
        nombre=datos.get("nombre_Usuario")
        cedulaUsuario=datos.get("cedula_Usuario")
        ciudad=datos.get("ciudad_Usuario")

        cliente=Clientes.objects.filter(Cedula=cedulaUsuario)
        if cliente != None:#el cliente ya ha comprado antes, debe mostrarse listado de productos que ha consumido, se muestra el formulario para pedir producto
            try:
                listProducts=Productos.objects.all()
                recetas=Recetas.objects.filter(cliente=cedulaUsuario)
            except KeyError:
                datosUser=KeyError
                print(datosUser)
        else:##se agrega a la bd y se muestra el formulario para pedir producto
            try:
                cliente=Clientes()
                cliente.Nombre=nombre
                cliente.Cedula=cedulaUsuario
                cliente.Ciudad=ciudad
                cliente.save()
                listProducts=Productos.objects.all()
            except KeyError:
                datosUser=KeyError
                print(datosUser)
            return render(request,'pedidos.html',{"listProducts":listProducts,"addProductFORM":addProductFORM,"username":sesion})
