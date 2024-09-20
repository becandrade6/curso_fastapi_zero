from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    # Vai tentar achar os atributos que tem os atributos do schema e construir
    # modelo do pydantic quando tentamos converter objeto do
    # sqlalchemy pro schema
    model_config = ConfigDict(from_attributes=True)


# Schema para retornar lista de usuários do DB mas sem a senha
class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str  # O token JWT que vamos gerar
    token_type: str  # 'Como usar' o token


class TokenData(BaseModel):
    username: str | None = None
