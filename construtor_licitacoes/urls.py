from django.urls import include, path

from . import views

app_name='construtor_licitacoes'
urlpatterns = [
    path('novaLicitacao/<pk>',views.nova_licitacao,name='adicionar'),
]
