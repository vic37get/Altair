from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pymongo import MongoClient
from utils import connectMongo
from fpdf import FPDF

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter

db_client = connectMongo('sample_mflix')

def index(request):
    template = loader.get_template('home_page/index.html')
    collection = db_client['comments']
    users = collection.find({})
    context = {
        'usuarios':users
    }
    return HttpResponse(template.render(context, request))

def modelo(request):
    template = loader.get_template('construtor_licitacoes/modelos.html')
    return  HttpResponse(template.render({}, request))
