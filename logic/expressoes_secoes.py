import re

EXP_GERAL = ('regra_secao_geral',re.compile(r'((\n)\s?(((SE[CÇ][ÃA]O)|(CAP[IÍ]TULO))([ ]){1,5})?(([LXVI]{1,8})|(\d{1,3}))([ )—––.-]+)([0])?([ )—––.-]*)(\n){0,2}((([A-ZÀÁÃÂÄÈÉÊËÍÎÔÕÓÒÖÛÚÙÜÇ-])+([0-9() \'“”""ªº\/:.,;–$%#@!\?&\*\|·])*){4,}))'))
EXP_AVISO = ('regra_aviso',re.compile(r'^(AVISO).{0,20}(LICITA[ÇC][ÃA]O)',flags=re.M))
EXP_ANEXO = ('regra_anexo',re.compile(r'^(ANEXO)',flags=re.M))

OBJETO = (['OBJETO'],re.compile(r'((OBJETO)|(DA LICITA[ÇC][ÃAÂ]O))'))
JULGAMENTO = (['JULGAMENTO'],re.compile(r'((JULGAMENTO)|(AN[AÁ]LISE[S]?.{0,20}PROPOSTA[S]?))'))
CONDICAO_PARTICIPACAO = (['CONDICAO_PARTICIPACAO'],re.compile(r'(PARTICIP)'))
HABILITACAO = (['HABILITACAO'],re.compile(r'(HABILITA)'))
CREDENCIAMENTO = (['CREDENCIAMENTO'],re.compile(r'(CREDENCI)'))