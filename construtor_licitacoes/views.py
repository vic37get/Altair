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
from utils import connectMongo, gestor_required, login_required,POST_required,GET_required
import base64,weasyprint
from logic.convertPDF import b64tPDF,pdf2txt,DEFAULT_FOLDER_PDF,DEFAULT_FOLDER_TXT,base_dir,extern_pdf_content
from data.licitacaoBD import insertLic, findallLic, findOneLic, findLicByDataAndId, findLicsDados, updateOneLic, deleteLic  
from data.usuarioBD import insertUser, searchAuthenticateUser, findOneUser, findOneUserDirect, updateUser
from data.templatesBD import findAllTemplates, findTemplateById, findOneTemplate
from data.avaliacaoBD import insertAvalic

db_client = connectMongo('Altair')

@login_required
@gestor_required
def nova_licitacao(request,pk):
    id = insertLic({'interno':True,'base64': Binary(''.encode()),'tituloArquivo':'Sem Título', 'achados':[], 'avaliada':0, 'status':0, 'id_template': pk,'dataCriação':datetime.now().strftime('%d/%m/%Y %H:%M'),'id_author':str(request.session['id']),'comentarios':''})
    return redirect('/gestor/construcao/editarLicitacao/'+str(id.inserted_id))

@login_required
@gestor_required
def editar(request,pk):
    licitacao = findOneLic(pk)
    if(licitacao['status']!=0):
        messages.info(request, 'Ação invalida, licitação: \''+licitacao['tituloArquivo']+'\' já submetida')
        return redirect('/gestor')
    template = findTemplateById(licitacao['id_template'])
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
@POST_required
def salvar(request):
    data = json.loads(request.body.decode('utf-8'))
    data['json']['base64'] = Binary(data['json']['base64'].encode())
    updateOneLic(data['_id'], data['json'])
    return HttpResponse()

@login_required
@gestor_required
@POST_required
def excluir(request,pk):
    licitacao = findLicByDataAndId(pk, {'status', 'tituloArquivo'})
    if licitacao['status'] != 0:
        messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' não pôde ser excluída')
        return redirect('/gestor')
    messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' foi excluída!')
    deleteLic(pk)
    return redirect('/gestor')

@csrf_exempt
@login_required
@gestor_required
def editarTitulo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        updateOneLic(data['_id'], data['json'])
    return HttpResponse()

@login_required
@gestor_required
def enviarConstrucao(request, pk):
    licitacao = findOneLic(pk)
    context = {
        'licitacao':licitacao,
        'id_licitacao':licitacao['_id']
    }
    modelo = loader.get_template('construtor_licitacoes/enviarConstrucao.html')
    return HttpResponse(modelo.render(context, request))

@login_required
@gestor_required
@POST_required
def salvarFormulario(request, pk):
    data = request.POST.copy()
    data['status'] = 1
    data['avaliada'] = 0
    del data['csrfmiddlewaretoken']
    licitacao = findLicByDataAndId(pk, {'status', 'tituloArquivo'})
    updateOneLic(pk, data)
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
@POST_required
def enviarGeral(request):
    from logic import Header, Tokeniza
    data = request.POST
    arquivo = request.FILES['arquivopdf'].read()
    bytespdf = base64.b64encode(arquivo)
    id_externo = insertLic({'interno':False,'tituloArquivo':str(request.FILES['arquivopdf']),'id_template': '62fa7d2fa15dc0d036b941fd','dataCriação':datetime.now().strftime('%d/%m/%Y %H:%M'), 'dataModificacao':datetime.now().strftime('%d/%m/%Y %H:%M'), 'base64': bytespdf, 'status': 1, 'orgao': data['orgao'], 'municipio': data['municipio'], 'estado': data['estado'], 'tipo': data['tipo'],  'objeto': data['objeto'], 'data': data['data'], 'id_author':str(request.session['id']),'comentarios':'', 'content': ''})
    content = extern_pdf_content(bytespdf,str(id_externo.inserted_id)+'.pdf')
    updateOneLic(id_externo.inserted_id, {'content':content})
    licitacao = findOneLic(id_externo.inserted_id)
    isValido = Tokeniza.Main().verificarValidade(licitacao)
    if not(isValido):
        deleteLic(id_externo.inserted_id)
        messages.info(request, 'A Licitação \''+licitacao['tituloArquivo']+'\' \nnão possui formato valido para o sistema')
        return redirect('/gestor/construcao/enviar')
        ...
    return redirect('/')


@csrf_exempt
@login_required
@gestor_required
@POST_required
def toPDF(request):
    data = json.loads(request.body.decode('utf-8'))
    pdf = weasyprint.HTML(string=data['contentPDF']).write_pdf()
    pdf = base64.b64encode(pdf)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=sample_pdf.pdf"
    return response
