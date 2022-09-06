from utils import connectMongo

conexao = connectMongo('Altair')
collection_licitacao = conexao['licitacao']
licitacoes = collection_licitacao.find({})
print(licitacoes)