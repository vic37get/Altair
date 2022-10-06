from logic import Header
from logic import Achado

class Fraude:
    def __init__(self,Licitacao):
        self._Licitacao = Licitacao
        self.achados = None
    
    def getLicitacao(self):
        return self._Licitacao

    def verificaFraudeCompleta(self,expressao,tipo):
        for secao in self._Licitacao.getSecao():
            if secao.getTipo() == tipo:
                fraude_achada = expressao.search(secao.getConteudo())
                if fraude_achada[1]:
                    objeto_achado = Achado.Achado(expressao.getNome(),secao.getTitulo(),'','')
                    objeto_achado.setConteudoAchado.Achado(secao.getConteudo())
                    return objeto_achado
        return Achado.Achado(expressao.getNome(),None,'','')

    def verificaFraudeParcial(self,expressao,tipo):
        for secao in self._Licitacao.getSecao():
            if secao.getTipo() == tipo:
                fraude_achada = expressao.search(secao.getConteudo())
                texto_achado = ''
                if fraude_achada[1]:
                    achado_obj = Achado.Achado(expressao.getNome(),secao.getTitulo(),'',expressao.getDescricao())
                    if fraude_achada[0].start()>Header.CONTEXTO_INI and len(secao.getConteudo())> (fraude_achada[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = secao.getConteudo()[fraude_achada[0].start()-Header.CONTEXTO_INI:fraude_achada[0].end()+Header.CONTEXTO_FIM]
                    elif fraude_achada[0].start()<Header.CONTEXTO_INI and len(secao.getConteudo())> (fraude_achada[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = secao.getConteudo()[0:fraude_achada[0].end()+Header.CONTEXTO_FIM]
                    elif fraude_achada[0].start()>Header.CONTEXTO_INI and len(secao.getConteudo())< (fraude_achada[0].end()+Header.CONTEXTO_FIM):
                        texto_achado = secao.getConteudo()[fraude_achada[0].start()-Header.CONTEXTO_INI:]
                    else:
                        texto_achado = secao.getConteudo()
                    achado_obj.setConteudoAchado(texto_achado)
                    return achado_obj
        return Achado.Achado(expressao.getNome(),None,'','')

    def verificarLicitacaoCompleta(self):
        Todas_as_fraudes_achadas = []
        for i in Header.LISTA_TODOS:
            isNotNull = False
            for key,valor in Header.TIPOS.items():
                if key != Header.TIPOS['HABILITACAO']:
                    Fraudes_achadas = self.verificaFraudeCompleta(i,valor)
                    if Fraudes_achadas.getSecaoAchado.Achado() != None:
                        Todas_as_fraudes_achadas.append(Fraudes_achadas)
                        isNotNull = True
                        break
            if not isNotNull:
                Todas_as_fraudes_achadas.append(Achado.Achado(i.getNome(),None,'',''))
            
        for j in Header.LISTA_HABILITACAO:
            Todas_as_fraudes_achadas.append(self.verificaFraudeCompleta(j,Header.TIPOS['HABILITACAO']))
        return Todas_as_fraudes_achadas

    def verificarLicitacaoParcial(self):
        Todas_as_fraudes_achadas = []
        for i in Header.LISTA_TODOS:
            isNotNull = False
            for key,valor in Header.TIPOS.items():
                if key != Header.TIPOS['HABILITACAO']:
                    fraudes_achadas = self.verificaFraudeParcial(i,valor)
                    if fraudes_achadas.getSecaoAchado() != None:
                        Todas_as_fraudes_achadas.append(fraudes_achadas)
                        isNotNull = True
                        break
            if not isNotNull:
                Todas_as_fraudes_achadas.append(Achado.Achado(i.getNome(),None,'',''))
            
        for j in Header.LISTA_HABILITACAO:
            Todas_as_fraudes_achadas.append(self.verificaFraudeParcial(j,Header.TIPOS['HABILITACAO']))
        return Todas_as_fraudes_achadas
        
    def getAchadosCompleta(self):
        if self.achados == None:
            self.achados = self.verificarLicitacaoCompleta()
        return self.achados
    
    def getAchadosParcial(self):
        if self.achados == None:
            self.achados = self.verificarLicitacaoParcial()
        return self.achados

    def getAchados(self):
        return self.getAchadosParcial()


        

    
