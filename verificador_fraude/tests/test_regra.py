from django.test import SimpleTestCase
from logic import RegraProxy as rule
import re

class RegraTest(SimpleTestCase):
    def test_search_caso_somente_positivo(self):
        regra = rule.RegraProxy('def1_teste#41',re.compile(r'certid[ãa]o'))
        self.assertEqual(regra.search('de acordo com a certidao')[1],True)
    def test_search_caso_positivoEnegativo(self):
        regra = rule.RegraProxy('def2_teste#41',re.compile(r'certid[ãa]o'))
        regra.setRegexNegativos([re.compile(r'certid[ãa]o protesto')])
        self.assertEqual(regra.search('de acordo com a certidao')[1],True)
        self.assertEqual(regra.search('de acordo com a certidao protesto')[1],False)