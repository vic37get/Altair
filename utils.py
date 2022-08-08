from pymongo import MongoClient

def connectMongo(db_name):
    client = MongoClient('mongodb://root:root@localhost:27017')
    db = client[db_name]
    return db