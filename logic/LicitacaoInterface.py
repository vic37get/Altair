from abc import abstractmethod,ABC

class LicitacaoInterface(ABC):

    @abstractmethod
    def setSecoes(self, secoes):
        pass
    
    @abstractmethod
    def getSecao(self):
        pass

    @abstractmethod
    def setNomeLicitacao(self, nomeLicitacao):
        pass
        
    @abstractmethod    
    def getNomeLicitacao(self):
        pass
    
    @abstractmethod
    def setNomeArquivo(self, nomeArquivo):
        pass
    
    @abstractmethod
    def getNomeArquivo(self):
        pass

    @abstractmethod
    def getDados(self):
        pass
    
    @abstractmethod
    def setDados(self,dados):
        pass

    @abstractmethod
    def findSectionAndText(secoes,dados):
        pass