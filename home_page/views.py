from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo

db_client = connectMongo('Altair')

def index(request):
    template = loader.get_template('home_page/index.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

def modelo(request):
    modelo = loader.get_template('construtor_licitacoes/modelos.html')
    collection = db_client['template']
    templates = collection.find({})
    context = {
        'templates':templates
    }
    return  HttpResponse(modelo.render(context, request))

def enviar(request):
    modelo = loader.get_template('home_page/enviar.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(modelo.render(context, request))
    
def filtro(request):
    collection_licitacao = db_client['licitacao']
    home = loader.get_template('home_page/index.html')

    status = int(request.GET['status'])
    template = request.GET['template']
    tituloArquivo = request.GET['tipoArquivo']

    pesquisa = dict()
    if status != -1:
        pesquisa['status'] = status
    if template != '-1':
        collection_template = db_client['template']
        template_banco = collection_template.find_one({'nome':template},{'_id':1})
        pesquisa['id_template'] = str(template_banco['_id'])
    if tituloArquivo != '':
        pesquisa['tituloArquivo'] = {'$regex':tituloArquivo,'$options':'i'}
    licitacoes = collection_licitacao.find(pesquisa)
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(home.render(context, request))
    
def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

