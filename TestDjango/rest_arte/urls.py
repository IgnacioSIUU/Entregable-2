from django.urls import path
from rest_arte.views import lista_arte

urlpatterns = [
    path('lista_arte', lista_arte, name="lista_arte"),
]