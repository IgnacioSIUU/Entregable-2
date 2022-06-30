from django.shortcuts import render
from .models import Producto
# Create your views here.
def tiendita(request):

    productos=Producto.objects.all()

    return render(request,'tiendita/tiendita.html', {"productos":productos})