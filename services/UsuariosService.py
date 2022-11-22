from models.UsuarioModel import UsuarioCriarModel
from repositories.UsuarioRepository import (
    criar_usuario,
    buscar_usuario_por_email,
    buscar_usuario,
    listar_usuarios,
    atualizar_usuario,
    deletar_usuario
)


async def registar_usuario(usuario: UsuarioCriarModel):
    try:
        usuario_encontrado = await buscar_usuario_por_email(usuario.email)

        if usuario:
            return{
                "mensagem": f'E-mail {usuario.email} já cadastrado no sistema',
                "dados": "",
                "status": 400
            }
        else:
            novo_usuario = await criar_usuario(usuario)

            return {
                "mensagem": "Usuário cadastrado com sucesso",
                "dados": novo_usuario,
                "suatus": 201
            }
    except Exception as error:
        return {
            "mensgaem": "Erro interno no servidor",
            "dados": str(error),
            "status": 500
        }

async def buscar_usuario_logado(id: str):
    try:
        usuario_encontrado = await buscar_usuario(id)

        if usuario_encontrado:
            return {
                "mensagem": f"Usuário encontrado.",
                "dados": usuario_encontrado,
                "suatus": 200
            }
        else:
            return {
                "mensagem": f"Usuário com o id {id} não foi encontrado.",
                "dados": "",
                "suatus": 404
            }

    except Exception as erro:
        print(erro)
        return {
            "mensgaem": "Erro interno no servidor",
            "dados": str(erro),
            "status": 500
        }