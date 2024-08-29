# Fundamentos do desenvolvimento web

Arquitetura base Cliente-Servidor

Cliente requisita, servidor serve (roda a aplicação e devolve)

## O Uvicorn

O fastapi é um framework web. Já o Uvicorn é o servidor de aplicação que serve a aplicação.

Por padrão, o fastapi usa o uvicorn.

O cliente requisita para o servidor (uvicorn) e ele repassa para a aplicação python.

Até o momento, estamos usando o "loopback", o nosso pc é o cliente e o servidor ao mesmo tempo. Porém, depois queremos fazer uma aplicação para diversos clientes.

## Conceitos da rede

Saindo do loopback, podemos abrir o servidor do uvicorn para rede local:

    fastapi dev fast_zero/app.py --host 0.0.0.0

Assim, toda a rede doméstica pode acessar a aplicação se souberem o ip da máquina.

    basta acessar por http://seu_ip:8000

podemos obter o ip da maquina por (outros comandos
tbm funcionam, pesquisar na net caso necessário)
    ip addr

## O modelo padrão da web

- URL: Localizador Uniforme de recursos. Um endereço de rede pelo qual podemos nos comunicar com um computador na rede
- HTTP: um protocolo que especifica como deve ocorrer a comunicação entre dispositivos
- HTML: a linguagem usada para criar e estruturar páginas na web.

### URL

http://127.0.0.1:8000

significa que estamos até a segunda barra é o protocolo, depois até o : vem o endereço e depois vem a porta.

após esse padrão podemos ter

    /caminho/recurso?query#fragmento

- caminho: onde está o que queremos acessar
- recurso: a identificação do que queremos
- query: um filtro do recurso
- fragmento: especifica um pedaço do recurso

### HTTP

HyperText Transfer Protocol, é o protocolo fundamental na web para transferência de dados e comunicação entre clientes e servidores.

Tanto requisições quanto respostas são referidas como mensagens.

Podemos ter um cabeçalho. O cabeçalho contém metadados sobre a requisição ou resposta.

Verbos (indicam sua intenção) do HTTP, entre outros:

- GET: utilizado para recuperar "pegar" recursos.
- POST: permite criar um novo recurso. Ex: enviar dados para registrar um novo usuário
- PUT: Atualiza um recurso existente. Ex: atualizar as informações de um usuário existente.
- DELETE: Exclui um recurso. Ex: remover usuário específico do sistema.

Códigos de resposta (http with dogs (ou cats) pra exemplos):

- 1xx: informativo - utilizada para enviar informações
- 2xx: sucesso
- 3xx: redirecionamento
- 4xx: erro no **cliente**
- 5xx: erro no **servidor**

Códigos importantes para o curso:

- 200 (OK): solicitação foi bem sucedida
- 201 (Created): solicitação foi bem sucedida e um novo recurso foi criado como resultado
- 404 (Not Found): recurso solicitado não pôde ser encontrado
- 422 (Unprocessable Entity): usado quando a requisição está bem-formada, mas não pode ser seguida devido a erros semânticos. "Me mandou mas ta deselegante, conteudo meio errado"
- 500 (Internal Server Error): quando existe um erro na nossa aplicação

## FastAPI e códigos de resposta

Por padrão o fastAPI já usa o código 200 OK como código de resposta. Mas podemos dizer isso explicitamente:

    from http import HTTPStatus

    # ou status direto tipo 200, 400 etc    
    @app.get('/', status_code = HTTPStatus.OK) 
    def read_root():
        return {'message': 'Olá mundo!'}

## APIs

Aqui entra o conceito de APIs, que frequentemente utilizam JSON para a troca de dados. JSON é um formato leve de troca de dados, fácil de ler e escrever para humanos, e simples de interpretar e gerar para máquinas.

### Contratos

Quando falamos sobre compartilhamento de JSON entre cliente e servidor, é crucial estabelecer um entendimento mútuo sobre a estrutura dos dados que serão trocados.

A este entendimento, denominamos **schema**, que atua como um contrato definindo a forma e conteúdo dos dados trafegados.

### Pydantic

No universo de APIs e contratos de dados, especialmente ao trabalhar com Python, o Pydantic se destaca como ferramenta poderosa e versátil. Além de embutida no FastAPI.

A ideia dele é criar uma camada de documentação, via OpenAPI, e de fazer a validação dos modelos de entrada e saída da nossa API.

Vamos criar um novo arquivo em nosso projeto chamado fast_zero/schemas.py

    from pydantic import BaseModel

    class Message(BaseModel):
        message: str

Aqui temos a ideia de um json representada em python. Um objeto de chave message, com um valor do tipo 'str'.

Basicamente importamos um modelo base e criamos uma nova dataclass para reger qual será uma entrada e/ou saída

