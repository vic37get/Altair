from logic import Header
from logic import Fraude
from logic import LicitacaoProxy

class Main:
    def _init_(self,source=Header.SOURCE_r):
        self.all()

    def verificarAltair(self,licitacao):
        licitacao_Obj = LicitacaoProxy.ProxyLicitacao("",licitacao['tituloArquivo'],"")
        secoes = []
        from logic import API
        api = API.API()
        for i in licitacao['secoes']:
            secao = api.APISecao(i['titulo'],i['conteudo'])
            secao.verificaSecao()
            secoes.append(secao)
        licitacao_Obj.setSecoes(secoes)
        verificadorFraude = Fraude.Fraude(licitacao_Obj)
        licitacao_Obj.setTipoValidade(Header.TIPOS['VALIDO'])
        return verificadorFraude.getAchados()

    def all(self):
        '''
        #
        dataManipulation = ProxyDataManipulation()
        #
        dataManipulation.createEmptyFiles()
        #
        dataManipulation.createEmptydataFrame(Header.OUTPUT_NOME)
        #
        nomes = dataManipulation.getNomesEditais(Header.SOURCE_r)
        lista_fraudes = []
        for count,nome in enumerate(nomes):
            #
            dados = dataManipulation.readTxTFiles(nome,Header.SOURCE_r)
            ProxyLic = ProxyLicitacao('',nome,dados)
            ProxyLic.struct()
            #
            dataManipulation.saveTypeFiles(ProxyLic)
            for i in ProxyLic.getSecao():
                pass
            if ProxyLic.getTipoValidade() == Header.TIPOS['VALIDO']:
                verificadorFraude = Fraude(ProxyLic)
                verificadorFraude.getAchados()
                lista_fraudes.append(verificadorFraude)
        #
        dataManipulation.saveResultsAll(lista_fraudes)
        '''
        pass
    
    
    def verify(self):
        '''
        dataManipulation = ProxyDataManipulation()
        dataManipulation.createEmptyFiles()
        nomes = dataManipulation.getNomesEditais(Header.SOURCE_r)
        for count,nome in enumerate(nomes):
            dados = dataManipulation.readTxTFiles(nome,Header.SOURCE_r)
            ProxyLic = ProxyLicitacao('',nome,dados)
            ProxyLic.struct()
            dataManipulation.saveTypeFiles(ProxyLic)'''
        pass

    def collectRegex():
        from expressoes import lista_de_expressoes,lista_habilitacao
        return lista_de_expressoes,lista_habilitacao

     
