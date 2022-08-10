from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def nova_licitacao(request):
    template = loader.get_template('construtor_licitacoes/adicionar.html')
    return HttpResponse(template.render({}, request))
