from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from pymongo import MongoClient
from utils import connectMongo

db_client = connectMongo('Altair')

def index(request):
    template = loader.get_template('home_page/index.html')
    collection = db_client['comments']
    users = collection.find({})
    context = {
        'usuarios':users
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
