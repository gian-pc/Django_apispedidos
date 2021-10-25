from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='categorias', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuarios', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'categorias'
        ordering = ['nombre']


class Proveedor(models.Model):
    tipo_prov = (
        ('N', 'NACIONAL'),
        ('E', 'EXTRANJERO')
    )
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    ruc = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=tipo_prov)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'proveedores'
        ordering = ['id']


class Productos(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField(blank=True, null=True)
    caracteristicas = models.CharField(max_length=140, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categorias')
    proveedor = models.ManyToManyField(Proveedor)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'productos'


class Productos_Fotos(models.Model):
    foto1 = models.ImageField(upload_to='productos/fotos', null=True, blank=True)
    foto2 = models.ImageField(upload_to='productos/fotos', null=True, blank=True)
    foto3 = models.ImageField(upload_to='productos/fotos', null=True, blank=True)
    foto4 = models.ImageField(upload_to='productos/fotos', null=True, blank=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='productos_fotos')
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name_plural = 'productos_fotos'


class Productos_Precio(models.Model):
    precioinsumo = models.DecimalField(max_digits=5, decimal_places=2)
    precioventa = models.DecimalField(max_digits=5, decimal_places=2)
    precioespecial = models.DecimalField(max_digits=5, decimal_places=2)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='productos_precios')
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombre + ' Precio Venta:' + str(self.precioventa) + \
               ' Precio Especial:' + str(self.precioespecial)

    class Meta:
        verbose_name_plural = 'productos_precios'
