from django.shortcuts import render, redirect
from .models import Arte
from .forms import ArteForm
# Create your views here.

def home(request):
    lista = Arte.objects.all()
    contexto = {
        'artes': lista,
    }
    return render(request, 'core/index.html', contexto)

def form_arte(request):
    contexto = { 
        'form': ArteForm(),
        }
    if request.method=='POST':
        formulario=ArteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form_arte.html', contexto)

def form_mod_arte(request, id):
    arte = Arte.objects.get(idprod=id)
    contexto = { 
        'form': ArteForm(instance=Arte),
        }
    if request.method=='POST':
        formulario=ArteForm(data=request.POST, instance=arte)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form-mod-arte.html', contexto)

def form_del_arte(request, id):
    arte = Arte.objects.get(idprod=id)
    arte.delete()
    return redirect(to="home")

def main_pinturas(request):
    return render(request, 'core/main_pinturas.html')
