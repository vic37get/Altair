from django.urls import include, path

from . import views

app_name='verificador_fraude'
urlpatterns = [
    path('', views.homeAud, name='homeAud'),
    path('avaliar/<pk>', views.avaliar, name='avaliar'),
    path('perfil/', views.perfil,name='perfil'),
    path('editarPerfil/', views.editarPerfil,name='editarPerfil'),
    path('alterarSenha', views.alterarSenha,name='alterarSenha'),
    path('alteracaoDeSenha', views.alteracaoDeSenha,name='alteracaoDeSenha'),
    path('filtroVerificador',views.filtroVerificador,name='filtroVerificador'),
    path('avaliar/<pk>/verificar',views.verificar,name='verificar'),
    path('avaliacao/<pk>',views.avalicao,name='avaliacao')
]
