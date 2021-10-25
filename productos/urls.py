from django.urls import path
from .views import index, detalles_productos, filtrar_productos, productos_fotos, list_all_platos, list_all_platos_procedure,find_plato

urlpatterns = [

    path('', index, name='index'),
    path('detalles/<codigo>', detalles_productos, name='detalles'),
    path('filtrar/<nombre>', filtrar_productos, name='filtrar'),
    path('productosfotos', productos_fotos, name='productosfotos'),
    path('platosql/', list_all_platos, name='platosql'),
    path('platosproc/', list_all_platos_procedure, name='platosproc'),
    path('findplato/<cod>', find_plato, name='findplato')
]
