from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, users

# Ao importar esse contrato e utiliza-lo, ja documenta e faz a validação
# para entradas da API, para validações com banco e tals usamos os models
from fast_zero.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)


# coloca na rota normal, apenas / após o ip
# passamos qual o status que ela deve retornar
# passamos qual o modelo de resposta esperado
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_home():
    # Caso retorne algo alem do contrato ele nao manda
    # Caso retorne algo faltante do contrato ele da erro interno do servidor
    return {'message': 'Olá Mundo!'}
