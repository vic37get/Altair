import Header
from logic import Fraude
from LicitacaoProxy import ProxyLicitacao
from logic import RegraProxy
from logic import ProxyDataManipulation

class Main:
    def _init_(self,source=Header.SOURCE_r):
        self.all()

    def all(self):
        dataManipulation = ProxyDataManipulation()
        dataManipulation.createEmptyFiles()
        dataManipulation.createEmptydataFrame(Header.OUTPUT_NOME)
        nomes = dataManipulation.getNomesEditais(Header.SOURCE_r)
        lista_fraudes = []
        for count,nome in enumerate(nomes):
            dados = dataManipulation.readTxTFiles(nome,Header.SOURCE_r)
            ProxyLic = ProxyLicitacao('',nome,dados)
            ProxyLic.struct()
            dataManipulation.saveTypeFiles(ProxyLic)
            for i in ProxyLic.getSecao():
                pass
            if ProxyLic.getTipoValidade() == Header.TIPOS['VALIDO']:
                verificadorFraude = Fraude(ProxyLic)
                verificadorFraude.getAchados()
                lista_fraudes.append(verificadorFraude)
        dataManipulation.saveResultsAll(lista_fraudes)
    
    
    def verify(self):
        dataManipulation = ProxyDataManipulation()
        dataManipulation.createEmptyFiles()
        nomes = dataManipulation.getNomesEditais(Header.SOURCE_r)
        for count,nome in enumerate(nomes):
            dados = dataManipulation.readTxTFiles(nome,Header.SOURCE_r)
            ProxyLic = ProxyLicitacao('',nome,dados)
            ProxyLic.struct()
            dataManipulation.saveTypeFiles(ProxyLic)

    def collectRegex():
        from expressoes import lista_de_expressoes,lista_habilitacao
        return lista_de_expressoes,lista_habilitacao 