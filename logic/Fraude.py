import Header
from logic import Achado

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

    def verificaFraudeParcial(self,expressao,tipo):
        for j in self._Licitacao.getSecao():
            if j.getTipo() == tipo:
                achado = expressao.search(j.getConteudo())
                texto_achado = ''
                if achado[1]:
                    achado_obj = Achado(expressao.getNome(),j.getTitulo(),'','')
                    if achado[0].start()>Header.CONTEXTO_INI and len(j.getConteudo())> (achado[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = j.getConteudo()[achado[0].start()-Header.CONTEXTO_INI:achado[0].end()+Header.CONTEXTO_FIM]
                    elif achado[0].start()<Header.CONTEXTO_INI and len(j.getConteudo())> (achado[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = j.getConteudo()[0:achado[0].end()+Header.CONTEXTO_FIM]
                    elif achado[0].start()>Header.CONTEXTO_INI and len(j.getConteudo())< (achado[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = j.getConteudo()[achado[0].start()-Header.CONTEXTO_INI:]
                    else:
                        texto_achado = j.getConteudo()
                    achado_obj.setConteudoAchado(texto_achado)
                    print(achado_obj.getConteudoAchado())
                    print("*****************************")
                    return achado_obj
        return Achado(expressao.getNome(),None,'','')

    def verificarLicitacaoCompleta(self):
        achados = []
        for i in Header.LISTA_TODOS:
            c = False
            for key,valor in Header.TIPOS.items():
                if key != Header.TIPOS['HABILITACAO']:
                    achado = self.verificaFraudeCompleta(i,valor)
                    if achado.getSecaoAchado() != None:
                        achados.append(achado)
                        c = True
                        break
            if not c:
                achados.append(Achado(i.getNome(),None,'',''))
            
        for j in Header.LISTA_HABILITACAO:
            achados.append(self.verificaFraudeCompleta(j,Header.TIPOS['HABILITACAO']))
        return achados

    def verificarLicitacaoParcial(self):
        achados = []
        for i in Header.LISTA_TODOS:
            c = False
            for key,valor in Header.TIPOS.items():
                if key != Header.TIPOS['HABILITACAO']:
                    achado = self.verificaFraudeParcial(i,valor)
                    if achado.getSecaoAchado() != None:
                        achados.append(achado)
                        c = True
                        break
            if not c:
                achados.append(Achado(i.getNome(),None,'',''))
            
        for j in Header.LISTA_HABILITACAO:
            achados.append(self.verificaFraudeParcial(j,Header.TIPOS['HABILITACAO']))
        return achados


        

    
