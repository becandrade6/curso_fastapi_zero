# Criando Rotas CRUD

Aplicação prática dos conceitos da aula passada

- http, verbos, status codes, schemas, ...

Vamos criar endpoints para cadastro, recuperação, alteração e deleção de usuários

### Um tipo de recurso

Quando queremos manipular um tipo específico de dados, precisamos fazer algumas operações com ele.

Por exemplo, vamos pensar na manipulação de _users_, temos Registrar, Deletar, Editar, ...

## Operações com dados (CRUD)

- **C**reate (Criar): Adicionar novos registros
- **R**ead (Ler): Recuperar registros existentes
- **U**pdate (Atualizar): Modificar registros existentes
- **D**elete (Excluir): Remover registros existentes

### Associações com HTTP

Associamos essas operações acima com os verbos do http vistos na aula passada

- Create    -> POST
- Read      -> GET
- Update    -> PUT
- Delete    -> DELETE

## A estrutura dos dados

Se quisermos trocar mensagens via HTTP, precisamos definir um formato (schema/contrato) para transferir esse dado

Imagino um JSON como esse:

    {
        "username": "dunossauro",
        "email": "dunossauro@email.com",
        "password": "senha-do_dunossauro"
    }

### Pydantic

A responsabilidade de entender os schemas de contrato e a validação para saber se os dados estão no formato do schema, vai ficar a cargo do pydantic. Usando o BaseModel dele.

#### O pydantic tem dados além do python

Validação de emails podem ser melhores importando do proprio pydantic o EmailStr

Para usar essa validação, podemos instalar uma extensão do pydantic:

    poetry add "pydantic[email]"

## Não se repita (DRY)

Você deve ter notado que a linha client = TestClient(app) nos testes ficou repetida nas funções de teste

Repetir código pode tornar o gerenciamento de testes mais complexo à medida que cresce, e é aqui que o princípio de DRY entra em jogo.

DRY incentiva a redução de repetição, criando um código mais limpo e manutenível

### Fixtures

Criamos a fixture direto no codigo do test_app, mas existe um padrão

Usualmente as fixtures ficam num arquivo _tests/conftest.py_, ele é um arquivo especial reconhecido pelo pyteste que permite definir fixtures que podem ser reutilizadas em diferentes módulos de teste dentro de um projeto. É uma forma de centralizar recursos comuns de teste.