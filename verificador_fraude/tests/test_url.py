from django.urls import resolve
from unittest import TestCase

class UrlTests(TestCase):
    def test_urlHomePage(self):
        resolver = resolve('/gestor/')
        self.assertEqual(resolver.view_name, 'home_page:index')

        resolver = resolve('/gestor/templates')
        self.assertEqual(resolver.view_name, 'home_page:template')

        resolver = resolve('/gestor/perfil')
        self.assertEqual(resolver.view_name, 'home_page:perfil')

        resolver = resolve('/gestor/filtro')
        self.assertEqual(resolver.view_name, 'home_page:filtro')

    def test_urlConstrutor(self):
        resolver = resolve('/gestor/construcao/novaLicitacao/<pk>')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:adicionar')

        resolver = resolve('/gestor/construcao/editarLicitacao/<pk>')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:editar')

        resolver = resolve('/gestor/construcao/salvar')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:salvar')

        resolver = resolve('/gestor/construcao/editarTitulo')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:editarTitulo')

        resolver = resolve('/gestor/construcao/enviar')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:enviar')

        resolver = resolve('/gestor/construcao/enviarG')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:enviarGeral')

        resolver = resolve('/gestor/construcao/enviar/<pk>')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:enviarConstrucao')

        resolver = resolve('/gestor/construcao/submeter/<pk>')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:enviarSubmetidos')

        resolver = resolve('/gestor/construcao/excluirLicitacao/<pk>')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:excluir')

        resolver = resolve('/gestor/construcao/toPDF')
        self.assertEqual(resolver.view_name, 'construtor_licitacoes:toPDF')

    def test_urlHome_All(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.view_name, 'home_all:login')

        resolver = resolve('/loginAuth/')
        self.assertEqual(resolver.view_name, 'home_all:loginAuth')

        resolver = resolve('/logout/')
        self.assertEqual(resolver.view_name, 'home_all:logout')

        resolver = resolve('/cadastro/')
        self.assertEqual(resolver.view_name, 'home_all:cadastro')

        resolver = resolve('/submeterCadastro/')
        self.assertEqual(resolver.view_name, 'home_all:submeterCadastro')

    def test_urlVerificador_fraude(self):
        resolver = resolve('/aud/')
        self.assertEqual(resolver.view_name, 'verificador_fraude:homeAud')

        resolver = resolve('/aud/avaliar/<pk>')
        self.assertEqual(resolver.view_name, 'verificador_fraude:avaliar')

        resolver = resolve('/aud/perfil/')
        self.assertEqual(resolver.view_name, 'verificador_fraude:perfil')

        resolver = resolve('/aud/filtroVerificador')
        self.assertEqual(resolver.view_name, 'verificador_fraude:filtroVerificador')

        resolver = resolve('/aud/avaliar/<pk>/verificar')
        self.assertEqual(resolver.view_name, 'verificador_fraude:verificar')

        resolver = resolve('/aud/avaliacao/<pk>')
        self.assertEqual(resolver.view_name, 'verificador_fraude:avaliacao')
        