from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root_must_return_ok_and_ola_mundo(client):
    # Temos uma metodologia de testes baseadas no AAA
    # Arrange, Act e Assert

    response_root = client.get('/')  # Act (ação, executa o bloco de teste)

    # Usamos HTTPStatus.OK para "traduzir" ao inves de ficar
    # colocando os codigos 200, 300, etc...
    assert response_root.status_code == HTTPStatus.OK  # Assert
    # Obtemos a resposta do .get no .json() do objeto
    assert response_root.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    # Act
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Assert (validar UserPublic)
    # voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # voltou o que esperavamos?
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_create_user_username_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'password': 'password',
            'email': 'email@email.com',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST

    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_email_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'username',
            'password': 'password',
            'email': user.email,
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST

    assert response.json() == {'detail': 'Email already exists'}


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    # Pega os atributos do user (modelo do sqlalchemy) e
    # converte em modelo do schema
    # e depois transforma pra dicionario python com o dump
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [user_schema]}


def test_read_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_read_non_existent_user(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': '123',
            'id': user.id,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': user.id,
    }


def test_update_non_existent_user(client, token):
    response = client.put(
        '/users/666',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': '123',
            'id': 2,
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN

    assert response.json() == {'detail': 'Not enough permission'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.json() == {'message': 'User deleted'}


def test_delete_non_existent_user(client, token):
    response = client.delete(
        '/users/666', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permission'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token  # Existe a chave?
