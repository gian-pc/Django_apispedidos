from django.contrib import admin
from .models import Categoria, Productos, Productos_Fotos,Productos_Precio

admin.site.register([Categoria, Productos,Productos_Fotos,Productos_Precio])

