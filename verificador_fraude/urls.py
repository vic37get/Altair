from django.urls import include, path

from . import views

app_name='verificador_fraude'
urlpatterns = [
    path('aud', views.homeAud, name='homeAud'),
    path('aud/avaliar/<pk>', views.avaliar, name='avaliar'),
    path('filtroVerificador',views.filtroVerificador,name='filtroVerificador'),
    path('aud/avaliar/<pk>/verificar',views.verificar,name='verificar'),
]
