from django.shortcuts import render, redirect
from .models import Arte
from .forms import ArteForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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

def Home(request):
    return render(request,'core/Home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'registracion.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('home')
