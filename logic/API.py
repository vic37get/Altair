from logic import Secao
import base64,re
import html
class API:
    def __init__(self):
        ...
    def decodeb64(self,dado):
        if(type(dado)==list):
            dado = dado[0]
        return html.unescape(base64.b64decode(dado).decode('ISO-8859-1'))
    def extract(self,b64):
        return re.sub(re.compile('<.*?>'),'',b64)
    def APISecao(self,titulo, conteudo):
        return Secao.Secao("",self.extract(self.decodeb64(titulo)),self.extract(self.decodeb64(conteudo)),"")
        