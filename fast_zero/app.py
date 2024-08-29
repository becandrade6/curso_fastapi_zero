from http import HTTPStatus

from fastapi import FastAPI

# Ao importar esse contrato e utiliza-lo, ja documenta e faz a validação
from fast_zero.schemas import Message

app = FastAPI()


# coloca na rota normal, apenas / após o ip
# passamos qual o status que ela deve retornar
# passamos qual o modelo de resposta esperado
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_home():
    # Caso retorne algo alem do contrato ele nao manda
    # Caso retorne algo faltante do contrato ele da erro interno do servidor
    return {'message': 'Olá Mundo!'}


# coloca na rota ip/botafogo
@app.get('/botafogo')
def read_root():
    return {'message': 'Olá Fogão!'}
