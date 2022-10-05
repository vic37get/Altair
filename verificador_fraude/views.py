import base64
import json

import bson.json_util as json_util
from bson.binary import Binary
from bson.objectid import ObjectId
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from utils import aud_required, connectMongo, login_required, GET_required
from data.licitacaoBD import insertLic, findallLic, findOneLic, findLicByDataAndId, findLicsDados, updateOneLic, deleteLic  
from data.usuarioBD import insertUser, searchAuthenticateUser, findOneUser, findOneUserDirect, updateUser
from data.templatesBD import findAllTemplates, findTemplateById, findOneTemplate
from data.avaliacaoBD import insertAvalic

db_client = connectMongo('Altair')

@login_required
@aud_required
def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    licitacoes = findallLic()
    def binarytoStr(element):
        element['base64'] = Binary(element['base64']).decode()
        return element
    licitacoes = list(licitacoes)
    licitacoes = list(map(binarytoStr,licitacoes))
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

@login_required
def perfil(request):
    context = {
        'usuario': request.session['username'],
        'email': request.session['email'],
        'cargo': request.session['cargo'],
        'nome':  request.session['nome'],
    }
    perfil = loader.get_template('verificador_fraude/perfil.html')
    return HttpResponse(perfil.render(context, request))

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        request.session['username'] = data['usuario']
        request.session['email'] = data['email']
        request.session['nome'] = data['nome']
        usuario = findOneUser(request.session['id'])
        updateUser(request.session['id'], data)
        messages.info(request, 'Os dados do usuário \''+usuario['nome']+'\' foram alterados!')
    return redirect('/aud')

@login_required
def alterarSenha(request):
    context = {
    }
    alterar_senha = loader.get_template('verificador_fraude/alterarSenha.html')
    return HttpResponse(alterar_senha.render(context, request))

@login_required
def alteracaoDeSenha(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        usuario = findOneUser(request.session['id'])
        updateUser(request.session['id'], data)
        messages.info(request, 'A senha do usuário \''+usuario['nome']+'\' foi alterada!')
    return redirect('/aud')

@login_required
@aud_required
def avaliar(request,pk):
    licitacao = findOneLic(pk)
    context = {
        'licitacao':licitacao['base64'],
        'licitacao_dados': licitacao
    }
    modelo = loader.get_template('verificador_fraude/avaliar.html')
    return HttpResponse(modelo.render(context, request))

@login_required
@aud_required
@GET_required
def filtroVerificador(request):
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
    licitacoes = findLicsDados(pesquisa)
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(verificador.render(context, request))

@login_required
@aud_required
@GET_required
def verificar(request,pk):
    from logic import Header, Tokeniza
    licitacao = findOneLic(pk)
    tam = int(request.GET['tamanho'])
    if int(request.GET['tamanho']) <= 0:
        tam = 0
    Header.CONTEXTO_FIM,Header.CONTEXTO_INI = tam,tam
    if licitacao['interno']:
        verificadorFraude = Tokeniza.Main().verificarAltair(licitacao)
    else:
        verificadorFraude = Tokeniza.Main().verificarAltairExt(licitacao)
    achados = []
    for i in verificadorFraude:
            if i.getConteudoAchado() != '':
                achados.append(i)
    achados = [i.__dict__ for i in achados]
    licitacao['achados'] = achados
    updateOneLic(pk, licitacao)
    context = {
        'licitacao':licitacao['base64'],
        'licitacao_dados': licitacao
    }
    modelo = loader.get_template('verificador_fraude/avaliar.html')
    return HttpResponse(modelo.render(context, request))

@login_required
@aud_required
@GET_required
def avalicao(request,pk):
    data = request.GET.copy()
    del data['csrfmiddlewaretoken']
    data['_idLicitacao'] = pk
    insertAvalic(dict(data))
    updateOneLic(pk, {'avaliada': 1,'comentarios':data['comentarios']})
    messages.info(request,'Avaliação registrada')
    return redirect('/aud/avaliar/'+pk)