from pymongo import MongoClient

def connectMongo(db_name):
    client = MongoClient('mongodb+srv://altair-admin-victor:ebgLlVUfbYr0EXfn@altair-nv.b4uqhas.mongodb.net/?retryWrites=true&w=majority&socketTimeoutMS=360000&connectTimeoutMS=360000')
    db = client[db_name]
    return db

def addRegra(database,regra):
    collections = database['regra']

def authenticate(user,password):
    db_client = connectMongo('Altair')
    collection_usuario = db_client['usuario']
    user_temp = collection_usuario.find_one({'userID':user,'senha':password})
    if user_temp != None:
        return [True,user_temp]
    else:
        return [False,None]

from django.contrib import messages
from django.shortcuts import redirect
def gestor_required(f):
     def verifica(request, *args, **kwargs):
          if request.session['cargo']!='Gestor':
            messages.info(request, 'Necessario logar como gestor')
            return redirect('/login')
          else:
               return f(request, *args, **kwargs)
     verifica.__doc__= f.__doc__
     verifica.__name__= f.__name__
     return verifica


def aud_required(f):
     def verifica(request, *args, **kwargs):
          if request.session['cargo']!='Auditor':
            messages.info(request, 'Necessario logar como auditor')
            return redirect('/login')
          else:
               return f(request, *args, **kwargs)
     verifica.__doc__= f.__doc__
     verifica.__name__= f.__name__
     return verifica
    
def login_required(f):
     def verifica(request, *args, **kwargs):
          if len(request.session.keys()) == 0:
            messages.info(request, 'Necessario relizar login')
            return redirect('/login')
          else:
               return f(request, *args, **kwargs)
     verifica.__doc__= f.__doc__
     verifica.__name__= f.__name__
     return verifica

def logged(f):
     def verifica(request, *args, **kwargs):
          if len(request.session.keys()) != 0:
               messages.info(request, 'Usuario: '+request.session['nome']+' já logado')
               if request.session['cargo']!='Auditor':
                    return redirect('/aud')
               if request.session['cargo']!='Gestor':
                    return redirect('/gestor')     
          else:
               return f(request, *args, **kwargs)
     verifica.__doc__= f.__doc__
     verifica.__name__= f.__name__
     return verifica