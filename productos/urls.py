from django.urls import path
from .views import index, detalles_productos,filtrar_productos

urlpatterns = [

    path('', index, name='index'),
    path('detalles/<codigo>', detalles_productos, name='detalles'),
    path('filtrar/<nombre>', filtrar_productos, name='filtrar')
]
