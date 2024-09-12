# Aula 04 - Banco de dados com SQLAlchemy e gerenciando migrações com Alembic

Iremos manipular o banco com o SQLAlchemy e gerenciar migrações usando o Alembic.

Link para referência da aula em texto <https://fastapidozero.dunossauro.com/04/>


# SQLAlchemy

O SQLAlchemy tem muitas ferramentas para manipular bancos e facilitar o uso do SQL.

Dentro dele temos um ORM. Que permite que trabalhemos com bancos de dados SQL de maneira mais natural com métodos e atributos Python para manipular seus registros de banco de dados.

Vincularemos objetos a registros de banco de dados.

## Registry

Uma "coisa" que registra **metadados**

Metadados armazenam dados sobre dados. Ou seja, podemos falar o tipo de um campo, o nome de um campo, etc.

Logo, o registry registra esses metadados das nossas tabelas.

Vamos então atribuindo mapeamentos dentro do registro usando o decorator .mapped_as_dataclass

E usamos o Mapped do sqlalchemy para falar os tipos 

## Engine

A engine do SQLAlchemy é o ponto de conexão ao banco de dados, estabelecendo e gerenciando conexões.


## Session

É uma camada intermediária entre o nosso código e o banco de dados. Alguem que fica no meio de campo e nós ficamos chamando ela para executar as coisas dentro do banco de dados.


# Pydantic Settings

Usamos o pydantic-settings para estabelecer variaveis e manter segurança e escalabilidade do nosso aplicativo.

Faz parte dos "12 fatores"


# Migrações

Aqui estamos falando de migrações sobre Metadados (tabelas, tipos de colunas, o esqueleto do database).

Usaremos o alembic para:

- Banco de dados evolutivo
- O banco acompanha as alterações do código
- Reverter alterações no schema do banco


# Exercicios finais

- Criamos campo updated_at com init=False e onupdate=func.now() para pegar o datetime quando atualizar aquela linha
- Geramos uma nova migração autogerada com o comando *alembic revision --autogenerate -m "update users table with updated_at"*
- Aplicamos a migração com o comando *alembic upgrade head*