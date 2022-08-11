from django.urls import path,include
from . import views

app_name='construtor_licitacoes'
urlpatterns = [
    path('novaLicitacao/',views.nova_licitacao,name='adicionar'),
]
