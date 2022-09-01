from regraInterface import RegraInterface
import re

class Regra(RegraInterface):
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
        pass