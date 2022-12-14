import re
from logic import RegraProxy
from logic import descricao_expressoes as desc

alimentos_caros = RegraProxy.RegraProxy('alimentos_caros', re.compile(r'((((\s)|(\n))ostra[s]?(\s))|(((\s)|(\n))lagost[aims]+)(\s)|((caviar).{0,40}((beluga)|(petrossian)))|(((\s)|(\n))capelin(\s))|(((\s)|(\n))truta(\s))|(((\s)|(\n))lumpo(\s))|(((\s)|(\n))trufa[s]?(\s))|((presunto).{0,30}((parma)|(pata.{0,5}negra)|(italiano)|(ib[ée]rico)|(villani)|(espanhol)|(jam[óo]n)|(serrano)))|(((contra.{0,3}fil[ée])|(carne)).{0,20}((wagyu)|(matsusaka)|(kobe)|( yonezawa)|(mishima)|(omi)|(sanda)))|((caf[eé]).{0,20}((kape)|(alamid)|(luwak)|(kopi)|(civeta)|(weasel)|(jacu)))|((weasel).{0,20}(coffee))|(((foie)|(fois)).{0,10}(gras))|((cogumelo).{0,10}(matsutake))|((frango).{0,20}((cemani)|(ayam)))|((kobe).{0,10}(beef))|((queijo).{0,10}(alce)))',flags=re.IGNORECASE|re.S))
alimentos_caros.setDescricao(desc.alimentos_caros[1])

bebidas_alcoolicas = RegraProxy.RegraProxy('bebidas_alcoolicas', re.compile(r'((champanh[ea])|(champagne)|(u[ií]sque)|(whisk[e]?y)|([wv][oó]d[ck]a)|(cerveja)|(tequila)|(c[ou]nhaque)|(brandy)|(cacha[çc]a)|(((\s)|(\n))saquê(\s))|(((\s)|(\n))gim(\s))|(((\s)|(\n))cho[p]+[e]?(\s))|(((\s)|(\n))sidra(\s))|(absinto)|(vermut[eh])|((bebida).{0,20}(alc[oó]+lic[ao])))', flags=re.IGNORECASE|re.S))
bebidas_alcoolicas.setDescricao(desc.bebidas_alcoolicas[1])

comida_japonesa = RegraProxy.RegraProxy('comida_japonesa', re.compile(r'((sashimi)|(sushi)|(hossomaki)|(nigiri)|(norimaki)|(temaki)|(uramaki)|(futomaki)|(tekkamaki)|(gunkanzush))', flags=re.IGNORECASE|re.S))
comida_japonesa.setDescricao(desc.comida_japonesa[1])

itens_caros = RegraProxy.RegraProxy('itens_caros', re.compile(r'((playstation)|(Xbox)|(Nintendo)|(console[s]?(.{0,4}((video).{0,2})?(game[s]?))))', flags=re.IGNORECASE|re.S))
itens_caros.setDescricao(desc.itens_caros[1])

certidao_protesto = RegraProxy.RegraProxy('certidao_protesto', re.compile(r'((certid[aã]o).{0,100}(protesto))',flags=re.IGNORECASE|re.S))
certidao_protesto.setDescricao(desc.certidao_protesto[1])

certidao_corregedor = RegraProxy.RegraProxy('certidao_corregedor', re.compile('((certid[aã]o)|(declara[çc][ãa]o))(.{0,100}(corregedor)) ', flags=re.IGNORECASE|re.S))
certidao_corregedor.setDescricao(desc.certidao_corregedor[1])

integralizado = RegraProxy.RegraProxy('integralizado', re.compile(r'((capital.{0,20}integralizado)|(patrim[oô]nio.{0,20}integralizado))', flags=re.IGNORECASE|re.S))
integralizado.setDescricao(desc.integralizado[1])

garantia_cs_ou_pl = RegraProxy.RegraProxy('garantia_cs_ou_pl', re.compile(r'(garantia)(.{0,20}((patrim[oô]nio.{0,10}l[íi]qu[ií]do)|(capital.{0,10}social)))|((capital).{0,10}(social))(.{0,10}(patrim[oô]nio.{0,10}(l[íi]qu[ií]do).{0,10}(m[ií]n[ií]mo)))', flags=re.IGNORECASE|re.S))
garantia_cs_ou_pl.setDescricao(desc.garantia_cs_ou_pl[1])

