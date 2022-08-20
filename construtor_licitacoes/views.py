from multiprocessing import context
from bson.objectid import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo
from django.views.decorators.csrf import csrf_exempt
import json

db_client = connectMongo('Altair')
def nova_licitacao(request,pk):
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    collection_template = db_client['template']
    collection_licitacao = db_client['licitacao']
    id = collection_licitacao.insert_one({})
    template = collection_template.find_one({"_id":ObjectId(pk)})
    context = {
        'template':dict(template),
        'id_licitacao':id.inserted_id
    }
    return HttpResponse(modelo.render(context, request))

def editar(request,pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    context = {
        'licitacao':dict(licitacao)
    }
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    return HttpResponse(modelo.render(context, request))

@csrf_exempt
def salvar(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        collection_licitacao.update_one({'_id':ObjectId(data['_id'])},{'$set':data['json']},upsert=True)
        print(data['json'])
        print(data['_id'])
    return HttpResponse()
