import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# As nossas funções de teste agora recebem um parametro que chama client
# Esse client é uma fixture do pytest
# Ou seja, toda vez que uma função de teste receber um parametro client
# Ele vai executar a função defenida ali e passar o retorno da função
# como o parametro
@pytest.fixture
def client():
    return TestClient(app)