idoneidade_financeira = RegraProxy.RegraProxy('idoneidade_financeira', re.compile('((atesta[do]*)|(certid[ãa]o)|(declara[çc]*[ãa]*[o]*))(.{0,70}((i[ni]*doneidade)).{0,20}((financeira)|(banc[áa]ria)))', flags=re.IGNORECASE|re.S))
idoneidade_financeira.setDescricao(desc.idoneidade_financeira[1])

vedacao_impugnacao = RegraProxy.RegraProxy('vedacao_impugnacao', re.compile(r'(i[nm]pugna[çc][ãaoõ][s]?)(.{1,15}(protocolizada[s]?))|((recurso[s]?)(.{0,10}(contrarraz[oõ]es)(.{1,10}(protocolizada[s]?))))', re.S))
vedacao_impugnacao.setDescricao(desc.vedacao_impugnacao[1])

certidao_quitacao = RegraProxy.RegraProxy('certidao_quitacao',re.compile(r'(((atesta[do]*)|(certid[ãa]o)|(declara[çc]*[ãa]*[o]*)).{0,10}((negativ[ao].{0,10}quita[çc][ãa]o)))', re.S))
certidao_quitacao.setDescricao(desc.certidao_quitacao[1])

carta_credenciamento = RegraProxy.RegraProxy('carta_credenciamento', re.compile(r'(((comprova[cçan][tãa][eo]).{0,15}(revenda))|(credenciamento.{0,10}fabricante)|(carta.{0,10}solidariedade))', flags=re.IGNORECASE|re.S))
carta_credenciamento.setDescricao(desc.carta_credenciamento[1])

quadro_permanente = RegraProxy.RegraProxy('quadro_permanente', re.compile(r'(((quadro).{0,10}(permanen[ciate]+)).{0,10}((contrato)|(carteira.{0,10}trabalho)|(presta[çc][aã]o.{0,10}servi[cç]o)|((servi[çc]o).{1,10}(futuro))))', flags=re.IGNORECASE|re.S))
quadro_permanente.setDescricao(desc.quadro_permanente[1])

filiacao_abav_iata = RegraProxy.RegraProxy('filiacao_abav_iata', re.compile(r'((((associa[çc][aã]o)|(empresa[s])|(sindicato))(.{0,30}((turismo)|(transporte)|(viage[mns]+)|(aerovi[áa]ria[s]?))))|((international)(.{0,10}((air).{0,10}(transport).{0,10}(association))))|(((\s)|(\n))embratur(\s))|(((\s)|(\n))iata(\s))|(((\s)|(\n))abav(\s))|(((\s)|(\n))sindetur(\s))|(((\s)|(\n))snea(\s)))', flags=re.IGNORECASE|re.S))
filiacao_abav_iata.setDescricao(desc.filiacao_abav_iata[1])

visto_registro_profissional = RegraProxy.RegraProxy('visto_registro_profissional', re.compile(r'(((visto).{0,20}((conselho)|(CREA)|(CAU)|(entidade.{0,10}profissional)|(registro)))|((caso).{0,20}((empresa[s]?.{0,10}n[ãa]o.{0,10}sediada[s]?)|(licitante[s]?.{0,10}n[aã]o.{0,10}sediado[s]?))))', re.S))
visto_registro_profissional.setDescricao(desc.visto_registro_profissional[1])

comprovante_localizacao = RegraProxy.RegraProxy('comprovante_localizacao', re.compile('(((alvar[aá])|(comprov[mnteçcãao]*)).{0,20}((localiza[çc][ãa]o)|(funcionamento)))',flags=re.IGNORECASE|re.S))
comprovante_localizacao.setDescricao(desc.comprovante_localizacao[1])

usina_asfalto_cbuq = RegraProxy.RegraProxy('usina_asfalto_cbuq', re.compile(r'(((localiza[cçaão]+)|(licen[cç]a.{0,10}(opera[cçãao]+))|(propriedade)|(patrim[oô]nio)|(disponibili[zacçãaodade]+)|(loca[cç][aã]o))(.{0,5}((usina)(.{0,5}((asfalto)|(cbuq)))))|(usina.{0,10}asfalto.{0,10}pr[óo]pria))', flags=re.IGNORECASE|re.S))
usina_asfalto_cbuq.setDescricao(desc.comprovante_localizacao[1])

