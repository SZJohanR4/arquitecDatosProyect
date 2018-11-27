from django.shortcuts import render
from .forms import getClienteFORM, getProductoFORM, nuevaRecetaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from usuario.models import Clientes, Empleados
from .models import Recetas, Productos, Facturas
import datetime


def pedidos(request):
    sesion=request.user
    return render(request,'pedidos.html',{"getCliente":getClienteFORM,"username":sesion})


def verifCliente(request):
    sesion=request.user
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
    cliente=Clientes.objects.get(Cedula=cedulaUsuario)
    recetasList=Recetas.objects.filter(idClientes=cliente)
    productoList=Productos.objects.all()
    context = {
        'sesion':sesion,
        'productoList': productoList,
        'recetasList':recetasList,
        'getCliente':getClienteFORM
    }
    return render(request,'pedidos.html',{"getCliente":getClienteFORM,"username":sesion,"productoList":productoList,"recetasList":recetasList,"cliente":cliente})


def productoDetail(request, cliente_id,producto_id):
    sesion=request.user
    producto = Productos.objects.get(pk=producto_id)
    cliente=Clientes.objects.get(pk=cliente_id)
    form = getProductoFORM(initial={'nombre_Producto': producto.Nombre,'fecha_Consumo': producto.Fecha_Consumo,'observacion': producto.Observacion,'precio': producto.Precion_Consumo,})
    return render(request,'productoDetail.html',{"getCliente":getClienteFORM,"username":sesion,"producto":producto,"getProductoFORM":form,"cliente":cliente,"nuevaRecetaForm":nuevaRecetaForm})

def recetaDetail(request, receta_id):
    sesion=request.user
    receta = Recetas.objects.get(pk=receta_id)
    return render(request,'recetaDetail.html',{"getCliente":getClienteFORM,"username":sesion,"receta":receta})

def comprar(request, cliente_id, producto_id_compra):
    sesion=request.user
    now = datetime.datetime.now()
    producto = Productos.objects.get(pk=producto_id_compra)
    cliente=Clientes.objects.get(pk=cliente_id)
    factura=Facturas()
    factura.Fecha_Factura=now
    factura.idClientes=cliente
    factura.idProductos=producto
    factura.save()
    return render(request,'home.html',{"factura":factura,"username":sesion,"producto":producto})


def crearReceta(request, cliente_id, receta_id_compra):
    sesion=request.user
    now = datetime.datetime.now()
    producto = Productos.objects.get(pk=receta_id_compra)
    cliente=Clientes.objects.get(pk=cliente_id)
    factura=Facturas()
    factura.Fecha_Factura=now
    factura.idClientes=cliente
    factura.idProductos=producto
    factura.save()
    recetaNewForm=nuevaRecetaForm(request.POST or None)
    print(recetaNewForm.is_valid())
    if recetaNewForm.is_valid():
        datos=recetaNewForm.cleaned_data
        receta = Recetas()
        receta.Nombre=datos.get('nombre_Receta')
        receta.ingrediente1=datos.get('ingrediente1')
        receta.cant_ingrediente1=datos.get('cantidad1')
        receta.ingrediente2=datos.get('ingrediente2')
        receta.cant_ingrediente2=datos.get('cantidad2')
        receta.ingrediente3=datos.get('ingrediente3')
        receta.cant_ingrediente3=datos.get('cantidad3')
        receta.preparacion=datos.get('preparacion')
        receta.idClientes=cliente
        receta.idProductos=producto
        receta.save()
    return HttpResponseRedirect('/unimonito/home')
"""    now = datetime.datetime.now()
    producto = Productos.objects.get(pk=producto_id_compra)
    cliente=Clientes.objects.get(pk=cliente_id)
    factura=Facturas()
    factura.Fecha_Factura=now
    factura.idClientes=cliente
    factura.idProductos=producto
    factura.save()"""
