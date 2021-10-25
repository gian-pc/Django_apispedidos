from django.shortcuts import render
from .models import Productos
from django.http import Http404


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
