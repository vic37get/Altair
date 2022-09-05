from django.test import SimpleTestCase
import weasyprint
import os

class PdfTest(SimpleTestCase):
    def test_pdf_python(self):
        pdf = weasyprint.HTML(filename=os.path.join(os.getcwd(),'construtor_licitacoes','tests','sample.html')).write_pdf()
        open(os.path.join(os.getcwd(),'construtor_licitacoes','tests','google.pdf'), 'wb').write(pdf)