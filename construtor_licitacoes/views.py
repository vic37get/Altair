from multiprocessing import context
from bson.objectid import ObjectId
import bson.json_util as json_util
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from utils import connectMongo
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

db_client = connectMongo('Altair')
def nova_licitacao(request,pk):
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    collection_template = db_client['template']
    collection_licitacao = db_client['licitacao']
    id = collection_licitacao.insert_one({'tituloArquivo':'Sem Título','id_template': pk,'dataCriação':datetime.now().strftime('%d/%m/%Y %H:%M')})
    template = collection_template.find_one({"_id":ObjectId(pk)})
    context = {
        'template':dict(template),
        'id_licitacao':id.inserted_id
    }
    #return HttpResponse(modelo.render(context, request))
    return redirect('/construcao/editarLicitacao/'+str(id.inserted_id))
    
def editar(request,pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    collection_template = db_client['template']
    template = collection_template.find_one({"_id":ObjectId(licitacao['id_template'])})
    context = {
        'template':dict(template),
        'licitacao':json_util.dumps(licitacao),
        'id_licitacao':licitacao['_id']
    }
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    return HttpResponse(modelo.render(context, request))

@csrf_exempt
def salvar(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        collection_licitacao.update_one({'_id':ObjectId(data['_id'])},{'$set':data['json']},upsert=True)
        #print(data['json'])
        #print(data['_id'])
    return HttpResponse()

def excluir(request,pk):
    collection_licitacao = db_client['licitacao']
    if request.method == 'POST':
        collection_licitacao.delete_one({"_id":ObjectId(pk)})
        context = {  
        }
        return redirect('/')

@csrf_exempt
def editarTitulo(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        collection_licitacao.update_one({'_id':ObjectId(data['_id'])},{'$set':data['json']},upsert=True)
        #print(data['json'])
        #print(data['_id'])
    return HttpResponse()

def enviar(request, pk):
    modelo = loader.get_template('construtor_licitacoes/enviar.html')
    return HttpResponse(modelo.render())
