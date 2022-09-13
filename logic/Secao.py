from logic import Header

class Secao:
    def __init__(self,numero, titulo, conteudo,completo):
        self.numero = numero
        self.titulo = titulo
        self.conteudo = conteudo
        self.completo = completo
        self.tipo = None
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def getConteudo(self):
        return self.conteudo
    
    def setConteudo(self, conteudo):
        self.conteudo = conteudo
    
    def getNumeracao(self):
        return self.numero
    
    def setNumeracao(self,numeracao):
        self.numeracao = numeracao

    def isEmpty(self):
        if len(self.getConteudo()) == 0:
            return True
        return False

    def __str__(self):
        return self.titulo

    def verificaSecao(self):
        for i in Header.SECOES:
            if i.search(self.getTitulo())[0]:
                self.setTipo(i.getNome())
                break
        if self.getTipo() == None:
            self.setTipo(Header.TIPOS['OUTROS'])