from django.test import SimpleTestCase
from logic import RegraProxy as rule
import re,utils
from bson.objectid import ObjectId

db_client = utils.connectMongo('Altair')
class RegraTest(SimpleTestCase):
    def test_search_caso_somente_positivo(self):
        regra = rule.RegraProxy('def1_teste#41',re.compile(r'certid[ãa]o'))
        self.assertEqual(regra.search('de acordo com a certidao')[1],True)
    def test_search_caso_positivoEnegativo(self):
        regra = rule.RegraProxy('def2_teste#41',re.compile(r'certid[ãa]o'))
        regra.setRegexNegativos([re.compile(r'certid[ãa]o protesto')])

        self.assertEqual(regra.search('de acordo com a certidao')[1],True)
        self.assertEqual(regra.search('de acordo com a certidao protesto')[1],False)
    def test_save_toJson(self):
        regra = rule.RegraProxy('',re.compile(r'a',flags=re.IGNORECASE))
        regra.setRegexNegativos([re.compile(r'a b',flags=re.I|re.DOTALL)])

        collections_regra = db_client['regra']
        id = collections_regra.insert_one(regra.toJson())

        regra_mongo = dict(collections_regra.find_one({"_id":ObjectId(id.inserted_id)}))
        dicts_regra_classe = dict(regra.toJson())
        dicts_regra_classe["_id"] = ObjectId(id.inserted_id)

        collections_regra.delete_one({"_id":ObjectId(id.inserted_id)})
        self.assertEqual(dicts_regra_classe.__eq__(dict(regra_mongo)),True)
    
    def test_load_loadJson(self):
        # Grade falha de segurança uso do eval
        regra = rule.RegraProxy('',re.compile(r'a',flags=re.IGNORECASE))
        regra.setRegexNegativos([re.compile(r'a b',flags=re.I|re.DOTALL)])

        collections_regra = db_client['regra']
        id = collections_regra.insert_one(regra.toJson())
        regra_mongo = dict(collections_regra.find_one({"_id":ObjectId(id.inserted_id)}))
        regra = rule.RegraProxy()
        regra.loadJson(regra_mongo)

        self.assertEqual(regra.search('a')[1],True)
        self.assertEqual(regra.search('a bc')[1],False)
        