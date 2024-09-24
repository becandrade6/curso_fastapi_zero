# Tornando o sistema de autenticação robusto

- Testar casos de autenticação de forma correta
- Testar os casos de autorização de forma correta
- Implementar o refresh do token
- Introduzir testes que param o tempo com *freezegun*
- Introduzir geração de modelos automática com *factory-boy*

# Testes de autorização

## Criando modelos Users sob demanda

Para fazer a criação de users de forma mais intuitiva e sem preocupação de valores repetidos, podemos usar uma "fábrica" de usuários.

Isso pode ser feito com uma biblioteca chamada *factory-boy*

    Fábrica é um padrão de projeto de construção de objetos

    Adicionamos a biblioteca no grupo de dev

    poetry add --group dev factory-boy

## "Viajando no tempo"

Para testar coisas por exemplo que precisam mexer com o tempo, temos o *freezegun*

    poetry add --group dev freezegun

Usaremos por exemplo para testar um token invalido apos 30min