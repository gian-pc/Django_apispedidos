from django.shortcuts import render
from .models import Productos


def index(request):
    # QuerySet
    productos = Productos.objects.all()
    context = {'prod': productos}
    return render(request, "index.html", context)
