from django.test import SimpleTestCase
from logic import RegraProxy as rule
import re,utils
from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo
from logic import Tokeniza
import base64

db = connectMongo('Altair')
class TestAlimentosCaros(SimpleTestCase):
    def test_AlimentosCaros(self):
        collection_licitacao = db['licitacao']
        licitacao = collection_licitacao.find_one({"_id":ObjectId('6318e79e47c026f220cd94f8')})

        fraudeTest = Tokeniza.Main().verificarAltair(licitacao)

        tipoDaFraude = fraudeTest[0].getTipoAchado()

        self.assertEquals('alimentos_caros',tipoDaFraude)

