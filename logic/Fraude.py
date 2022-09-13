import Header
from Achado import Achado
class Fraude:
    def __init__(self,Licitacao):
        self._Licitacao = Licitacao
        self.achados = None
    
    def getLicitacao(self):
        return self._Licitacao

    def verificaFraudeCompleta(self,expressao,tipo):
        for j in self._Licitacao.getSecao():
            if j.getTipo() == tipo:
                achado = expressao.search(j.getConteudo())
                if achado[1]:
                    achado_obj = Achado(expressao.getNome(),j.getTitulo(),'','')
                    achado_obj.setConteudoAchado(j.getConteudo())
                    return achado_obj
        return Achado(expressao.getNome(),None,'','')
    