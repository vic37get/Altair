from django.urls import include, path

from . import views

app_name='construtor_licitacoes'
urlpatterns = [
    path('novaLicitacao/<pk>',views.nova_licitacao,name='adicionar'),
    path('editarLicitacao/<pk>',views.editar,name='editar'),
    path('salvar',views.salvar,name='salvar'),
    path('editarTitulo',views.editarTitulo,name='editarTitulo'),
    path('enviar', views.enviarGeral, name='enviarGeral'),
    path('enviar/<pk>', views.enviarConstrucao, name='enviarConstrucao'),
    path('enviarD/<pk>',views.salvarFormulario,name='enviarSubmetidos'),
    path('excluirLicitacao/<pk>',views.excluir,name='excluir'),
]
