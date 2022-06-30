from django.urls import path
from rest_arte import views
from rest_arte.viewslogin import login
from rest_arte.views import lista_arte,detalle_arte


urlpatterns = [
    path('lista_arte', lista_arte, name="lista_arte"),
    path('detalle_arte/<id>',detalle_arte,name="detalle_arte"),
    path('login',login,name="login"),
    
]