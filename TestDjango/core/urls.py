from django.urls import path
from .views import home, form_arte, form_mod_arte, form_del_arte, main_pinturas

urlpatterns = [
    path('',home,name="home"),
    path('form_arte', form_arte, name="form_arte"),
    path('form-mod-arte/<id>', form_mod_arte, name="form_mod_arte"),
    path('form-del-arte/<id>', form_del_arte, name="form_del_arte"),
    path('main_pinturas',main_pinturas,name="main_pinturas"),
    
]