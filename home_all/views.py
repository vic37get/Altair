from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

def home(request):
    home = loader.get_template('home_all/home.html')
    return HttpResponse(home.render({}, request))

def login(request):
    login = loader.get_template('home_all/homeLogin.html')
    return HttpResponse(login.render({}, request))

def cadastro(request):
    cadastro = loader.get_template('home_all/homeCadastro.html')
    return HttpResponse(cadastro.render({}, request))

def redirectHome(request):
    return redirect('home/')

def submeterCadastro(request):
    pass