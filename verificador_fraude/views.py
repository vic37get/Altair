import json

import bson.json_util as json_util
from bson.objectid import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo

db_client = connectMongo('Altair')

def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    collection_licitacao = db_client['licitacao']
    def binarytoStr(field):
        return str(field['base64'])
    licitacoes = collection_licitacao.find({})
    #licitacoes = list(map(binarytoStr,licitacoes))
    #print(licitacoes[0]['base64'])
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

def avaliar(request,pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    context = {
        'licitacao':licitacao['base64'],
        'licitacao_dados': licitacao
    }
    modelo = loader.get_template('verificador_fraude/avaliar.html')
    return HttpResponse(modelo.render(context, request))
