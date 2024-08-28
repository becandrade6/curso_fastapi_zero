from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_must_return_ok_and_ola_mundo():
    # Temos uma metodologia de testes baseadas no AAA
    # Arrange, Act e Assert
    client = TestClient(app)    # Arrange (organização do teste)

    response_home = client.get('/')  # Act (ação, executa o bloco de teste)

    response_root = client.get('/botafogo')  # Act

    # Usamos HTTPStatus.OK para "traduzir" ao inves de ficar
    # colocando os codigos 200, 300, etc...
    assert response_home.status_code == HTTPStatus.OK  # Assert
    # Obtemos a resposta do .get no .json() do objeto
    assert response_home.json() == 'Olá Mundo!'        # Assert

    assert response_root.status_code == HTTPStatus.OK         # Assert
    assert response_root.json() == {'message': 'Olá Fogão!'}  # Assert
