import os
from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends, Header, UploadFile

from middlewares.JWTMiddelewares import verificar_token


router = APIRouter()


@router.post("/", response_description="Rota para criar um novo Post.")
async def rota_criar_postagem(file: UploadFile, usuario: PostagemCriarModel = Depends(UsuarioCriarModel)):
    try:
        caminho_foto = f'files2/foto-{datetime.now().strftime("%H%M%S%")}.png'
        with open(caminho_foto, 'wb+') as arquivo:
            arquivo.write(file.file.read())

        #resultado= await registar_usuario(usuario, caminho_foto)

        os.remove(caminho_foto)

    except Exception as erro:
        raise erro


@router.get(
    '/',
    response_description='Rota para listar as postagens.',
    dependencies=[Depends(verificar_token)]
    )
async def listar_pstagens(Authorization: str = Header(default='')):
    try:

        return {
            "teste": "OK"
        }

    except Exception as erro:
        raise erro

    @router.get(
        '/me',
        response_description='Rota para listar as postagens do usuário.',
        dependencies=[Depends(verificar_token)]
    )
    async def buscar_info_usuario_logado(Authorization: str = Header(default='')):
        try:

            return {
                "teste": "OK"
            }

        except Exception as erro:
            raise erro