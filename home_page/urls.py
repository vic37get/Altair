from django.urls import path,include
from . import views

app_name='home_page'
urlpatterns = [
    path('', views.index,name='index'),
    path('templates',views.modelo,name='template'),
    path('enviar', views.enviar, name='enviar'),
    path('filtro',views.filtro,name='filtro'),
]
