from django.shortcuts import render

def nova_licitacao(request):
    return render(request, 'adicionar.html',{})
