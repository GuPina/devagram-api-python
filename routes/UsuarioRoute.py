from fastapi import APIRouter, Body


router = APIRouter()



@router.post("/", response_description="Rota para criar um novo Usúario.")
async def rota_criar_usuario(usuario = Body(...)):
    return{
        "mensagem": "Usuário cadastrado com sucesso."
    }