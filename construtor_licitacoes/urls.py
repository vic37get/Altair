from django.urls import path,include
from . import views

app_name='construtor_licitacoes'
urlpatterns = [
    path('licitacao/',views.nova_licitacao,name='adicionar'),
    #path('licitacao/<pk>/editar/',views.editar_licitacao,name='editar'),
    #path('delete/<pk>', views.lic_delete, name='delete'),
]
