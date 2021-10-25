from django.urls import path
from .views import index, detalles_productos

urlpatterns = [

    path('', index, name='index'),
    path('detalles/<codigo>', detalles_productos, name='detalles')
]