amostra_prototipo = RegraProxy.RegraProxy('amostra_prototipo', re.compile('((amostra)|(prot[oó]tipo))(.{0,5}((proposta)|(envelope)))',flags=re.IGNORECASE|re.S))
amostra_prototipo.setDescricao(desc.amostra_prototipo[1])

n_min_max_limitacao_atestados = RegraProxy.RegraProxy('n_min_max_limitacao_atestados', re.compile(r'((((dois|duas)|(tr[êe]s)|(quatro)|(cinco)).{0,10}((atestado[s]?)|(certid[aãoões]*))).{0,20}((capacidade t[eé]cnica)|(qualifica[cç][aã]o t[eé]cnica)))', flags=re.IGNORECASE|re.S))
n_min_max_limitacao_atestados.setDescricao(desc.n_min_max_limitacao_atestados[1])

preferencia_prod_nacionais = RegraProxy.RegraProxy('preferencia_prod_nacionais', re.compile(r'(((margem).{0,10})?((prefer[eê]ncia.{0,10}(produto[s]?).{0,10})((nacionais)|(nacional))))', flags=re.IGNORECASE|re.S))
preferencia_prod_nacionais.setDescricao(desc.preferencia_prod_nacionais[1])

temp_exp_profissional = RegraProxy.RegraProxy('temp_exp_profissional', re.compile(r'(((tempo).{0,20}((experi[eê]ncia)|(exerc[ií]cio.{0,10}profissional)|(registro.{0,10}conselho)|(forma[cç][aã]o.{0,10}acad[eê]mica)))|(experi[êe]ncia.{0,10}ano)|(ano[s]?.{0,10}experi[eê]ncia))', flags=re.IGNORECASE|re.S))
temp_exp_profissional.setDescricao(desc.temp_exp_profissional[1])

atestado_compactador = RegraProxy.RegraProxy('atestado_compactador', re.compile(r'(((atestado).{0,20}((compactador)|(compactador percuss[aã]o)|(compacta[çc][aã]o)|(compactado)|(compactar)))|((t[eé]cnico operacional).{0,20}((compactar)|(compactado)))|((capacidade t[eé]cnica).{0,20}((compactador)|(compacta[cç][aã]o)|(compactado)|(compactar))))', flags=re.IGNORECASE|re.S))
atestado_compactador.setDescricao(desc.atestado_compactador[1])

atestado_aterro = RegraProxy.RegraProxy('atestado_aterro', re.compile(r'(((atestado).{0,20}((aterro)|(aterramento)|(aterrado)|(aterrar)))|((t[eé]cnico operacional).{0,20}((aterro)|(aterrar)|(aterrado)))|((capacidade t[eé]cnica).{0,20}((aterro)|(aterrado)|(aterrar))))', flags=re.IGNORECASE|re.S))
atestado_aterro.setDescricao(desc.atestado_aterro[1])

atestado_demolicao = RegraProxy.RegraProxy('atestado_demolicao', re.compile(r'(((atestado).{0,20}((demoli[cç][aã]o)|(demolir)|(demolido)))|((t[eé]cnico operacional).{0,20}((demoli[cç][aã]o)|(demolido)|(demolir)))|((capacidade t[eé]cnica).{0,20}((demoli[cç][aã]o)|(demolido)|(demolir))))', flags=re.IGNORECASE|re.S))
atestado_demolicao.setDescricao(desc.atestado_demolicao[1])

atestado_lastro = RegraProxy.RegraProxy('atestado_lastro', re.compile(r'(((atestado).{0,20}((lastro)|(lastreado)|(lastrear)|(lastro.{0,20}brita)|(lastro.{0,20}concreto)|(lastro.{0,20}areia)))|((t[eé]cnico operacional).{0,20}((lastro)|(lastreado)|(lastrear)|(lastro.{0,20}brita)|(lastro.{0,20}concreto)|(lastro.{0,20}areia)))|((capacidade t[eé]cnica).{0,20}((lastro)|(lastreado)|(lastrear)|(lastro.{0,10}brita)|(lastro.{0,10}concreto)|(lastro.{0,10}areia))))', flags=re.IGNORECASE|re.S))
atestado_lastro.setDescricao(desc.atestado_lastro[1])

