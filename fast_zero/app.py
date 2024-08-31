from http import HTTPStatus

from fastapi import FastAPI

# Ao importar esse contrato e utiliza-lo, ja documenta e faz a validação
from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

# Criando um database "falso" para apenas estudar durante terceira aula
database = []


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
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
# Usa como parâmetro o schema que criamos para usuário
# Ao fazer isso, criamos varios validações automáticas e rápidas
# Assim como documentações também
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump(),  # Desempacota dados do dicionario user e
        # transforma objeto do pydantic em dicionario do python
    )

    database.append(user_with_id)

    return user_with_id
