from email.mime import base
from django.test import SimpleTestCase
from utils import connectMongo
from bson.objectid import ObjectId
import base64
import re


db = connectMongo('Altair')
class ExtraçãoTextoTest(SimpleTestCase):

    def test_licitacoes(self):
        collection_licitacao = db['licitacao']
        licitacoes = collection_licitacao.find({})
        self.assertIsNotNone(licitacoes)

    def test_secoes(self):
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId('63175236a996a9d6f805e57d')})
        exp_html = re.compile('<.*?>')
        texto = licitacao['secoes'][0]['titulo']
        texto = base64.b64decode(texto).decode('ISO-8859-1')
        texto_limpo = re.sub(exp_html, '', texto)
        print(texto)
        print(texto_limpo)
        
