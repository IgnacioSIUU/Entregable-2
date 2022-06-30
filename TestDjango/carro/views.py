from .carro import Carro
from tiendita.models import Producto
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tiendita")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tiendita")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("tiendita")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar()
    return redirect("tiendita")