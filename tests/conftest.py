import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import User, table_registry
from fast_zero.security import get_password_hash


# As nossas funções de teste agora recebem um parametro que chama client
# Esse client é uma fixture do pytest
# Ou seja, toda vez que uma função de teste receber um parametro client
# Ele vai executar a função defenida ali e passar o retorno da função
# como o parametro
@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override

        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # Cria banco em memoria volatil e dura apenas durante teste
    # Não faz checagem de mesma thread pro banco de teste
    # Usa a mesma pool
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    # Cria tudo
    table_registry.metadata.create_all(engine)

    # Cria a sessão e retorna ela na fixture
    with Session(engine) as session:
        # Roda até aqui e esse objeto cai la dentro do teste
        yield session

    # Exclua tudo depois
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user(session):
    pwd = 'testtest'
    user = User(
        username='Teste',
        email='teste@test.com',
        password=get_password_hash(pwd),
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = pwd

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    return response.json()['access_token']
