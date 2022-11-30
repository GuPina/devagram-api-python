from fastapi.params import Form
from pydantic import BaseModel, Field, EmailStr

class UsuarioCriarModel(BaseModel):
    id: str = Field(...)
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



def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )

    return cls

@form_body
class UsuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "email": "Fulano@gmail.com",
                "senha": "senha123",
            }
        }
