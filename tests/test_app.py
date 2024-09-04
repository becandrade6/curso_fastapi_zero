from http import HTTPStatus


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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': '123',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}
