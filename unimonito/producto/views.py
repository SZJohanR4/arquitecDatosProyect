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

        cliente=Clientes.objects.get(Cedula=cedulaUsuario)
        if not cliente:#el cliente ya ha comprado antes, debe mostrarse listado de productos que ha consumido, se muestra el formulario para pedir producto
            cliente=Clientes()
            cliente.Nombre=nombre
            cliente.Cedula=cedulaUsuario
            cliente.Ciudad=ciudad
            cliente.save()
        else:#se agrega a la bd y se muestra el formulario para pedir producto
            print("*******************************")
            print(cliente)
            recetasList=Recetas.objects.get(idClientes=cliente)
    productoList=Productos.objects.all()
    if productoList:
        print("hay productos")
    if recetasList:
        print("hay recetas")
    context = {
        'sesion':sesion,
        'productoList': productoList,
        'recetasList':recetasList,
        'getCliente':getClienteFORM
    }
    template = loader.get_template('pedidos.html')
    return HttpResponse(template.render(context, request))
