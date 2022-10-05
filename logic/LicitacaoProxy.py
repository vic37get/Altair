from logic import Licitacao
from logic import LicitacaoInterface
from logic import Header

class ProxyLicitacao(LicitacaoInterface.LicitacaoInterface):
    def __init__(self, nomeLicitacao, nomeArquivo,dados):
        self._Licitacao = Licitacao.Licitacao(nomeLicitacao, nomeArquivo,dados)
        self._CACHE_SECOES = None
        self._CACHE_DADOS = None
        self._CACHE_ISVALIDO = None

        self._CACHE_SECOES_PRINCIPAIS = Header.TIPOS_SECOES.copy()

    def getObjeto(self):
        return self._CACHE_SECOES_PRINCIPAIS['OBJETO']

    def getHabilitacao(self):
        return self._CACHE_SECOES_PRINCIPAIS['HABILITACAO']

    def getCredenciamento(self):
        return self._CACHE_SECOES_PRINCIPAIS['CREDENCIAMENTO']

    def getCondicoes_participacao(self):
        return self._CACHE_SECOES_PRINCIPAIS['CONDICAO_PARTICIPACAO']

    def getJulgamento(self):
        return self._CACHE_SECOES_PRINCIPAIS['JULGAMENTO']
 
    def setSecoes(self, secoes):
        self.clearCache()
        return self._Licitacao.setSecoes(secoes)
    
    def getSecoesEmpty(self):
        return self._Licitacao.getSecoesEmpty()

    def getSecoes(self):
        if self._CACHE_SECOES == None:
            self._CACHE_SECOES = self._Licitacao.getSecoes()
            return self._CACHE_SECOES
        else:
            return self._CACHE_SECOES


    def setNomeLicitacao(self, nomeLicitacao):
        return self._Licitacao.setNomeArquivo(nomeLicitacao)
        
   
    def getNomeLicitacao(self):
        return self._Licitacao.getNomeArquivo()
    
  
    def setNomeArquivo(self, nomeArquivo):
        return self._Licitacao.setNomeArquivo(nomeArquivo)
    

    def getNomeArquivo(self):
        return self._Licitacao.getNomeArquivo()
    
    def getDados(self):
        if self._CACHE_DADOS == None:
            self._CACHE_DADOS =  self._Licitacao.getDados()
            return self._CACHE_DADOS
        else:
            return self._CACHE_DADOS

    def setDados(self,dados):
        return self._Licitacao.setDados(dados)

    def findSectionAndText(self,secoes,dados):
        return self._Licitacao.findSectionAndText(secoes,dados)

    def struct(self):
        busca_anexo = Header.EXP_ANEXO.search(self.getDados())[0]
        if not busca_anexo:
            secoes = Header.EXP_GERAL.search(self.getDados())[0]
            self._Licitacao.struct(secoes,self.getDados())
            self.pulaSumario()
        else:
            secoes = Header.EXP_GERAL.search(self.getDados()[:busca_anexo.start()])[0]
            self._Licitacao.struct(secoes,self.getDados()[:busca_anexo.start()])
            self.pulaSumario()
            if len(self.getSecoes())<3:
                secoes = Header.EXP_GERAL.search(self.getDados()[busca_anexo.end():])[0]
                self._Licitacao.struct(secoes,self.getDados()[busca_anexo.end():])
                self.pulaSumario()
        self.clearCache()
        self.setTipoSecoes()

        candidatos_objeto,candidatos_habilitacao,candidatos_julgamento = [],[],[]
        for i in self.getSecoes():
            if i.getTipo() == Header.TIPOS['OBJETO']:
                candidatos_objeto.append(i)
            if i.getTipo() == Header.TIPOS['HABILITACAO']:
                candidatos_habilitacao.append(i)
            if i.getTipo() == Header.TIPOS['JULGAMENTO']:
                candidatos_julgamento.append(i)
            if self._CACHE_SECOES_PRINCIPAIS[i.getTipo()] == False:
                self._CACHE_SECOES_PRINCIPAIS[i.getTipo()] = i

        self._CACHE_SECOES_PRINCIPAIS[Header.TIPOS['OBJETO']] = self.selectSECAO(candidatos_objeto,Header.TAMANHO_MAX_OBJ)
        if Header.OP_MOD_DATAFRAME:
            #VERBOSE
            Header.VERBOSE.addMetaNumeroSecoes(Header.TIPOS['HABILITACAO'],len(candidatos_habilitacao))
            Header.VERBOSE.addMetaNumeroSecoes(Header.TIPOS['JULGAMENTO'],len(candidatos_julgamento))
            Header.VERBOSE.addMetaNumeroSecoes(Header.TIPOS['OBJETO'],len(candidatos_objeto))
            self.concatenaSecoes(
                [Header.TIPOS['HABILITACAO'],candidatos_habilitacao],
                [Header.TIPOS['JULGAMENTO'],candidatos_julgamento])
        '''
        for i in self.getSecao():
            #Header.VERBOSE.addInfoSecao(i)
            ...
        '''
        if Header.EXP_AVISO.search(self.getDados())[0]:
            self.setTipoValidade(Header.TIPOS['AVISO'])
            return
        if len(self.getSecoes()) == 0:
            self.setTipoValidade(Header.TIPOS['SEM_SECAO'])
            return
        if self.isValido():
            self.setTipoValidade(Header.TIPOS['VALIDO'])
        else:
            self.setTipoValidade(Header.TIPOS['INVALIDO'])
            return

    def concatenaSecoes(self,*args):
        for i in args:
            try:
                self._CACHE_SECOES_PRINCIPAIS[i[0]].setConteudo(self.concatenacao(i[1]))
            except:
                pass

    def selectSECAO(self,candidatos,numeroMaximo):
        secao = False
        maior = -1
        if len(candidatos) == 1:
            secao = candidatos[0]
        elif len(candidatos) > 1:
            for i in candidatos:
                if len(i.getTitulo())<numeroMaximo:
                    if maior > len(i.getConteudo()) or maior == -1:
                        maior = len(i.getConteudo())
                        secao = i
            if not secao:
                secao = candidatos[0]
        return secao
    
    def setTipoSecoes(self):
        return self._Licitacao.setTipoSecoes()

    def pulaSumario(self):
        self.clearCache()
        self._Licitacao.pulaSumario()
    
    def clearCache(self):
        self._CACHE_SECOES = None
        self._CACHE_DADOS = None

    def verificaSecoesObrigatorias(self):
        return self._Licitacao.verificaSecoesObrigatorias()

    def verificaSecoesOpcionais(self):
        return self._Licitacao.verificaSecoesOpcionais()

    def isValido(self):
        if self._CACHE_ISVALIDO == None:
            self._CACHE_ISVALIDO = self._Licitacao.isValido()
            return self._CACHE_ISVALIDO
        else:
            return self._CACHE_ISVALIDO
    
    def getTipoValidade(self):
        return self._Licitacao.getTipoValidade()
    
    def setTipoValidade(self,tipo):
        return self._Licitacao.setTipoValidade(tipo)
    
    def concatenacao(self,lista_secoes):
        conteudo = ''
        for i in lista_secoes:
            conteudo += i.getConteudo() + '/n'
        return conteudo
        
if __name__ == '__main__':
    ProxyLicitacao('*nomeLicitacao','*nomeArquivo','*dados')