recomposicao = RegraProxy.RegraProxy('recomposicao', re.compile(r'(((atestado).{0,20}((corte.{0,10}foice)|(preparo.{0,10}manual.{0,10}terreno)|(raspagem.{0,10}superficial.{0,10}manual)|(poda.{0,10}cerca.{0,5}viva)|(poda.{0,10}altura.{0,10}[aá]rvore)|(corte.{0,10}oxiacetileno)|(corte.{0,10}trilho.{0,10}equipamento.{0,10}leve)|(corte.{0,10}[áa]rea[s]?.{0,10}gramada[s]?)|(corte.{0,10}remo[çc][aã]o.{0,10}[aá]rvores)|(demoli[cç][aã]o.{0,10}martelete))))', flags=re.IGNORECASE|re.S))
recomposicao.setDescricao(desc.recomposicao[1])

atestado_regularizacao = RegraProxy.RegraProxy('atestado_regularizacao', re.compile(r'(((atestado).{0,50}((regulariza[cç][aã]o)|(regularizado)|(regularizar)))|((t[eé]cnico operacional).{0,50}((regulariza[cç][aã]o)|(regularizado)|(regularizar)))|((capacidade t[eé]cnica).{0,50}((regulariza[cç][aã]o)|(regularizar)|(regularizado))))', flags=re.IGNORECASE|re.S))
atestado_regularizacao.setDescricao(desc.atestado_regularizacao[1])

atestado_remendo = RegraProxy.RegraProxy('atestado_remendo', re.compile(r'(((atestado).{0,50}((remendo)|(remendado)|(remendar)|(tapa buraco)))|((t[eé]cnico operacional).{0,50}((remendo)|(remendado)|(remendar)|(tapa buraco)))|((capacidade t[eé]cnica).{0,50}((remendo)|(remendado)|(remendar)|(tapa buraco))))', flags=re.IGNORECASE|re.S))
atestado_remendo.setDescricao(desc.atestado_remendo[1])

atestado_escavacao = RegraProxy.RegraProxy('atestado_escavacao', re.compile(r'(((atestado).{0,50}((escava[cç][aã]o.{0,20}categoria)|(escavado.{0,20}categoria)|(escavar.{0,20}categoria)|(escava[cç][aã]o.{0,20}material)|(escavado.{0,20}material)|(escavar.{0,20}material)))|((t[eé]cnico operacional).{0,50}((escava[cç][aã]o.{0,20}categoria)|(escavado.{0,20}categoria)|(escavar.{0,20}categoria)|(escava[cç][aã]o.{0,20}material)|(escavado.{0,20}material)|(escavar.{0,20}material))|((capacidade).{0,50}((escava[cç][aã]o.{0,20}categoria)|(escavado.{0,20}categoria)|(escavar.{0,20}categoria)|(escava[cç][aã]o.{0,20}material)|(escavado.{0,20}material)|(escavar.{0,20}material)))))', flags=re.IGNORECASE | re.S))
atestado_escavacao.setDescricao(desc.atestado_escavacao[1])

atestado_carga = RegraProxy.RegraProxy('atestado_carga', re.compile(r'(((atestado).{0,50}((carregamento)|(carga)|(carregado)|(carregar)))|((t[eé]cnico operacional).{0,50}((carregamento)|(carga)|(carregado)|(carregar)))|((capacidade t[eé]cnica).{0,50}((carregamento)|(carga)|(carregado)|(carregar))))', flags=re.IGNORECASE|re.S))
atestado_carga.setDescricao(desc.atestado_carga[1])

atestado_corte = RegraProxy.RegraProxy('atestado_corte', re.compile(r'((atestado).{0,50}((corte)|(cortado)|(cortar)))', flags=re.IGNORECASE|re.S))
atestado_corte.setDescricao(desc.atestado_corte[1])

atestado_terraplanagem = RegraProxy.RegraProxy('atestado_terraplanagem', re.compile(r'(((atestado).{0,50}((terraplanagem)|(terraplanado)|(terraplanar)|(terraplenagem)))|((t[eé]cnico operacional).{0,50}((terraplanagem)|(terraplanar)|(terraplanado)|(terraplenagem)))|((capacidade t[eé]cnica).{0,50}((terraplanagem)|(terraplanar)|(terraplanado)|(terraplenagem))))', flags=re.IGNORECASE|re.S))
atestado_terraplanagem.setDescricao(desc.atestado_terraplanagem[1])

