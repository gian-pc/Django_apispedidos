from django.shortcuts import render
from .models import Productos, Productos_Fotos
from django.http import Http404
from django.db import connection


def index(request):
    # QuerySet
    productos = Productos.objects.all()
    context = {'prod': productos}
    return render(request, "index.html", context)


def detalles_productos(request, codigo):
    try:
        productos_id = Productos.objects.get(codigo=codigo)
        context = {'prod': productos_id}
    except Productos.DoesNotExist:
        raise Http404("Producto No Existe. Lo sentimos")
    return render(request, "productodetalle.html", context)


def filtrar_productos(request, nombre):
    busqueda = Productos.objects.filter(nombre__contains=nombre)
    context = {'prod': busqueda}
    return render(request, "productos.html", context)


def productos_fotos(request):
    platos = Productos_Fotos.objects.all()
    context = {'prod': platos}
    return render(request, "productosfotos.html", context)


# MYSQL DIRECTAMENTE
def list_all_platos(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from productos_productos")
        rowdata = cursor.fetchall()
        result = []
        for item in rowdata:
            result.append(list(item))
        context = {'prod': result}
    return render(request, 'productosql.html', context)


# EJECUTANDO EL PROCEDIMIENTO
def list_all_platos_procedure(request):
    with connection.cursor() as cursor:
        cursor.callproc("usp_productos")
        rowdata = cursor.fetchall()
        result = []
        for item in rowdata:
            result.append(list(item))
        context = {'prod': result}
    return render(request, 'productosqlproc.html', context)


def find_plato(request, cod):
    with connection.cursor() as cursor:
        cursor.callproc("usp_productos_fotos", [cod])
        rowdata = cursor.fetchall()
        result = []
        for item in rowdata:
            result.append(list(item))
        context = {'prod': result}
    return render(request, 'productosqlproc.html', context)
