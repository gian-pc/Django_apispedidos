from django.contrib import admin
from .models import Categoria, Productos, Productos_Fotos, Productos_Precio, Proveedor

admin.site.register([Categoria, Productos, Productos_Fotos, Productos_Precio, Proveedor])