atestado_sondagem_manual = RegraProxy.RegraProxy('atestado_sondagem_manual', re.compile(r'(((atestado).{0,50}(sondagem))|((t[eé]cnico operacional).{0,50}(sondagem))|((capacidade t[eé]cnica).{0,50}(sondagem)))', flags=re.IGNORECASE|re.S))
atestado_sondagem_manual.setDescricao(desc.atestado_sondagem_manual[1])

atestado_sondagem = RegraProxy.RegraProxy('atestado_sondagem', re.compile(r'(((atestado).{0,50}((sondado)|(sondar)))|((t[eé]cnico operacional).{0,50}((sondado)|(sondar)))|((capacidade t[eé]cnica).{0,50}((sondado)|(sondar))))', flags=re.IGNORECASE|re.S))
atestado_sondagem.setDescricao(desc.atestado_sondagem[1])

atestado_transporte = RegraProxy.RegraProxy('atestado_transporte', re.compile(r'(((atestado).{0,50}((transporte)|(transportadora)))|((técnico operacional).{0,50}((transporte)|(transportadora)))|((capacidade técnica).{0,50}((transporte)|(transportadora))))', flags=re.IGNORECASE|re.S))
atestado_transporte.setDescricao(desc.atestado_transporte[1])

atestado_apicoamento = RegraProxy.RegraProxy('atestado_apicoamento', re.compile(r'(((atestado).{0,50}((apicoamento)|(apicotamento)))|((t[eé]cnico operacional).{0,50}((apicoamento)|(apicotamento)))|((capacidade t[eé]cnica).{0,50}((apicoamento)|(apicotamento)))|((qualifica[cç][aã]o t[eé]cnica).{0,50}((apicoamento)|(apicotamento)))|((habilita[cç][aã]o t[eé]cnica).{0,50}((apicoamento)|(apicotamento))))', flags=re.IGNORECASE|re.S))
atestado_apicoamento.setDescricao(desc.atestado_apicoamento[1])

atestado_remocao = RegraProxy.RegraProxy('atestado_remocao', re.compile(r'(((atestado).{0,50}((remo[cç][aã]o)|(removido)|(remover)))|((t[eé]cnico operacional).{0,50}((remo[cç][aã]o)|(removido)|(remover)))|((capacidade t[eé]cnica).{0,50}((remo[cç][aã]o)|(removido)|(remover))))', flags=re.IGNORECASE|re.S))
atestado_remocao.setDescricao(desc.atestado_remocao[1])

atestado_argamassa = RegraProxy.RegraProxy('atestado_argamassa', re.compile(r'(((atestado).{0,50}((argamassa)|(embo[cç]o)|(reboco)|(chapisco)))|((t[eé]cnico operacional).{0,50}((argamassa)|(embo[cç]o)|(reboco)|(chapisco)))|((capacidade t[eé]cnica).{0,50}((argamassa)|(embo[cç]o)|(reboco)|(chapisco))))', flags=re.IGNORECASE|re.S))
atestado_argamassa.setDescricao(desc.atestado_argamassa[1])

atestado_concreto = RegraProxy.RegraProxy('atestado_concreto', re.compile(r'(((atestado).{0,50}(concreto))|((t[eé]cnico operacional).{0,50}(concreto))|((capacidade t[eé]cnica).{0,50}(concreto)))', flags=re.IGNORECASE|re.S))
atestado_concreto.setDescricao(desc.atestado_concreto[1])

atestado_base_ou_leito = RegraProxy.RegraProxy('atestado_base_ou_leito', re.compile(r'(((atestado).{0,50}((execu[cç][aã]o.{0,10}base)|(base.{10}rodovia)|(execu[cç][aã]o.{0,10}leito)|(execu[cç][aã]o.{0,10}leito.{0,10}rodovia))|((t[eé]cnico operacional).{0,50}((execu[cç][aã]o.{0,10}base)|(base.{10}rodovia)|(execu[cç][aã]o.{0,10}leito)|(execu[cç][aã]o.{0,10}leito.{0,10}rodovia)))|((capacidade t[eé]cnica).{0,50}((execu[cç][aã]o.{0,10}base)(base.{0,10}rodovia)|(execu[cç][aã]o.{0,10}leito)|(execu[cç][aã]o.{0,10}leito.{0,10}rodovia)))))', flags=re.IGNORECASE|re.S))
atestado_base_ou_leito.setDescricao(desc.atestado_base_ou_leito[1])

