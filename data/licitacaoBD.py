from bson.objectid import ObjectId

from data.database import connectMongo

db_client = connectMongo('Altair')

def insertLic(dados):
    collection_licitacao = db_client['licitacao']
    id = collection_licitacao.insert_one(dados)
    return id

def findallLic():
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find()
    return licitacoes

def findOneLic(id):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(id)})
    return licitacao

def findLicByDataAndId(id, dados):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(id)}, dados)
    return licitacao

def findLicsDados(dados):
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find(dados)
    return licitacoes

def updateOneLic(id, dados):
    collection_licitacao = db_client['licitacao']
    collection_licitacao.update_one({'_id':ObjectId(id)},{'$set':dados},upsert=True)

def deleteLic(id):
    collection_licitacao = db_client['licitacao']
    collection_licitacao.delete_one({"_id":ObjectId(id)})