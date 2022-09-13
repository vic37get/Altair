import base64
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
    licitacoes = collection_licitacao.find({})
    print(licitacoes[0])
    #licitacoes = list(map(binarytoStr,licitacoes))
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

def verificar(request,pk):
    from logic import Tokeniza,Header
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    tam = int(request.GET['tamanho'])
    if int(request.GET['tamanho']) <= 0:
        tam = 0
    Header.CONTEXTO_FIM,Header.CONTEXTO_INI = tam,tam
    verificadorFraude = Tokeniza.Main().verificarAltair(licitacao)
    achados = []
    for i in verificadorFraude:
            if i.getConteudoAchado() != '':
                achados.append(i)
    achados = [i.__dict__ for i in achados]
    licitacao['achados'] = achados
    collection_licitacao.update_one({'_id':ObjectId(pk)},{'$set':licitacao},upsert=True)
    context = {
        'licitacao':licitacao['base64'],
        'licitacao_dados': licitacao
    }
    modelo = loader.get_template('verificador_fraude/avaliar.html')
    return HttpResponse(modelo.render(context, request))