atestado_desobstrucao = RegraProxy.RegraProxy('atestado_desobstrucao', re.compile(r'(((atestado).{0,50}((desobstru[cç][aã]o)|(limpeza.{0,10}fossa)|(boca de lobo)))|((t[eé]cnico operacional).{0,50}((desobstru[cç][aã]o)|(limpeza.{0,10}fossa)|(boca de lobo)))|((capacidade t[eé]cnica).{0,50}((desobstru[cç][aã]o)|(limpeza.{0,10}fossa)|(boca de lobo))))', flags=re.IGNORECASE|re.S))
atestado_desobstrucao.setDescricao(desc.atestado_desobstrucao[1])

atestado_limpeza = RegraProxy.RegraProxy('atestado_limpeza', re.compile(r'(((atestado).{0,50}(limpeza))|((t[eé]cnico operacional).{0,50}(limpeza))|((capacidade t[eé]cnica).{0,50}(limpeza)))', flags=re.IGNORECASE|re.S))
atestado_limpeza.setDescricao(desc.atestado_limpeza[1])

carregadeira_pneus = RegraProxy.RegraProxy('carregadeira_pneus', re.compile(r'(((mini(\s)?carregadeira).{0,10}((T)|(M3)|(CHI)|(CHP)|(H)|(UM)))|((carregadeira).{0,10}((1,5 M3)|(1,7 M3)|(1,9 M3)|(2,5 M3)|(2,8 M3)|(3,5 M3)|(106 Kw)|(113 Kw)))|(caminh[aã]o.{0,10}basculante.{0,10}carregadeira)|(trator.{0,10}carregadeira m3)|(usina.{0,10}m[oó]vel.{0,10}carregadeira)|(carregadeira.{0,10}1[Aª].{0,10}categoria)|(carregadeira.{0,10}2[Aª].{0,10}categoria))', flags=re.IGNORECASE|re.S))
carregadeira_pneus.setDescricao(desc.carregadeira_pneus[1])

rocha3a = RegraProxy.RegraProxy('rocha3a', re.compile(r'((material.{0,10}3[Aª]?.{0,10}categoria.{0,10}M3)|(rocha.{0,10}3[Aª]?.{0,10}categoria.{0,10}M3)|(rocha.{0,10}dura.{0,10}M3)|(rocha.{0,10}viva.{0,10}M3))', flags=re.IGNORECASE|re.S))
rocha3a.setDescricao(desc.rocha3a[1])

trator_esteiras = RegraProxy.RegraProxy('trator_esteiras', re.compile(r'((trator.{0,20}esteira[s]?)|(escava[cç][aã]o.{0,20}carga.{0,20}trator.{0,20}carregadeira))', flags=re.IGNORECASE|re.S))
trator_esteiras.setDescricao(desc.trator_esteiras[1])

trator_esteiras_laminas = RegraProxy.RegraProxy('trator_esteiras_laminas', re.compile(r'((areia.{0,20}extra[ií]da.{0,20}trator[es]*)|(areia.{0,20}extra[íi]da.{0,20}carregadeira)|(j[áa]z[ií]da.{0,20}trator))', flags=re.IGNORECASE|re.S))
trator_esteiras_laminas.setDescricao(desc.trator_esteiras_laminas[1])

areia_comercial = RegraProxy.RegraProxy('areia_comercial', re.compile(r'(areia.{0,50}comercial)', flags=re.IGNORECASE|re.S))
areia_comercial.setDescricao(desc.areia_comercial[1])

brita_comercial = RegraProxy.RegraProxy('brita_comercial', re.compile(r'((br[ií]ta.{0,30}comercial)|(pedra.{0,30}br[ií]ta.{0,30}comercial)|(pedra.{0,30}m[aão].{0,30}comercial))', flags=re.IGNORECASE|re.S))
brita_comercial.setDescricao(desc.brita_comercial[1])

