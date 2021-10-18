from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='categorias', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    producto = models.CharField(max_length=140)
    descripcion = models.TextField(blank=True, null=True)
    caracteristicas = models.CharField(max_length=140,blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='categorias')

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name_plural='productos'



