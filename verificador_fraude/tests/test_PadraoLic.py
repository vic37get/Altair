from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo
from logic import Tokeniza

db = connectMongo('Altair')


##teste para recusar arquivo que não está no padrão - sem seções
class TestPadraoLic(SimpleTestCase):
    def test_PadraoLic(self):
        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":'teste nao passa',
            "interno": False,
            "status":0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"",
            "avaliada": 1,
            "content": """2.1 - Poderá participar desta licitação toda e qualquer firma individual ou sociedade
                        regularmente estabelecida no País, que seja especializada e credenciada no fornecimento
                        dos referidos bens, e que satisfaça a todas as exigências do presente Edital, espe cificações
                        e normas, de acordo com os anexos relacionados.
                        2.2 - É vedada a formação de consórcios para participação desta licitação.
                        Página | 3 2.3 - Não poderão participar desta licitação, as empresas declaradas inidôneas e impedidas
                        de contratar com a Administraç ão Municipal.
                        2.4 - A licitante desejando apresentar preposto deverá fazê -lo mediante um único
                        representante, que deverá se identificar no ato da abertura da licitação, através de
                        procuração pública ou particular, outorgando amplos poderes para o mandatári o
                        representar a licitante nesta licitação.
                        2.5 - As empresas interessadas deverão apresentar toda documentação exigida para
                        o cadastro de fornecedores municipal em até 03 (três) dia antes da abertura do
                        processo licitatório no qual será entregue o certifi cado de fornecedor municipal sob
                        pena de desclassificação.
                        3.0 - APRESENTAÇÃO DOS ENVELOPES
                        3.1 - As empresas interessadas deverão entregar a Comissão de Licitação no local e hora
                        já apontados no preâmbulo do presente Edital em envelopes devidamente separa dos,
                        lacrados e indevassáveis, contendo em sua parte frontal, além da razão social, os dizeres
                        datilografados:
                        a) O ENVELOPE 1 contendo os documentos relativos à habilitação que terá
                        no frontispício os seguintes dizeres:
                        À PREFEITURA MUNICIPAL DE DOMINGOS MOURÃO
                        COMISSÃO PERMANENTE DE LICITAÇÃO
                        TOMADA DE PREÇO Nº 001/2022
                        “DOCUMENTOS DE HABILITAÇÃO”
                        Deverá conter também o nome e o endereço da empresa licitante.
                        b) O ENVELOPE 2 contendo as propostas de preço que terá no frontispício
                        os seguintes dizeres:
                        À PREFEITURA MUNICIPAL DE DOMINGOS MOURÃO
                        COMISSÃO PERMANENTE DE LICITAÇÃO
                        TOMADA DE PREÇO Nº 001/2022
                        “DOCUMENTOS DE PROPOSTA DE PREÇOS”
                        Deverá conter também o nome e endereço da empresa licitante.
                        Página | 4
                        4.0 – DA HABILITAÇÃO
                        4.1 – Para se habilitarem na presente Licitação Tomada de Preços, os interessados deverão
                        apresentaros documentos abaixo relacionados através de seus representantes, no local,
                        data e horários indicados no preâmbulo deste Edital, em envelope inteiramente fechado,
                        contendo em sua parteexterna, além da razão social e endereço da licitante, os seguintes
                        dizeresdo 3.1 A
                        4.1.1 – Será obrigatória a apresentação do Certificado de Registro Cadastral de
                        Fornecedores /Prestadores de Serviçosdo Município de Domingos Mourão- PI, expedido
                        pela C omissão Permanente de Licitação deste."""
        })
        licitacao = collection_licitacao.find_one({'_id':ObjectId(id.inserted_id)})

        testeRecusa = Tokeniza.Main().verificarValidade(licitacao)
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})

        self.assertEquals(False,testeRecusa)

        
