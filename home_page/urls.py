from django.urls import include, path
from verificador_fraude import views as viewAud

from . import views

app_name='home_page'
urlpatterns = [
    path('', views.index,name='index'),
    path('templates',views.modelo,name='template'),
    path('perfil', views.perfil,name='perfil'),
    path('alterarSenha', views.alterarSenha,name='alterarSenha'),
    path('alteracaoDeSenha', views.alteracaoDeSenha,name='alteracaoDeSenha'),
    path('filtro',views.filtro,name='filtro'),
    path('editarPerfil',views.editarPerfil,name='editarPerfil'),
]
