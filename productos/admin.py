from django.contrib import admin
from .models import Categoria, Productos

admin.site.register([Categoria, Productos])
