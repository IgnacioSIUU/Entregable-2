from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre Categoria')

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"
    
    def __str__(self):
        return self.nombre

##Modelo Producto

class Producto(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre Producto')
    descripcion=models.CharField(max_length=100, verbose_name='Descripción Producto')
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tiendita", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"