compactador_manual = RegraProxy.RegraProxy('compactador_manual', re.compile(r'(((compactador).{0,50}((percuss[aã]o)|(percurss[aã]o)|(soquete)|(placa)|(manual)))|((aterro).{0,20}((manual)|(percuss[aã]o)|(percurss[aã]o)|(percurs[aã]o)|(soquete)|(placa)|(geocomposto)|(vala)|(compactado.{0,20}geogrelha.{0,20}unidirecional)|(material.{0,20}j[áa]z[ií]da)|(fita.{0,20}met[aá]lica)))|(reaterro.{0,20}manual)|(placa.{0,20}vibrat[óo]ria)|(compacta[cç][aã]o.{0,20}geocomposto)|(compacta[cç][aã]o.{0,20}vala)|(demoli[cç][aã]o.{0,20}manual)|(escava[cç][aã]o.{0,20}manual)|((lastro).{0,20}((brita)|(pedra.{0,20}britada)|(material.{0,20}granular)))|(recomposi[cç][aã]o.{0,20}eros[aã]o.{0,20}corte)|((regulariza[cç][aã]o).{0,20}((taludes.{0,20}soquete)|(vala.{0,20}apiloamento)))|(remendo.{0,20}profundo.{0,20}demoli[cç][aã]o.{0,20}serra)|(tapa.{0,10}buraco.{0,20}serra))', flags=re.IGNORECASE|re.S))
compactador_manual.setDescricao(desc.compactador_manual[1])

transporte_manual = RegraProxy.RegraProxy('transporte_manual', re.compile(r'(((transporte).{0,50}((manual)|(gerica)|(jerica)|(jirica)|(girica)|(carro.{0,10}m[aã]o)|(carrinho)))|((lan[cç]ado).{0,50}((manual)|(gerica)|(jerica)|(jirica)|(girica)|(carro.{0,10}m[aã]o)|(carrinho)))|((concretagem).{0,50}((manual)|(gerica)|(jerica)|(jirica)|(girica)|(carro.{0,10}m[aã]o)|(carrinho)))|(concreto.{0,20}lançamento.{0,20}manual)|(concreto.{0,20}central.{0,20}dosadora.{0,10}30.{0,10}M3)|(escava[cç][aã]o.{0,20}tunnel)|(concreto.{0,20}poroso.{0,20}tubo)|(confecç[aã]o.{0,20}tubo.{0,20}concreto)|(estaca.{0,20}raiz.{0,20}perfurada)|(sub.{0,5}base.{0,5}concreto))', flags=re.IGNORECASE|re.S))
transporte_manual.setDescricao(desc.transporte_manual[1])

roçagem_poda_corte_manual = RegraProxy.RegraProxy('roçagem_poda_corte_manual', re.compile(r'(((corte).{0,20}((foice)|(oxiacetileno)|(trilho)|([aá]reas.{0,10}gramadas)|(corte.{0,20}remo[cç][aã]o.{0,20}[aá]rvores)))|(preparo.{0,20}manual.{0,20}terreno)|(raspagem.{0,20}superficial.{0,20}terreno)|((poda).{0,20}((cerca viva)|(altura.{0,20}[aá]rvore)))|(demoli[cç][aã]o.{0,20}martelete)|(ro[cç]ada)|(capina)|(poda))', flags=re.IGNORECASE|re.S))
roçagem_poda_corte_manual.setDescricao(desc.roçagem_poda_corte_manual[1])

alvenaria_deitada = RegraProxy.RegraProxy('alvenaria_deitada', re.compile(r'(((alvenaria).{0,20}((deitada)|(uma vez)|(tijolo.{0,10}deitado)|(concreto.{0,10}deitado)))|(tijolo.{0,10}deitado))', flags=re.IGNORECASE|re.S))
alvenaria_deitada.setDescricao(desc.alvenaria_deitada[1])

certificado_registro_cadastral = RegraProxy.RegraProxy('certificado_registro_cadastral', re.compile(r'((cert.{0,20}(registr)).{0,10}(cadastr))', flags=re.IGNORECASE|re.S))
certificado_registro_cadastral.setDescricao(desc.certificado_registro_cadastral[1])

doc_firma_reconhecida_cartorio = RegraProxy.RegraProxy('doc_firma_reconhecida_cartorio', re.compile(r'((document).{0,20}(firma).{0,10}(reconhec).{0,10}cart[oó]rio)', flags=re.IGNORECASE|re.S))
doc_firma_reconhecida_cartorio.setDescricao(desc.doc_firma_reconhecida_cartorio[1])

certificado_boas_praticas = RegraProxy.RegraProxy('certificado_boas_praticas', re.compile(r'(((certificado[s]?)|(atestado[s]?)|(certid[aã]o)).{0,20}(boa[s]?.{0,5}pr[aá]tica[s]?))', flags=re.IGNORECASE|re.S))
certificado_boas_praticas.setDescricao(desc.certificado_boas_praticas[1])

