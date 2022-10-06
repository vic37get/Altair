from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from utils import authenticate, connectMongo, logged, login_required
from data.licitacaoBD import insertLic, findallLic, findOneLic, findLicByDataAndId, findLicsDados, updateOneLic, deleteLic  
from data.usuarioBD import insertUser, searchAuthenticateUser, findOneUser, findOneUserDirect, updateUser
from data.templatesBD import findAllTemplates, findTemplateById, findOneTemplate
from data.avaliacaoBD import insertAvalic

@login_required
@logged
def home(request):
    home = loader.get_template('home_all/home.html')
    return HttpResponse(home.render({}, request))

def login(request):
    del request.session
    login = loader.get_template('home_all/homeLogin.html')
    return HttpResponse(login.render({}, request))

@login_required
def logout(request):
    request.session['logged'] = False
    return redirect('/login')

def loginAuth(request):
    if request.method == "POST":
        dados_usuario = request.POST.copy()
        del dados_usuario['csrfmiddlewaretoken']
        isExists,user = authenticate(dados_usuario['usuario'],dados_usuario['senha'])
        request.session['logged'] = False
        if isExists:
            request.session['username'] =user['userID']
            request.session['email'] = user['email']
            request.session['id'] = str(user['_id'])
            request.session['cargo'] = user['cargo']
            request.session['nome'] = user['nome']
            request.session['logged'] = True
            if(request.session['cargo'] == 'Gestor'):
                return redirect('/gestor')
            elif(request.session['cargo'] == 'Auditor'):
                return redirect('/aud')
        else:
            messages.info(request, 'Usuario ou senha incorretos')
            return redirect('/login')


def cadastro(request):
    cadastro = loader.get_template('home_all/homeCadastro.html')
    return HttpResponse(cadastro.render({}, request))

def submeterCadastro(request):
    if request.method == "POST":
        dados_usuario = request.POST.copy()
        del dados_usuario['csrfmiddlewaretoken']
        busca = findOneUserDirect({'userID': dados_usuario['usuario']})
        if busca == None:
            messages.info(request, 'Usuário \''+dados_usuario['usuario']+'\' cadastrado com sucesso!')
            insertUser({'userID': dados_usuario['usuario'], 'nome':dados_usuario['nome'],'cargo': dados_usuario['cargo'],'email':dados_usuario['email'],'senha': dados_usuario['senha']})
            return redirect('/login')
        else:
            messages.info(request, 'Ação invalida, usuário: \''+busca['userID']+'\' já existe!')
            return redirect('/cadastro')