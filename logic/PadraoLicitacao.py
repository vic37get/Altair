import os
from weakref import proxy
import Header
from LicitacaoProxy import ProxyLicitacao

class PadraoLicitacao:
    def __init__(self, document):
        self.document = document
        self.proxylicitacao = ProxyLicitacao('','','')
        self.proxylicitacao.setDados("texto")
        self.proxylicitacao.struct()

    def verificaTipo(self):
        arquivo = self.document
        nome, extensao = os.path.splitext(arquivo)
        if extensao != '.pdf':
            return False
        return True

    def verificaPesquisavel(self):
        #proxy = proxyDataManipulation() criar dps
        conteudo = proxy.transformPdfToTxt(self.document)
        if conteudo == None or len(conteudo) < 100:
            return False
        else: 
            return True

    def verificaSecaoVazia(self):
        result = self.proxylicitacao.getSecoesEmpty()
        if len(result) == 0:
            return True
        else:
            return 'A secao {} está vazia'.format(result),result

    def verificaOrdemSecoes(self):
        numerosecoes = []
        for secao in self.proxylicitacao.getSecao():
            try:
                numero = int(secao.getNumeracao())
            except:
                #numero = rom_parse(secao.getNumeracao()) passar de romano para numeral
                numerosecoes.append(numero)

        for num in range(0, len(numerosecoes)):
            if num+1 != numerosecoes[num]:
                return False
            return True

    def verificaSecoesPrincipais(self):
        pass


