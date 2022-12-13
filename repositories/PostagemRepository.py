import motor. motor_asyncio
from bson import ObjectId

from decouple import config
from models.UsuarioModel import UsuarioCriarModel
from repositories.UsuarioRepository import usuario_collection, ConverterUtil
from utils.AuthUtil import gerar_senha_criptografada

from models.PostagemModel import PostagemCriarModel


MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.devagram

postagem_collection = database.get_collection("postagem")


ConverterUtil = ConverterUtil()
class PostagemRepository:
    async def criar_postagem(self, postagem: PostagemCriarModel) -> dict:
        postagem_criada = await postagem_collection.insert_one(postagem.__dict__)

        nova_postagem = await postagem_collection.find_one({"_id": postagem_collection.inserted_id})

        return ConverterUtil.postagem_converter(nova_postagem)

    async def listar_postagens():
        return usuario_collection.find()

    async def buscar_postagem(self, id: str) -> dict:
        postagem = await postagem_collection.find_one({"_id": ObjectId(id)})

        if postagem:
            return ConverterUtil.postagem_converter(postagem)


    async def deletar_postagem(self, id: str):
        postagem = await postagem_collection.find_one({"_id": ObjectId(id)})

        if postagem:
            await postagem_collection.delete_one({"_id": ObjectId(id)})

