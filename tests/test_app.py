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
