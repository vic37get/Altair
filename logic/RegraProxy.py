from logic import regraInterface as i
from logic import Regra

class RegraProxy(i.RegraInterface):
    def __init__(self,nome='Null',regra=None):
        self._Regra = Regra.Regra(nome,regra)

    def getNome(self):
        return self._Regra.getNome()

    def setNome(self, nome):
        return self._Regra.setNome(nome)

    def getRegexPositivo(self):
        return self._Regra.getRegexPositivo()

    def setRegexPositivo(self, regra):
        return self._Regra.setRegexPositivo(regra)

    def getRegexNegativos(self):
        return self._Regra.getRegexNegativos()

    def setRegexNegativos(self, regras):
        return self._Regra.setRegexNegativos(regras)
    
    def __str__(self):
        return self._Regra.__str__()
    
    def search(self,texto):
        negativos = []
        if len(self._Regra.getRegexNegativos()) >0:
            for i in self._Regra.getRegexNegativos():
                negativos.append(self._Regra.search(i,texto))
        positivo = self._Regra.search(self._Regra.getRegexPositivo(),texto)
        #questão do positivo e negativo
        return positivo,all([positivo,not(any(negativos))])

    def getDescricao(self):
        return self._Regra.getDescricao()

    def setDescricao(self, descricao):
        self._Regra.setDescricao(descricao)

    def toJson(self):
        return self._Regra.toJson()

    def loadJson(self,json):
        return self._Regra.loadJson(json)

if __name__ == '__main__':
    RegraProxy('*','*regra')