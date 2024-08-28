# Anotações sobre o curso de Fast API do zero 

>Eduardo Mendes no youtube https://fastapidozero.dunossauro.com

## Configuração do ambiente e hello world com testes

Usamos o _pyenv_ para gerenciar versões do python e especificar a versão que o projeto irá rodar.

Para gerenciamento dos pacotes e dependências estamos usando o _poetry_. Foi com ele que criamos a pasta do projeto, ja criando a estrutura básica do projeto. Com ele também adicionamos o fastapi no ambiente.

Dentro do _pyproject.toml_ ficam as dependências abstratas (que queremos que sejam instaladas) e dentro do _poetry.lock_ as dependências concretas (exatamente as versões exatas que estamos instalando).
    
    Quando for comitar o git, sobe o .lock também


Ao rodarmos python -i abrimos o terminal interativo do python

Após usar _poetry install_ e _poetry add fastapi_ ainda precisamos **ativar o ambiente virtual** usando o comando

    poetry shell

**Diferença na versão atual do que da do curso**: agora deve-se rodar __poetry add fastapi[standard]__

Usamos o Ruff para determinar padrões conforme PEP8 e nos deixar "dentro das regras" para codar. Mas iremos adicioná-lo apenas para ambiente de dev, logo criamos o grupo de dev

    poetry add --group dev ruff

Significado das siglas para o ruff no pyproject.toml estão no curso.

Para checar todos os arquivos daquele local do shell:

    ruff check .

Para consertar:

    ruff check . --fix

Para formatar caso tivessemos regras (no pyproject.toml):
    ruff format .

*Usaremos o taskipy para criar alguns aliases e abreviar comandos*

    poetry add --group dev taskipy

Adicionamos no __pyproject.toml__ os aliases conforme o exemplo que ja esta la

E então, rodamos task __alias__ para rodar aquele comando

    eg.: task run

### Testes

Para escrever o teste, criamos sempre um arquivo dentro da pasta _tests_.

Por convenção, os arquivos sempre tem o prefixo _test__[...]_.py_

Criamos um cliente de teste do fastapi usando o objeto

    TestClient, importado de fastapi.testclient

    client = TestClient(app)

A estrutura de um teste, costuma contar com 3 ou 4 fases importantes (estrutura AAA):

- Organizar (Arrange): organizar o terreno
- Agir (Act): executar a ação
- Afirmar (Assert): garanta/afirme que isso igual a isso
- teardown: quando precisa desorganizar para testar outra coisa

No exemplo final do arquivo _test__app.py_ temos comentado o que faz parte de cada etapa

### Ferramentas extras

- Utilizamos o _ignr_ para gerar o arquivo gitignore para o nosso projeto do python, rodando (chama e armazena no arquivo passado)

        ignr -p python > .gitignore
    
- Inicializamos um repositorio na pasta

        git init.
    
    E fizemos o primeiro commit

        git add .
        git commit -m "Mensagem de commit"
    
    E adicionamos ele no nosso github, usando o gh

        gh repo create
    
    