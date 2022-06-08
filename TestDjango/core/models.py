from django.db import models



# Modelo para Categorias
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de categoria')
  nombreCategoria = models.CharField(max_length = 50, verbose_name = 'Nombre de la cetgoria')

  def __str__(self):
    return self.nombreCategoria

# Modelo para Arte
class Arte(models.Model):
  idprod = models.CharField(max_length = 6, primary_key = True, verbose_name = 'Idproducto')
  nombre = models.CharField(max_length = 20, verbose_name = 'Nombre del arte')
  precio = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'Precio')
  categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

  def __str__(self):
    return self.idprod
