import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


# As nossas funções de teste agora recebem um parametro que chama client
# Esse client é uma fixture do pytest
# Ou seja, toda vez que uma função de teste receber um parametro client
# Ele vai executar a função defenida ali e passar o retorno da função
# como o parametro
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # Cria banco em memoria volatil e dura apenas durante teste
    engine = create_engine('sqlite:///:memory:')
    # Cria tudo
    table_registry.metadata.create_all(engine)

    # Cria a sessão e retorna ela na fixture
    with Session(engine) as session:
        # Roda até aqui e esse objeto cai la dentro do teste
        yield session

    # Exclua tudo depois
    table_registry.metadata.drop_all(engine)
