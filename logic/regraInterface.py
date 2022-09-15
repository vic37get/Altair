from abc import abstractmethod,ABC

class RegraInterface(ABC):

    @abstractmethod
    def getNome(self,):
        pass

    @abstractmethod
    def setNome(self,nome):
        pass

    @abstractmethod
    def getRegexPositivo(self):
        pass

    @abstractmethod
    def setRegexPositivo(self,regra):
        pass

    @abstractmethod
    def getRegexNegativos(self):
        pass

    @abstractmethod
    def setRegexNegativos(self,regras):
        pass