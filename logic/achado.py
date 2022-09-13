class Achado:
    def _init_(self, tipoAchado, secaoAchado, conteudoAchado, descricaoAchado):
        self.tipoAchado = tipoAchado
        self.secaoAchado = secaoAchado
        self.conteudoAchado = conteudoAchado
        self.descricaoAchado = descricaoAchado
    
    def getTipoAchado(self):
        return self.tipoAchado
    
    def setTipoAchado(self, tipoAchado):
        self.tipoAchado = tipoAchado
    
    def getSecaoAchado(self):
        return self.secaoAchado
    
    def setSecaoAchado(self, secaoAchado):
        self.secaoAchado = secaoAchado

    def getConteudoAchado(self):
        return self.conteudoAchado
    
    def setConteudoAchado(self, conteudoAchado):
        self.conteudoAchado = conteudoAchado
    
    def getDescricaoAchado(self):
        return self.descricaoAchado
    
    def setDescricaoAchado(self, descricaoAchado):
        self.descricaoAchado = descricaoAchado