from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.
#Permite administrar el modelo completo

admin.site.register(CategoriaProd)
admin.site.register(Producto)