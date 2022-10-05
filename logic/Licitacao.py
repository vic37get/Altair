import base64
import re
from email.mime import base

from bson.objectid import ObjectId
from utils import connectMongo

from logic import Header
from logic import LicitacaoInterface
from logic import Secao

db = connectMongo('Altair')
class Licitacao(LicitacaoInterface.LicitacaoInterface):
    def __init__(self, nomeLicitacao, nomeArquivo,dados):
        self.nomeLicitacao = nomeLicitacao
        self.nomeArquivo = nomeArquivo
        self.dados = dados
        self.secoes = []
        self._isValido = False
        self._tipo = 'NO TYPE'
        self.secoes_principais = Header.TIPOS_SECOES.copy()

    def setSecoes(self,secoes):
        self.secoes = secoes
    
    def getSecao(self):
        return self.secoes

    def addSecoes(self,secoes):
        self.secoes.append(secoes)

    def setNomeLicitacao(self, nomeLicitacao):
        self.nomeLicitacao = nomeLicitacao
        
    def getNomeLicitacao(self):
        return self.nomeLicitacao
    
    def setNomeArquivo(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
    
    def getNomeArquivo(self):
        return self.nomeArquivo

    def getDados(self):
        return self.dados

    def setDados(self,dados):
        self.dados = dados

    def findSectionAndTextBank(self, licitacao_id):
        lista_secoes = []
        conteudo_secao = []
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId(licitacao_id)})
        exp_html = re.compile('<.*?>')

        for secao in licitacao['secoes']:
            titulo = ''
            titulo = base64.b64decode(secao['titulo']).decode('ISO-8859-1')
            titulo = re.sub(exp_html, '', titulo)
            lista_secoes.append(titulo)
            
            conteudo = ''
            conteudo = base64.b64decode(secao['conteudo'][0]).decode('ISO-8859-1')
            conteudo = re.sub(exp_html, '', conteudo)
            conteudo_secao.append(conteudo)

            return lista_secoes, conteudo_secao

    def findSectionAndText(self, secoes, dados):
        lista_secoes = []
        conteudo_secao = []
        dados2 = dados
        c = 0
        while secoes != None:
            texto_entre_secoes = dados[c+secoes.end():]
            c += secoes.end()       
            lista_secoes.append(secoes)
            dados2 = dados2[secoes.end():]        
            secoes = Header.EXP_GERAL.search(dados2)[0]
            if secoes == None:             
                texto_entre_secoes = dados2
            else:
                texto_entre_secoes = texto_entre_secoes[:secoes.start()]
            if texto_entre_secoes[0:1] != '\n':
                texto_entre_secoes = ''
                 
            conteudo_secao.append(texto_entre_secoes)
        if len(lista_secoes) > 0:
            if lista_secoes[-1] == None:
                lista_secoes = lista_secoes[0:-1]

        return lista_secoes, conteudo_secao
    
    def structBank(self, licitacao_id):
        lista_secoes, conteudo_secao = self.findSectionAndTextBank(self, licitacao_id)
        for i in zip(lista_secoes, conteudo_secao):
            secao = i[0]
            secao.verificaSecao()
            self.addSecoes(secao)

    def struct(self,secoes,dados):
        lista_secoes,conteudo_secao = self.findSectionAndText(secoes,dados)
        for i in range(len(lista_secoes)-1,-1,-1):
            anexo_nofinal = Header.EXP_ANEXO.search(conteudo_secao[i])[0]
            if anexo_nofinal:
                conteudo_secao[i] = conteudo_secao[i][:anexo_nofinal.start()]
        for i in zip(lista_secoes,conteudo_secao):
            secao = Secao.Secao(i[0].group(8),i[0].group(15),i[1],i[0].group(0))
            secao.verificaSecao()
            self.addSecoes(secao)

    def setTipoSecoes(self):
        for i in self.getSecao():
            self.secoes_principais[i.getTipo()] = True

    def pulaSumario(self):
        i = 0
        while(i<len(self.getSecao())):
            texto = self.getSecao()[i].getConteudo()
            if len(texto.replace('\n','')) == 0:
                self.getSecao().pop(i)
            else:
                i+=1

    def verificaSecoesObrigatorias(self):
        for i in Header.SECOES_OBRIGATORIAS:
            if not self.secoes_principais[i.getNome()]:
                return False
        return True

    def verificaSecoesOpcionais(self):
        for i in Header.SECOES_OPCIONAIS:
            if self.secoes_principais[i.getNome()]:
                return True
        return False

    def isValido(self):
        self._isValido = all([self.verificaSecoesObrigatorias(),self.verificaSecoesOpcionais()])
        return self._isValido

    def getTipoValidade(self):
        return self._tipo
    
    def setTipoValidade(self,tipo):
        self._tipo = tipo

    def getSecoesEmpty(self):
        secoesVazias = []
        for i in self.getSecao():
            if i.isEmpty():
                secoesVazias.append(i)
        return secoesVazias
