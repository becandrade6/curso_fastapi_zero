from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User

# Ao importar esse contrato e utiliza-lo, ja documenta e faz a validação
# para entradas da API, para validações com banco e tals usamos os models
from fast_zero.schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI()


# coloca na rota normal, apenas / após o ip
# passamos qual o status que ela deve retornar
# passamos qual o modelo de resposta esperado
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_home():
    # Caso retorne algo alem do contrato ele nao manda
    # Caso retorne algo faltante do contrato ele da erro interno do servidor
    return {'message': 'Olá Mundo!'}


# Apesar de retornar o user que é um UserSchema, ele ocultará a senha
# isso ocorre pq no response_model passamos o UserPublic que não tem senha
# Usa como parâmetro o schema que criamos para usuário
# Ao fazer isso, criamos varios validações automáticas e rápidas
# Assim como documentações também
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = User(
        username=user.username, email=user.email, password=user.password
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(
    limit: int = 10, skip: int = 0, session: Session = Depends(get_session)
):
    user = session.scalars(select(User).limit(limit).offset(skip))
    return {'users': user}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return db_user


# {user_id} cria uma "variavel" na url. Ou seja, é passada na url da requisição
# user_id: int -> diz que esse valor vai ser validado como inteiro
@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db_user.email = user.email
    db_user.username = user.username
    db_user.password = user.password

    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}
