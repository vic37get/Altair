from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('homeAll/homeLogin.html')
    return HttpResponse(template.render({}, request))

def redirectHome(request):
    return redirect('home/')