from bson.objectid import ObjectId

from data.database import connectMongo

db_client = connectMongo('Altair')

def insertAvalic(dados):
    collection_avaliacao = db_client['avaliacao']
    collection_avaliacao.insert_one(dados)
