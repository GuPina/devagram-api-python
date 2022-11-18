from pydantic import BaseModel, Field, EmailStr

class UsuarioModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome":"Fulano de tal",
                "email": "Fulano@gmail.com",
                "senha": "senha123",
                "foto": "fulano.png"
            }
        }


