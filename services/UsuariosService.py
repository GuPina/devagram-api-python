from models.UsuarioModel import UsuarioCriarModel
from providers.AWSProvider import AWSProvider
from repositories.UsuarioRepository import UsuarioRepository

awsProvider = AWSProvider()
usuarioRepository = UsuarioRepository

class UsuarioService:

    async def registar_usuario(self, usuario: UsuarioCriarModel, caminho_foto):
        try:
            usuario_encontrado = await usuarioRepository.buscar_usuario_por_email(usuario.email)

            if usuario_encontrado:
                return{
                    "mensagem": f'E-mail {usuario.email} já cadastrado no sistema',
                    "dados": "",
                    "status": 400
                }
            else:
                novo_usuario = await usuarioRepository.criar_usuario(usuario)
                try:
                    url_foto = awsProvider.upload_arquivo_s3(
                        f'fotos-perfil/{novo_usuario["id"]}.png',
                        caminho_foto
                    )

                    novo_usuario = await usuarioRepository.atualizar_usuario(novo_usuario["id"],{"foto": url_foto})
                except Exception as erro:
                    print(erro)

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

    async def buscar_usuario_logado(self, id: str):
        try:
            usuario_encontrado = await usuarioRepository.buscar_usuario(id)

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