exigencia_posse_previa = RegraProxy.RegraProxy('exigencia_posse_previa', re.compile(r'(((propriedade)|(posse)|(localiza[cç][aã]o)).{0,20}((ve[ií]culo[s]?)|(m[aá]quina[s]?)|(equipamento[s]?)))', flags=re.IGNORECASE|re.S))
exigencia_posse_previa.setDescricao(desc.exigencia_posse_previa[1])

licenca_ambiental = RegraProxy.RegraProxy('licenca_ambiental', re.compile(r'((licen[cç]a).{0,20}(ambiental))', flags=re.IGNORECASE|re.S))
licenca_ambiental.setDescricao(desc.licenca_ambiental[1])

vinculo_empregaticio = RegraProxy.RegraProxy('vinculo_empregaticio', re.compile(r'((v[ií]nculo).{0,20}(empreg).{0,20}((CTPS)|(carteira.{0,5}trabalho)|(carteira.{0,5}profissional)))', flags=re.IGNORECASE|re.S))
vinculo_empregaticio.setDescricao(desc.vinculo_empregaticio[1])

cadastro_previo = RegraProxy.RegraProxy('cadastro_previo', re.compile(r'(((cadastr).{0,20}(pr[ée]vio)))', flags=re.IGNORECASE|re.S))
cadastro_previo.setDescricao(desc.cadastro_previo[1])

certificado_qualidade = RegraProxy.RegraProxy('certificado_qualidade', re.compile(r'(((certifi)|(atestado)|(certid)|(declara)|(qualidade)).{0,20}((ABNT)|(ABIC)|(\sISO)))', flags=re.IGNORECASE|re.S))
certificado_qualidade.setDescricao(desc.certificado_qualidade[1])

comprovacao_atividade = RegraProxy.RegraProxy('comprovacao_atividade', re.compile(r'((comprova|confirma|prova|garantia).{1,10}(atividade|aptid[aã]o|compet[êe]ncia|habilidade|capacidade|propriedade).{1,10}(prazo|dia[s]?|periodo|mese[s]|ano[s]))', flags=re.IGNORECASE|re.S))
comprovacao_atividade.setDescricao(desc.comprovacao_atividade[1])

vedacao_documento = RegraProxy.RegraProxy('vedacao_documento', re.compile(r'((documento[s]?).{0,20}((postal)|(email)|(fax)))', flags=re.IGNORECASE|re.S))
vedacao_documento.setDescricao(desc.vedacao_documento[1])

lista_geral = [alimentos_caros,bebidas_alcoolicas,comida_japonesa, itens_caros, garantia_cs_ou_pl,
                       vedacao_impugnacao,preferencia_prod_nacionais,atestado_compactador,atestado_aterro,atestado_demolicao,atestado_lastro,recomposicao,atestado_regularizacao,atestado_remendo,atestado_escavacao,atestado_carga,atestado_corte,
                       atestado_terraplanagem,atestado_sondagem_manual,atestado_sondagem,atestado_transporte,atestado_apicoamento,atestado_remocao,atestado_argamassa,atestado_concreto,atestado_base_ou_leito,atestado_desobstrucao,atestado_limpeza,carregadeira_pneus,rocha3a,
                       trator_esteiras,trator_esteiras_laminas,areia_comercial,brita_comercial,compactador_manual,transporte_manual,roçagem_poda_corte_manual,alvenaria_deitada]

lista_habilitacao = [certidao_protesto, certidao_corregedor, integralizado, idoneidade_financeira, 
certidao_quitacao, carta_credenciamento, filiacao_abav_iata, visto_registro_profissional, 
comprovante_localizacao, usina_asfalto_cbuq, amostra_prototipo, n_min_max_limitacao_atestados,
 temp_exp_profissional, quadro_permanente, certificado_registro_cadastral, doc_firma_reconhecida_cartorio, certificado_boas_praticas,
exigencia_posse_previa, licenca_ambiental, vinculo_empregaticio, cadastro_previo, certificado_qualidade,
comprovacao_atividade, vedacao_documento]
'''
lista_habilitacao,lista_geral = [],[]

import utils
db = utils.connectMongo('Altair')
collection_regra = db['regra']

regras = collection_regra.find({'secao':'habilitacao'})
for regra in regras:
    lista_habilitacao.append(RegraProxy.RegraProxy().loadJson(regra))

regras = collection_regra.find({'secao':'geral'})
for regra in regras:
    lista_geral.append(RegraProxy.RegraProxy().loadJson(regra))
'''