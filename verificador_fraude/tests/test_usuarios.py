from bson.objectid import ObjectId
from django.test import SimpleTestCase
from utils import connectMongo

db = connectMongo('Altair')

class UsuariosTest(SimpleTestCase):
    def test_cadastroExistente(self):
        collection_usuario = db['usuario']

        id = collection_usuario.insert_one({
            'usuario':'usuario.teste',
            'nome': 'usuario de teste',
            'cargo': 'Gestor',
            'email': 'usuariodeteste@gmail.com',
            'senha': 'senhadeteste123',
        })
        usuarios = collection_usuario.find_one({'_id':ObjectId(id.inserted_id)})
        self.assertIsNotNone(usuarios)
        collection_usuario.delete_one({'_id':ObjectId(id.inserted_id)})