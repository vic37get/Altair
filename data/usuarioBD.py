from bson.objectid import ObjectId

from data.database import connectMongo

db_client = connectMongo('Altair')

def insertUser(dados):
    collection_usuario = db_client['usuario']
    collection_usuario.insert_one(dados)

def searchAuthenticateUser(user, password):
    collection_usuario = db_client['usuario']
    usuario = collection_usuario.find_one({'userID':user,'senha':password})
    return usuario

def findOneUser(id):
    collection_usuario = db_client['usuario']
    usuario = collection_usuario.find_one({"_id":ObjectId(id)})
    return usuario

def findOneUserDirect(id):
    collection_usuario = db_client['usuario']
    usuario = collection_usuario.find_one(id)
    return usuario

def updateUser(id, data):
    collection_usuario = db_client['usuario']
    collection_usuario.update_one({'_id':ObjectId(id)},{'$set':data},upsert=True)
