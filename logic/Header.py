def diretorio():
    dst_dir = r'/'
    return dst_dir


DIRETORIO_TXT = diretorio()

CONTEXTO_INI,CONTEXTO_FIM = 200,200

SOURCE_r = 'raw'
SOURCE_v = 'validos'
OP_MOD_a = 'all'
OP_MOD_v = 'validar'
OP_MOD_tm= 'teste'

OP_MOD_DATAFRAME = False

import re
from RegraProxy import RegraProxy

EXP_GERAL = RegraProxy('regra_secao_geral',re.compile(r'((\n)\s?(((SE[CÇ][ÃA]O)|(CAP[IÍ]TULO))([ ]){1,5})?(([LXVI]{1,8})|(\d{1,3}))([ )—––.-]+)([0])?([ )—––.-]*)(\n){0,2}((([A-ZÀÁÃÂÄÈÉÊËÍÎÔÕÓÒÖÛÚÙÜÇ-])+([0-9() \'“”""ªº\/:.,;–$%#@!\?&\*\|·])*){4,}))'))
EXP_AVISO = RegraProxy('regra_aviso',re.compile(r'^(AVISO).{0,20}(LICITA[ÇC][ÃA]O)',flags=re.M))
EXP_ANEXO = RegraProxy('regra_anexo',re.compile(r'^(ANEXO)',flags=re.M))

TIPOS = {
    'OBJETO':'OBJETO',
    'JULGAMENTO':'JULGAMENTO',
    'CONDICAO_PARTICIPACAO':'CONDICAO_PARTICIPACAO',
    'HABILITACAO':'HABILITACAO',
    'CREDENCIAMENTO':'CREDENCIAMENTO',
    'OUTROS':'OUTROS',
    'AVISO':'AVISO',
    'SEM_SECAO':'SEM_SECAO',
    'LICITACAO':'LICITACAO',
    'VALIDO':'VALIDO',
    'INVALIDO':'INVALIDO',
    'INEXISTENTE':'INEXISTENTE'
}

TIPOS_SECOES = {
    'OBJETO':False,
    'JULGAMENTO':False,
    'CONDICAO_PARTICIPACAO':False,
    'HABILITACAO':False,
    'CREDENCIAMENTO':False,
    'OUTROS':False
}

TAMANHO_MAX_OBJ = 15

import expressoes
LISTA_TODOS = expressoes.lista_de_expressoes
LISTA_HABILITACAO = expressoes.lista_habilitacao

OBJETO = RegraProxy(TIPOS['OBJETO'],re.compile(r'((OBJETO)|(DA LICITA[ÇC][ÃAÂ]O))'))
JULGAMENTO = RegraProxy(TIPOS['JULGAMENTO'],re.compile(r'((JULGAMENTO)|(AN[AÁ]LISE[S]?.{0,20}PROPOSTA[S]?))'))
CONDICAO_PARTICIPACAO = RegraProxy(TIPOS['CONDICAO_PARTICIPACAO'],re.compile(r'(PARTICIP)'))
HABILITACAO = RegraProxy(TIPOS['HABILITACAO'],re.compile(r'(HABILITA)'))
CREDENCIAMENTO = RegraProxy(TIPOS['CREDENCIAMENTO'],re.compile(r'(CREDENCI)'))

SECOES = [OBJETO,JULGAMENTO,CONDICAO_PARTICIPACAO,HABILITACAO,CREDENCIAMENTO]

SECOES_OBRIGATORIAS = [OBJETO]
SECOES_OPCIONAIS = [JULGAMENTO,CONDICAO_PARTICIPACAO,HABILITACAO,CREDENCIAMENTO]