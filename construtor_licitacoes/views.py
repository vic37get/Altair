import json
from datetime import datetime
from email import message
from multiprocessing import context

import bson.json_util as json_util
from bson.binary import Binary
from bson.objectid import ObjectId
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import connectMongo, gestor_required, login_required

db_client = connectMongo('Altair')

@login_required
@gestor_required
def nova_licitacao(request,pk):
    collection_licitacao = db_client['licitacao']
    id = collection_licitacao.insert_one({'tituloArquivo':'Sem Título', 'achados':[], 'avaliada':0,'base64': Binary(''.encode()), 'status':0, 'id_template': pk,'dataCriação':datetime.now().strftime('%d/%m/%Y %H:%M'),'id_author':str(request.session['id'])})
    return redirect('/gestor/construcao/editarLicitacao/'+str(id.inserted_id))

@login_required
@gestor_required
def editar(request,pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    if(licitacao['status']!=0):
        messages.info(request, 'Ação invalida, licitação: \''+licitacao['tituloArquivo']+'\' já submetida')
        return redirect('/gestor')
    collection_template = db_client['template']
    template = collection_template.find_one({"_id":ObjectId(licitacao['id_template'])})
    context = {
        'template':dict(template),
        'licitacao':json_util.dumps(licitacao),
        'id_licitacao':licitacao['_id']
    }
    modelo = loader.get_template('construtor_licitacoes/adicionar.html')
    return HttpResponse(modelo.render(context, request))

@csrf_exempt
@login_required
@gestor_required
def salvar(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        data['json']['base64'] = Binary(data['json']['base64'].encode())
        collection_licitacao.update_one({'_id':ObjectId(data['_id'])},{'$set':data['json']},upsert=True)
    return HttpResponse()

@login_required
@gestor_required
def excluir(request,pk):
    collection_licitacao = db_client['licitacao']
    if request.method == 'POST':
        licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)},{'status', 'tituloArquivo'})
        if licitacao['status'] != 0:
            messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' não pôde ser excluída')
            return redirect('/gestor')
        messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' foi excluída!')
        collection_licitacao.delete_one({"_id":ObjectId(pk)})
        return redirect('/gestor')

@csrf_exempt
@login_required
@gestor_required
def editarTitulo(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = json.loads(request.body.decode('utf-8'))
        collection_licitacao.update_one({'_id':ObjectId(data['_id'])},{'$set':data['json']},upsert=True)
    return HttpResponse()

@login_required
@gestor_required
def enviarConstrucao(request, pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    context = {
        'licitacao':licitacao,
        'id_licitacao':licitacao['_id']
    }
    modelo = loader.get_template('construtor_licitacoes/enviarConstrucao.html')
    return HttpResponse(modelo.render(context, request))


@login_required
@gestor_required
def salvarFormulario(request, pk):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = request.POST.copy()
        data['status'] = 1
        data['avaliada'] = 0
        del data['csrfmiddlewaretoken']
        licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)},{'status', 'tituloArquivo'})
        collection_licitacao.update_one({'_id':ObjectId(pk)},{'$set':data},upsert=True)
        messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' foi enviada!')
    return redirect('/gestor')

@login_required
@gestor_required
def enviar(request):
    modelo = loader.get_template('construtor_licitacoes/enviarGeral.html')
    context = {
    }
    return HttpResponse(modelo.render(context, request))

@login_required
@gestor_required
def enviarGeral(request):
    if request.method == 'POST':
        collection_licitacao = db_client['licitacao']
        data = request.POST
        arquivo = request.FILES['arquivopdf'].read()
        bytespdf = base64.b64encode(arquivo)
        id = collection_licitacao.insert_one({'tituloArquivo':'Sem Título','id_template': '62fa7d2fa15dc0d036b941fd','dataCriação':datetime.now().strftime('%d/%m/%Y %H:%M'), 'dataModificacao':datetime.now().strftime('%d/%m/%Y %H:%M'), 'base64': bytespdf, 'status': 1, 'orgao': data['orgao'], 'municipio': data['municipio'], 'estado': data['estado'], 'tipo': data['tipo'],  'objeto': data['objeto'], 'data': data['data']})
    return redirect('/gestor')    

    
#sudo apt-get install libpangocairo-1.0-0
import base64

import weasyprint


#pip install django-easy-pdf
#django-easy-pdf>=0.2.0 and WeasyPrint>=0.34
@csrf_exempt
@login_required
@gestor_required
def toPDF(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pdf = weasyprint.HTML(string=data['contentPDF']).write_pdf()
        pdf = base64.b64encode(pdf)
        #open(os.path.join(os.getcwd(),'construtor_licitacoes','tests','google.pdf'), 'wb').write(pdf)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename=sample_pdf.pdf"
        return response
