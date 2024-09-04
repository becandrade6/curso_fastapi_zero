from pydantic import BaseModel, EmailStr


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


# Classe provisória para simular db a partir do userSchema
class UserDB(UserSchema):
    id: int


# Schema para retornar lista de usuários do DB mas sem a senha
class UserList(BaseModel):
    users: list[UserPublic]
