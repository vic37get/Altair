from django.urls import include, path
from . import views
from verificador_fraude import views as viewAud

app_name='home_page'
urlpatterns = [
    path('', views.index,name='index'),
    path('templates',views.modelo,name='template'),
    path('enviar', views.enviar, name='enviar'),
    path('aud', viewAud.homeAud, name='homeAud'),
    path('filtro',views.filtro,name='filtro'),
]
