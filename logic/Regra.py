from logic import regraInterface as i
import re,json

class Regra(i.RegraInterface):
    def __init__(self,nome,regra):
        self._regexPositivo = regra
        self._regexNegativos = []
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getRegexPositivo(self):
        return self._regexPositivo

    def setRegexPositivo(self, regra):
        self._regexPositivo = regra

    def getRegexNegativos(self):
        return self._regexNegativos

    def setRegexNegativos(self, regras):
        self._regexNegativos = regras

    def __str__(self):
        return self._nome+"\n"+str(self._regexPositivo)

    def search(self,regra,texto):
        return re.search(regra,texto)

    def toJson(self):
        retorno = dict()
        for key,value in self.__dict__.items():
            retorno[key] = str(value)
        return retorno

    def loadJson(self,json):
        self._nome = json['_nome']
        self._regexPositivo = eval(json['_regexPositivo'])
        self._regexNegativos = eval(json['_regexNegativos'])
