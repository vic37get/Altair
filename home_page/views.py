from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from utils import connectMongo
from django.contrib.auth.forms import UserCreationForm  


db_client = connectMongo('Altair')

def InicialLogin(request):
    login = loader.get_template('home_page/login.html')
    context = {

    }
    return HttpResponse(login.render(context, request))

def login(request):
    #verifica login
    
    logged = True # se existe usuario e senha no banco certinho
    if (logged):
        request.session.set('logged', True)
        request.session.set('username', banco.username)
        request.session.set('name', banco.name)
        request.session.set('id', banco.id)
        return 
    else: 
        return #render #'login',{'errorMessage':'Usuario ou senha incorretos'}

def qualquer_coisa(request):
    # so pra mostrar como usa
    id = request.session.get('id') # ai tuy joga em algum lugar, exemplo:
    licitacao.criador = id

def logoff_incomplete(request):
    # desliga
    request.session.destroy()
    return #redirect 'index'

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

def cadastrarUsuario(request):
    modelo = loader.get_template('home_page/cadastro.html')
    context={

    }
    return HttpResponse(modelo.render(context, request))

def submeterCadastro(request):
    if request.method == "POST":
        collection_usuario = db_client['usuario']
        dados_usuario = request.POST.copy()
        del dados_usuario['csrfmiddlewaretoken']
        busca = collection_usuario.find_one({'userID': dados_usuario['usuario']})
        if busca == None:
            messages.info(request, 'Usuário \''+dados_usuario['usuario']+'\' cadastrado com sucesso!')
            collection_usuario.insert_one({'userID': dados_usuario['usuario'], 'nome':dados_usuario['nome'],'cargo': dados_usuario['cargo'],'email':dados_usuario['email'],'senha': dados_usuario['senha']})
            return redirect('/')
        else:
            messages.info(request, 'Ação invalida, usuário: \''+busca['userID']+'\' já existe!')
            print('Usuário já existe')
            return redirect('/cadastrarUsuario')
    




    
