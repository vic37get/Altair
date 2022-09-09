import base64
import re
from email.mime import base

from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo

db = connectMongo('Altair')
class ExtraçãoTextoTest(SimpleTestCase):

    def test_licitacoes(self):
        collection_licitacao = db['licitacao']
        licitacoes = collection_licitacao.find({})
        self.assertIsNotNone(licitacoes)

    def test_secoes(self):
        lista_secoes = []
        conteudo_secao = []
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId('6318e79e47c026f220cd94f8')})
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
    
    def test_ExtrairCabecalho(self):
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId('6318e79e47c026f220cd94f8')})
        exp_html = re.compile('<.*?>')
        try:
            cabecalho = base64.b64decode(licitacao['cabecalho']).decode('ISO-8859-1')
            cabecalho = re.sub(exp_html, '', cabecalho)
            
        except:
            cabecalho = ''

        self.assertEquals(cabecalho, 'PREFEITURA DE TERESINA')
    
    def test_structBank(self):
        texto = []
        lista_secoes, conteudo_secao = self.test_secoes()
        for conteudos in zip(lista_secoes, conteudo_secao):
            texto.append(conteudos)
        self.assertNotEqual(len(texto), 0)
    
    def test_getTitulo(self):
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId('6318e79e47c026f220cd94f8')})
        exp_html = re.compile('<.*?>')
        titulo = ''
        titulo = base64.b64decode(licitacao['secoes'][0]['titulo']).decode('ISO-8859-1')
        titulo = re.sub(exp_html, '', titulo)
        self.assertNotEqual(titulo, '')
