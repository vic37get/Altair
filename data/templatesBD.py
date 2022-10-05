from bson.objectid import ObjectId

from data.database import connectMongo

db_client = connectMongo('Altair')

def findAllTemplates():
    collection_template = db_client['template']
    templates = collection_template.find({})
    return templates

def findTemplateById(id):
    collection_template = db_client['template']
    template = collection_template.find_one({"_id":ObjectId(id)})
    return template

def findOneTemplate(nome, id):
    collection_template = db_client['template']
    template = collection_template.find_one(nome, id)
    return template
