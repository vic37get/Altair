from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo

db = connectMongo('Altair')
class ExtraçãoTextoTest(SimpleTestCase):

    def test_licitacoes(self):
        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":'PREFEITURA DE TERESINA',
            "status": 0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"PREFEITURA DE TERESINA",
        })  
        licitacoes = collection_licitacao.find({})
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})
        self.assertIsNotNone(licitacoes)

    def test_secoes(self):
        secao_um = {'titulo':'HABILITACAO',
        'conteudo':'habilitação conteudo'}
        secao_dois = {'titulo':'OBJETO',
        'conteudo':'objeto conteudo'}
        secoes = [secao_um,secao_dois]
        collection_licitacao = db['licitacao']

        id = collection_licitacao.insert_one({
            "tituloArquivo":'PREFEITURA DE TERESINA',
            "status": 0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"PREFEITURA DE TERESINA",
            "secoes": secoes
        })
        licitacao = collection_licitacao.find_one({'_id':ObjectId(id.inserted_id)})
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})
        lista_secoes = []
        conteudo_secao = []

        for i  in range(len(licitacao['secoes'])):
            titulo = ''
            titulo = (licitacao['secoes'][i]['titulo'])
            lista_secoes.append(titulo)
            
            conteudo = ''
            conteudo = (licitacao['secoes'][i]['conteudo'])
            conteudo_secao.append(conteudo)
        
        self.assertNotEqual(len(conteudo_secao[0]), 0)
        self.assertNotEqual(len(lista_secoes[1]), 0)

        return lista_secoes, conteudo_secao
    
    def test_ExtrairCabecalho(self):

        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":'TesteCabecalho',
            "status": 0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"PREFEITURA DE TERESINA",
        })
        licitacao = collection_licitacao.find_one({'_id':ObjectId(id.inserted_id)})
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})
        
        try:
            cabecalho = licitacao['cabecalho']
        except:
            cabecalho = ''

        self.assertEquals(cabecalho, 'PREFEITURA DE TERESINA')
    
    def test_getTitulo(self):
        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":'TesteTitulo',
            "status": 0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"PREFEITURA DE TERESINA",
        })
        licitacao = collection_licitacao.find_one({'_id':ObjectId(id.inserted_id)})
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})
        try:
            titulo = licitacao['tituloArquivo']
        except:
            titulo = ''

        self.assertNotEqual(titulo, '')