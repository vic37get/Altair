from django.urls import include, path
from verificador_fraude import views as viewAud

from . import views

app_name='home_page'
urlpatterns = [
    path('', views.index,name='index'),
    path('templates',views.modelo,name='template'),
    path('perfil', views.perfil,name='perfil'),
    path('enviar', views.enviar, name='enviar'),
    path('aud', viewAud.homeAud, name='homeAud'),
    path('cadastrar',views.submeterCadastro,name='submeterCadastro'),
    path('filtro',views.filtro,name='filtro'),
]
