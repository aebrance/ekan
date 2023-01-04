from django.db import models


class Categorias(models.Model):
    nombre = models.CharField(max_length=100, db_index=True, default="Categoria")
    slug = models.SlugField(max_length=100, db_index=True, default="url")

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    articulo = models.CharField(max_length=4, default="0000")
    producto = models.CharField(max_length=50, default="Producto")
    stock_disponible = models.IntegerField(default=0)
    precio_menor = models.FloatField(default=0)
    precio_mayor = models.FloatField(default=0)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    categoria = models.ForeignKey(
        Categorias, blank=False, null=True, on_delete=models.CASCADE
    )
