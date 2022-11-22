from fastapi import APIRouter, Body, HTTPException, Depends, Header

from middlewares.JWTMiddelewares import verificar_token
from models.UsuarioModel import UsuarioCriarModel
from services.AuthService import decodificar_token_jwt
from services.UsuariosService import (
    registar_usuario,
    buscar_usuario_logado

)

router = APIRouter()


@router.post("/", response_description="Rota para criar um novo Usúario.")
async def rota_criar_usuario(usuario: UsuarioCriarModel = Body(...)):
    try:
        resultado= await registar_usuario(usuario)

        if not resultado['status'] == 201:
            raise HTTPException(status_code=resultado['status'], detail=resultado['mensagem'])

        return resultado
    except Exception as erro:
        print(erro)

        raise HTTPException(status_code=500, detail='Erro interno no servidor')


@router.get(
    '/me',
    response_description='Rota para buscar as informações do usuário logado.',
    dependencies=[Depends(verificar_token)]
    )
async def buscar_info_usuario_logado(Authorization: str = Header(default='')):
    try:
        token = Authorization.split('')[1]

        payload = decodificar_token_jwt(token)

        print(payload)

        return {
            "mensagem": "teste"
        }
        resposta = await buscar_usuario_logado(payload["usuario_id"])

        if not resultado ['status'] == 200:
            raise HTTPException(status_code=resultado['status'], detail=resultado['mensagem'])
        return resultado
    except:
        raise HTTPException(status_code=500, detail='Erro interno no servidor')
