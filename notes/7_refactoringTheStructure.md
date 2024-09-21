# Refatorando a estrutura do projeto com Routers e Annotated

- Reestruturar o projeto para facilitar sua manutenção
- Mover coisas de autenticação para um arquivo chamado *auth.py*
- Deixando em *security.py* somente as validações de senha
- Remover constantes do código
- Criar routers específicos
- Testes


# Routers

Recurso fornecido pelo fastAPI

- Nos permite organizar e agrupar diferentes rotas em nossa aplicação
- Organização por domínios
- Um "subaplicativo" fastAPI que pode ser montado em uma aplicação principal

Manteremos o código mais organizado e legível, especialmente à medida que a nossa aplicação cresce e adicionamos mais rotas.

A ideia é mover tudo que é referente a users para um arquivo único que vamos chamar de *fast_zero/routes/users.py*

    from fastapi import APIRouter

    router = APIRouter(prefix = '/users', tags=['users'])

- *prefix*: o prefixo adiciona o /users em todos os endpoints do router
- *tags*: agrupa os endpoints na documentação


# Annotated

Tempos o tipo Annotated da biblioteca typing do proprio python

Permite colocarmos o tipo e alguns metadados adicionais

    from typing import Annotated

Podemos por exemplo, utilizar o Depends no campo de metadados