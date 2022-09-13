import re
from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo
from logic import LicitacaoProxy,Secao

db = connectMongo('Altair')
class Verificardor(SimpleTestCase):

    def test_licitacoes(self):
        sec1 = {'titulo':'',
        'conteudo':''}
        sec2 = {'titulo':'',
        'conteudo':''}
        sec3 = {'titulo':'',
        'conteudo':''}
        secoes = [sec1,sec2,sec3]
        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":"TESTE VERIFICAR",
            "status":0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"",
            "secoes":secoes,
        })
        licitacoes = collection_licitacao.find({'_id':ObjectId(id.inserted_id)})
        licitacao_Obj = LicitacaoProxy.ProxyLicitacao("",licitacoes['tituloArquivo'],"")
        #Necessita Interface Aqui
        for i in licitacoes['secoes'].items():
            #Necessita conversão de base64 para String
            secao = Secao.Secao(i['titulo'],i['conteudo'])
            #Exemplo da adaptação
            licitacao_Obj.setSecoes(secao)
        #-------------------
        self.assertIsNotNone(licitacoes)