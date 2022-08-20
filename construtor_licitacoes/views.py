from bson.objectid import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo

db_client = connectMongo('Altair')
def nova_licitacao(request,pk):
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    collection_template = db_client['template']
    template = collection_template.find_one({"_id":ObjectId(pk)})
    context = {
        'template':dict(template)
    }
    return HttpResponse(modelo.render(context, request))
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def salvar(request):
    if request.method == 'POST':
        collection_template = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        collection_template.insert_one(data)
        print(data['secoes'])
    return HttpResponse()
