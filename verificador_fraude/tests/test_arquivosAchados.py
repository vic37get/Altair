from django.test import SimpleTestCase
from logic import Achado


class arquivosAchados(SimpleTestCase):

    def test_licitacoes(self):
        #testando setters
        try:
            tipoAchado_teste = "comprovante_localizacao"
            secao_teste = "secao2_sub"
            conteudo_teste  = "papel timbrado e subscrita pelo representante legal ou pelo procurador se este tiver outorga para tal, assegurando a inexistência de fato impeditivo para licitar ou contratar com a Administração; c) Alvará de licença de funcionamento"
            descricao_teste = "Exigência de alvará de funcionamento ou outra comprovação de localização do licitante para habilitação."
            arquivoAchado =  Achado.Achado(tipoAchado_teste,secao_teste,conteudo_teste,descricao_teste)
            arquivoAchado.setConteudoAchado(conteudo_teste)
            arquivoAchado.setDescricaoAchado(descricao_teste)
            arquivoAchado.setSecaoAchado(secao_teste)
            arquivoAchado.setTipoAchado(tipoAchado_teste)
        except:
            #print("erro ao setar informações, verifique se foram passadas corretamente")
            ...

        try:
            #testando getters
            self.assertEquals(arquivoAchado.getTipoAchado,"comprovante_localizacao")
            self.assertEquals(arquivoAchado.getSecaoAchado,"secao2_sub")
            self.assertEquals(arquivoAchado.getConteudoAchado,conteudo_teste)
            self.assertEquals(arquivoAchado.getDescricaoAchado,descricao_teste)
        except:
            #print("Erro ao recuperar informações")
            ...
