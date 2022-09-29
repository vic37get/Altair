from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from utils import login_required
from django.contrib import messages
from utils import authenticate, connectMongo,login_required,logged

db_client = connectMongo('Altair')

@login_required
def home(request):
    home = loader.get_template('home_all/home.html')
    return HttpResponse(home.render({}, request))

def login(request):
    login = loader.get_template('home_all/homeLogin.html')
    return HttpResponse(login.render({}, request))

@login_required
def logout(request):
    del request.session
    return redirect('/login')

def loginAuth(request):
    if request.method == "POST":
        #collection_usuario = db_client['usuario']
        dados_usuario = request.POST.copy()
        del dados_usuario['csrfmiddlewaretoken']
        isExists,user = authenticate(dados_usuario['usuario'],dados_usuario['senha'])
        request.session['logged'] = False
        if isExists:
            request.session['username'] =user['userID']
            request.session['email'] = user['email']
            request.session['id'] = user['_id']
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