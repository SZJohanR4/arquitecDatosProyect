from django.shortcuts import render
from .forms import getClienteFORM
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from usuario.models import Clientes, Empleados
from .models import Recetas, Productos


def pedidos(request):
    sesion=request.user
    return render(request,'pedidos.html',{"getCliente":getClienteFORM,"username":sesion})


def verifCliente(request):
    sesion=request.user
    recetasList=Recetas.objects.all()
    clienteForm=getClienteFORM(request.POST or None)
    if clienteForm.is_valid():
        datos=clienteForm.cleaned_data
        nombre=datos.get("nombre_Usuario")
        cedulaUsuario=datos.get("cedula_Usuario")
        ciudad=datos.get("ciudad_Usuario")

        cliente=Clientes.objects.filter(Cedula=cedulaUsuario)
        if not cliente:#el cliente ya ha comprado antes, debe mostrarse listado de productos que ha consumido, se muestra el formulario para pedir producto
            cliente=Clientes()
            cliente.Nombre=nombre
            cliente.Cedula=cedulaUsuario
            cliente.Ciudad=ciudad
            cliente.save()
        else:#se agrega a la bd y se muestra el formulario para pedir producto
            cliente=Clientes.objects.get(Cedula=cedulaUsuario)
            print(cliente)
            recetasList=Recetas.objects.filter(idClientes=cliente)
    productoList=Productos.objects.all()
    context = {
        'sesion':sesion,
        'productoList': productoList,
        'recetasList':recetasList,
        'getCliente':getClienteFORM
    }
    return render(request,'pedidos.html',{"getCliente":getClienteFORM,"username":sesion,"productoList":productoList,"recetasList":recetasList})


def productoDetail(request, producto_id):
    sesion=request.user
    producto = Productos.objects.get(pk=producto_id)
    return render(request,'productoDetail.html',{"getCliente":getClienteFORM,"username":sesion,"producto":producto})

def recetaDetail(request, receta_id):
    sesion=request.user
    receta = Recetas.objects.get(pk=receta_id)
    return render(request,'recetaDetail.html',{"getCliente":getClienteFORM,"username":sesion,"receta":receta})
