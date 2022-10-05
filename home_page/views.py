from multiprocessing import context

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from utils import authenticate, connectMongo, gestor_required, login_required,POST_required
from data.licitacaoBD import insertLic, findallLic, findOneLic, findLicByDataAndId, findLicsDados, updateOneLic, deleteLic  
from data.usuarioBD import insertUser, searchAuthenticateUser, findOneUser, findOneUserDirect, updateUser
from data.templatesBD import findAllTemplates, findTemplateById, findOneTemplate
from data.avaliacaoBD import insertAvalic

db_client = connectMongo('Altair')

@login_required
@gestor_required
def index(request):
    template = loader.get_template('home_page/index.html')
    licitacoes = findLicsDados({'id_author':str(request.session['id'])})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

@login_required
def alterarSenha(request):
    context = {
    }
    alterar_senha = loader.get_template('home_page/alterarSenha.html')
    return HttpResponse(alterar_senha.render(context, request))

@login_required
def alteracaoDeSenha(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        usuario = findOneUser(request.session['id'])
        updateUser(request.session['id'], data)
        messages.info(request, 'A senha do usuário \''+usuario['nome']+'\' foi alterada!')
    return redirect('/gestor')

@login_required
def perfil(request):
    context = {
        'usuario': request.session['username'],
        'email': request.session['email'],
        'cargo': request.session['cargo'],
        'nome':  request.session['nome'],
    }
    perfil = loader.get_template('home_page/perfil.html')
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
    return redirect('/gestor')

@login_required
@gestor_required
def modelo(request):
    modelo = loader.get_template('construtor_licitacoes/modelos.html')
    templates = findAllTemplates()
    context = {
        'templates':templates
    }
    return  HttpResponse(modelo.render(context, request))

@login_required
@gestor_required  
def filtro(request):
    home = loader.get_template('home_page/index.html')
    status = int(request.GET['status'])
    template = request.GET['template']
    tituloArquivo = request.GET['tipoArquivo']
    pesquisa = dict()
    if status != -1:
        pesquisa['status'] = status
    if template != '-1':
        template  = findOneTemplate({'nome':template}, {'_id':1})
        pesquisa['id_template'] = str(template['_id'])
    if tituloArquivo != '':
        pesquisa['tituloArquivo'] = {'$regex':tituloArquivo,'$options':'i'}
    pesquisa['id_author'] = request.session['id']
    licitacoes = findLicsDados(pesquisa)
    context = {
        'licitacoes': licitacoes
    }
    return HttpResponse(home.render(context, request))