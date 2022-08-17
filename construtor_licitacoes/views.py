from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from fpdf  import FPDF
#baixar pdf
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import io;

def nova_licitacao(request):
    template = loader.get_template('construtor_licitacoes/adicionar.html')
    return HttpResponse(template.render({}, request))


def baixarPdf(request):
    
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    text = c.beginText()
    text.setTextOrigin(cm,cm)
    text.setFont("Helvetica",14)

    # lines = [
    #     "lorem ipsolum test",
    #     "light up the night",
    #     "there is a city this darkness cant hide",
    #     "there is a fire that will burn through the streets of the city",
    # ]
    lines = request.POST.get("textoSecao")
    print(lines);
    #loop

    for line in lines:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment = 1,filename='licitação.pdf')