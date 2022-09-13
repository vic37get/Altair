from bson.objectid import ObjectId
import re
from django.test import SimpleTestCase
from utils import connectMongo
from logic import LicitacaoProxy,Fraude,Header
import base64

db = connectMongo('Altair')
class VerificardorTest(SimpleTestCase):

    def test_licitacoes(self):
        sec1 = {'titulo':'PGg1IGNsYXNzPSJzZWNhb190aXR1bG8gdGl0dWxvQ2FwdHVyYSI+Q0FQzVRVTE8gSSAtIERPIE9CSkVUTzwvaDU+',
        'conteudo':'PHA+MS4xLiBPIG9iamV0byBkYSBwcmVzZW50ZSBsaWNpdGEmY2NlZGlsOyZhdGlsZGU7byAmZWFjdXRlOyBhIGVzY29saGEgZGEgcHJvcG9zdGEgbWFpcyB2YW50YWpvc2EgcGFyYSBhIEFxdWlzaSZjY2VkaWw7JmF0aWxkZTtvcGFyY2VsYWRhIHNvYiBkZW1hbmRhIGRlIE1hdGVyaWFpcywgU3VwcmltZW50b3MgZSBFcXVpcGFtZW50b3MgZGUgSW5mb3JtJmFhY3V0ZTt0aWNhLCBQcmVzdGEmY2NlZGlsOyZhdGlsZGU7b2RlIFNlcnZpJmNjZWRpbDtvcyBkZSBNYW51dGVuJmNjZWRpbDsmYXRpbGRlO28sIFJlY2FyZ2FzIGRlIENhcnR1Y2hvcyBlIFRvbm5lcnMsIGRlc3RpbmFkb3MgYSBhdGVuZGVyIGFQcmVmZWl0dXJhIE11bmljaXBhbCBlIGFzIGRpdmVyc2FzIFNlY3JldGFyaWFzIE11bmljaXBhaXMgZGUgQ0FSQUNPTCAmbmRhc2g7IFBJLCBkZSBhY29yZG8gY29tIGFxdWFudGlkYWRlIGUgZXNwZWNpZmljYSZjY2VkaWw7Jm90aWxkZTtlcyB0JmVhY3V0ZTtjbmljYXMgY29uc3RhbnRlcyBubyBUZXJtbyBkZSBSZWZlciZlY2lyYztuY2lhICZuZGFzaDsgQW5leG8gSSBkZXN0ZSBFZGl0YWwscXVhbnRpZGFkZXMgZSBleGlnJmVjaXJjO25jaWFzIGVzdGFiZWxlY2lkYXMgbmVzdGUgRWRpdGFsIGUgc2V1cyBhbmV4b3MuPC9wPgo8cD4xLjIuIEEgbGljaXRhJmNjZWRpbDsmYXRpbGRlO28gc2VyJmFhY3V0ZTsgUE9SIExPVEUsIGNvbmZvcm1lIHRhYmVsYSBjb25zdGFudGUgZG8gVGVybW8gZGUgUmVmZXImZWNpcmM7bmNpYSwgZmFjdWx0YW5kby1zZWFvIGxpY2l0YW50ZSBhIHBhcnRpY2lwYSZjY2VkaWw7JmF0aWxkZTtvIGVtIHF1YW50b3MgaXRlbnMgZm9yZW0gZGUgc2V1IGludGVyZXNzZS48L3A+CjxwPjEuMy4gTyBjcml0JmVhY3V0ZTtyaW8gZGUganVsZ2FtZW50byBhZG90YWRvIHNlciZhYWN1dGU7IG8gbWVub3IgcHJlJmNjZWRpbDtvIGRvIGl0ZW0sIG9ic2VydmFkYXMgYXMgZXhpZyZlY2lyYztuY2lhcyBjb250aWRhc25lc3RlIEVkaXRhbCBlIHNldXMgQW5leG9zIHF1YW50byAmYWdyYXZlO3MgZXNwZWNpZmljYSZjY2VkaWw7Jm90aWxkZTtlcyBkbyBvYmpldG8uQ29uZm9ybWUgRGVzcGFjaG8gZGUgSW5mb3JtYSZjY2VkaWw7JmF0aWxkZTtvIGRlIENyJmVhY3V0ZTtkaXRvIE9yJmNjZWRpbDthbWVudCZhYWN1dGU7cmlvIGUgbmFzIHNvbGljaXRhJmNjZWRpbDsmb3RpbGRlO2VzIHBvciBwYXJ0ZSBkYXMgc2VjcmV0YXJpYXNyZXF1ZXJlbnRlcyBhIERlc3Blc2Egc2UgZW5jb250cmEgYW1wYXJhZGEgY29tIHJlY3Vyc29zIGRvIE9SJkNjZWRpbDtBTUVOVE8gR0VSQUwvMjAyMixGUE0vSUNNUy9GVU5ERUIvU01FL1FTRS9GVVMvRk1TL0ZNQVMvSFBQL0dCRi9HU1VBUy9QU0IvQ1JBUy9QUiZPYWN1dGU7UFJJTyBlIG91dHJhc2NvbnNpZ25hZGFzIG5vIG9yJmNjZWRpbDthbWVudG8gdmlnZW50ZSwgY29uZm9ybWUgZG90YSZjY2VkaWw7Jm90aWxkZTtlcyBvciZjY2VkaWw7YW1lbnQmYWFjdXRlO3JpYXMgYWJhaXhvOjwvcD4='}
        sec2 = {'titulo':'PGg1IGNsYXNzPSJzZWNhb190aXR1bG8gdGl0dWxvQ2FwdHVyYSI+Q0FQzVRVTE8gSUkgLSBETyBKVUxHQU1FTlRPPC9oNT4=',
        'conteudo':'PHA+ZGFkZSByZWxhdGl2YSBhbyBGdW5kbyBkZSBHYXJhbnRpYSBwb3IgVGVtcG8gZGUgU2VydmkmY2NlZGlsO28gKEZHVFMpO1xuZykgUHJvdmEgZGUgcmVndWxhcmlkYWRlIHBlcmFudGUgYSBKdXN0aSZjY2VkaWw7YSBkbyBUcmFiYWxobywgbWVkaWFudGUgYSBhcHJlc2VudGEmY2NlZGlsOyZhdGlsZGU7byBkZSBDZXJ0aWQmYXRpbGRlO29cbk5lZ2F0aXZhIGRlIEQmZWFjdXRlO2JpdG9zIFRyYWJhbGhpc3RhcyAoQ05EVCkuXG5oKSBBbHZhciZhYWN1dGU7IGRlIGZ1bmNpb25hbWVudG8sIGV4cGVkaWRvIHBlbG8gTXVuaWMmaWFjdXRlO3BpbyBkbyBkb21pYyZpYWN1dGU7bGlvIG91IHNlZGUgZG8gbGljaXRhbnRlLlxuaSkgTGljZW4mY2NlZGlsO2EgZGEgVmlnaWwmYWNpcmM7bmNpYSBTYW5pdCZhYWN1dGU7cmlhIE11bmljaXBhbFxuaikgQ29tcHJvdmFudGUgZGUgaW5zY3JpJmNjZWRpbDsmYXRpbGRlO28gZGUgMjAxOCBubyBjYWRhc3RybyBkZSBmb3JuZWNlZG9yZXMgZG8gbXVuaWMmaWFjdXRlO3BpbyBsaWNpdGFudGUsIGV4cGVkaTwvcD4='}
        sec3 = {'titulo':'PGg1IGNsYXNzPSJzZWNhb190aXR1bG8gdGl0dWxvQ2FwdHVyYSI+Q0FQzVRVTE8gSUlJIC0gREFTIENPTkRJx9VFUyBERSBQQVJUSUNJUEHHw088L2g1Pg==',
        'conteudo':'PHA+cGFwZWwgdGltYnJhZG8gZSBzdWJzY3JpdGEgcGVsbyByZXByZXNlbnRhbnRlIGxlZ2FsIG91IHBlbG8gcHJvY3VyYWRvciBzZSBlc3RlIHRpdmVyIG91dG9yZ2EgcGFyYSB0YWwsIGFzc2VndXJhbmRvIGEgaW5leGlzdCZlY2lyYztuY2lhIGRlIGZhdG8gaW1wZWRpdGl2byBwYXJhIGxpY2l0YXIgb3UgY29udHJhdGFyIGNvbSBhIEFkbWluaXN0cmEmY2NlZGlsOyZhdGlsZGU7bzsgYykgQWx2YXImYWFjdXRlOyBkZSBsaWNlbiZjY2VkaWw7YSBkZSBmdW5jaW9uYW1lbnRvIDYuMiAmbmRhc2g7IERJU1BPU0kmQ2NlZGlsOyZPdGlsZGU7RVMgR0VSQUlTIERBIEhBQklMSVRBJkNjZWRpbDsmQXRpbGRlO08gaHR0cDovL3d3dy5sZWlkaXJldG8uY29tLmJyL2RlY3JldG8tbGVpLTU0NTIuaHRtbCBhKSBOYSBoaXAmb2FjdXRlO3Rlc2UgZGUgbiZhdGlsZGU7byBjb25zdGFyIHByYXpvIGRlIHZhbGlkYWRlIG5hcyBjZXJ0aWQmb3RpbGRlO2VzIGFwcmVzZW50YWRhcywgYSBBZG1pbmlzdHJhJmNjZWRpbDsmYXRpbGRlO28gYWNlaXRhciZhYWN1dGU7IGNvbW8gdiZhYWN1dGU7bCIsIiZpYWN1dGU7bmRpY2VzIG9maWNpYWlzIHF1YW5kbyBlbmNlcnJhZG9zIGgmYWFjdXRlOyBtYWlzIGRlIDAzICh0ciZlY2lyYztzKSBtZXNlcyBkYSBkYXRhIGRlIGFwcmVzZW50YSZjY2VkaWw7JmF0aWxkZTtvIGRhIHByb3Bvc3RhLCBjYXNvIGEgbGljaXRhbnRlIHRlbmhhIGluaWNpYWRvIHN1YXMgYXRpdmlkYWRlcyBubyBwcmVzZW50ZSBleGVyYyZpYWN1dGU7Y2lvLiA0LjEuNi4gT3V0cm9zIGRvY3VtZW50b3M6IGEpIEFsdmFyJmFhY3V0ZTsgZGUgbGljZW4mY2NlZGlsO2EgZGUgZnVuY2lvbmFtZW50byBhdHVhbGl6YWRvOyBiKSBEZWNsYXJhJmNjZWRpbDsmYXRpbGRlO28gZG8gbGljaXRhbnRlIGRlIHF1ZSBvcyBkb2N1bWVudG9zIGNvbnN0YW50ZXMgZGUgc2V1IEVudmVsb3BlIEEgJm5kYXNoOyBET0NVTUVOVE9TIERFIEhBQklMSVRBJkNjZWRpbDsmQXRpbGRlO08gcyZhdGlsZGU7byBmaSZlYWN1dGU7aXMgZSB2ZXJkYWRlaXJvcywgY29uZm9ybWUgbyBtb2RlbG8gZG8gYW5leG87IGMpIERlY2xhcmEmY2NlZGlsOyZhdGlsZGU7bywgc29iIGFzIHBlbmFzIGQ8L3A+'}
        secoes = [sec1,sec2,sec3]
        collection_licitacao = db['licitacao']
        id = collection_licitacao.insert_one({
            "tituloArquivo":'TESTE VERIFICAR',
            "status":0,
            "id_template":"62fa60beee51e36853cffe6d",
            "dataCriação":"13/09/2022 13:51",
            "cabecalho":"",
            "secoes":secoes,
        })
        licitacoes = collection_licitacao.find_one({'_id':ObjectId(id.inserted_id)})

        licitacao_Obj = LicitacaoProxy.ProxyLicitacao("",licitacoes['tituloArquivo'],"")
        secoes = []

        from logic import API
        api = API.API()
        for i in licitacoes['secoes']:
            secao = api.APISecao(i['titulo'],i['conteudo'])
            secoes.append(secao)
        licitacao_Obj.setSecoes(secoes)
        verificadorFraude = Fraude.Fraude(licitacao_Obj)
        licitacao_Obj.setTipoValidade(Header.TIPOS['VALIDO'])
        
        print(licitacao_Obj.getTipoValidade())
        print(verificadorFraude.getAchados())
        #-------------------
        collection_licitacao.delete_one({'_id':ObjectId(id.inserted_id)})
        self.assertIsNotNone(licitacao_Obj)

    
