import base64
import os
from pathlib import Path

import PyPDF2

base_dir = Path(__file__).resolve().parent.parent
DEFAULT_FOLDER_PDF = 'temp_pdf'
DEFAULT_FOLDER_TXT = 'temp_txt'


def pdf2txt(base_dir,folder,file):
    text = ''
    caminho_do_arquivo = Path.joinpath(base_dir,folder,file)
    caminho_do_arquivo = str(caminho_do_arquivo)
    pdf_em_bytes=open(caminho_do_arquivo,'rb')
    objeto_tipo_pdf=PyPDF2.PdfReader(pdf_em_bytes)
    for pagina in objeto_tipo_pdf.pages:
        text += pagina.extract_text() + "\n"
    try:
        with open(Path.joinpath(base_dir,DEFAULT_FOLDER_TXT,Path(str(file)).stem+'.txt'),'w') as file:
            for i in splitLine(text):
                file.writelines(i+'\n')
    except:
        ...
    file_txt = Path.joinpath(base_dir,DEFAULT_FOLDER_TXT,Path(str(file)).stem+'.txt')
    if(os.path.exists(file_txt)):
        return True
    else:
        return False
    
def splitLine(content):
    lines = content.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].replace("  ", "")
    while '' in lines: lines.remove('')
    return lines


def b64tPDF(data,name):
    with open(Path.joinpath(base_dir,DEFAULT_FOLDER_PDF,name),'wb') as file:
        file.write(base64.b64decode(data))
        file.close()

def extern_pdf_content(data,name):
    b64tPDF(data,name)
    txt = pdf2txt(base_dir,DEFAULT_FOLDER_PDF,name)
    os.remove(Path.joinpath(base_dir,DEFAULT_FOLDER_PDF,name))
    if txt:
        content = ''
        with open(Path.joinpath(base_dir,DEFAULT_FOLDER_TXT,Path(str(name)).stem+'.txt'),'r',encoding='utf-8') as file:
            content = file.read()
            file.close()
        os.remove(Path.joinpath(base_dir,DEFAULT_FOLDER_TXT,Path(str(name)).stem+'.txt'))
        return content
    else:
        return ''
