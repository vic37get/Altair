import base64
import json

import bson.json_util as json_util
from bson.binary import Binary
from bson.objectid import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo

db_client = connectMongo('Altair')

def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    def binarytoStr(element):
        element['base64'] = Binary(element['base64']).decode()
        return element
    licitacoes = list(licitacoes)
    licitacoes = list(map(binarytoStr,licitacoes))
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

def filtroVerificador(request):
    collection_licitacao = db_client['licitacao']
    verificador = loader.get_template('verificador_fraude/homeAud.html')

    avaliada = int(request.GET['avaliada'])
    tipo = request.GET['tipo']
    tituloArquivo = request.GET['NomeLicitação']

    pesquisa = dict()
    if tipo != '-1':
        pesquisa['tipo'] = tipo

    if avaliada != -1:
        pesquisa['avaliada'] = avaliada

    if tituloArquivo != '':
        pesquisa['tituloArquivo'] = {'$regex':tituloArquivo,'$options':'i'}
    licitacoes = collection_licitacao.find(pesquisa)
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(verificador.render(context, request))
