from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo

db_client = connectMongo('Altair')

def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))
