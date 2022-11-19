from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

def gerar_senha_criptografada(senha):
    return pwd_context.hash(senha)


def vericar_senha(senha, senha_criptografada):
    return pwd_context.verify(senha, senha_criptografada)