from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_must_return_ok_and_ola_mundo():
    # Temos uma metodologia de testes baseadas no AAA
    # Arrange, Act e Assert
    client = TestClient(app)    # Arrange

    response_home = client.get('/')  # Act

    response_root = client.get('/botafogo')  # Act

    assert response_home.status_code == HTTPStatus.OK  # Assert
    assert response_home.json() == 'Olá Mundo!'        # Assert

    assert response_root.status_code == HTTPStatus.OK         # Assert
    assert response_root.json() == {'message': 'Olá Fogão!'}  # Assert
