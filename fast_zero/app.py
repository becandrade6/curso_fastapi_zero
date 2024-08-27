from fastapi import FastAPI

app = FastAPI()


# coloca na rota normal, apenas / após o ip
@app.get('/')
def read_home():
    return 'Olá Mundo!'


# coloca na rota ip/botafogo
@app.get('/botafogo')
def read_root():
    return {'message': 'Olá Fogão!'}
