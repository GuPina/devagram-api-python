from models.UsuarioModel import UsuarioCriarModel
from repositories.UsuarioRepository import (
    criar_usuario,
    buscar_usuario_por_email,
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