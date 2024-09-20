# Autenticação e Autorização

# Armazenamento senhas de forma segura

Nossas senhas estão sendo armazenadas de forma limpa (cru) no banco de dados. Isso pode nos trazer diversos problemas

- Erros eventuais: Uma simples alteração do schema e a senha estará exposta
- Vazamento de banco de dados:
    - Caso alguém consiga acesso ao banco de dados, pode ver as senhas
    - Pessoas costumam usar as mesmas senhas em N lugares

Para armazenar de forma segura, vamos armazenar somente o hash das senhas e criar duas funções para controlar esse fluxo:

    poetry add "pwdlib[argon2]"

- pwdlib é uma biblioteca criada especialmente para manipular hashs de senhas
- argon2 é um algoritmo de hash

Vamos criar um novo arquivo no nosso pacote para gerenciar a parte de segurança: security.py


# Autenticação

- Cliente envia credenciais via formulario OAuth2 para servidor
- Servidor verifica as credenciais
- Servidor envia token jwt para cliente
- Cliente acessa locais com o token
- Caso cliente envia credenciais erradas
- Servidor retorna erro

## Criando o endpoint

Para que os clientes se autentiquem na nossa aplicação, precisamos criar um endpoint que receba as credenciais. Vamos chama-lo de /token

- Precisamos de um schema de credenciais e um schema para o token
- Validar se o email existe e se sua senha bate com o hash
    - Caso não batam, retornar um erro
- Retornar um token com uma duração de tempo! (30 min?)

### Materiais para implementação

- Precisamos de um schema de credenciais e um schema para o token
    - Para schema de credenciais, o fastAPI conta com o *OAuth2PasswordRequestForm*
    - Para o retorno, vamos criar um novo schema chamado Token
- Validar se o email existe e se sua senha bate com o hash
    - Para isso podemos injetar a session com Depends
- Retornar um Token com uma duração de tempo! 
    - Para isso podemos usar o *datetime.timedelta*

Quando usamos formulários no FastAPI precisamos instalar uma biblioteca para multipart:

    poetry add python-multipart

## O Token JWT

JWT = Json Web Token (é uma forma de assinatura do servidor)

O token diz que o cliente foi autenticado com a assinatura **desse** servidor. Ele é dividido em 3 partes:

- Header: Json que tem o algoritmo e o tipo do token
- Payload: Dados que serão usados para assinatura
- Assinatura: Aplicação do algoritmo + chave secreta da aplicação

### O payload e as claims

    {
        "sub": "teste@test.com",    -> a quem dentro da aplicação o token pertence
        "exp": 1690258153           -> ate quando o token vale
    }

- sub (Subject): identifica o "assunto", basciamente uma forma de identificar o cliente. Pode ser um id, um uuid, email...
- exp (Expiration Time): tempo de expiração do token.



# Autorização

Garantir que somente pessoas autorizadas possam executar determinadas operações. Como:

- Alterar (PUT): Queremos garantir que o cliente possa alterar somente sua conta
- Deletar: Queremos garantir que o cliente possa deletar somente a sua conta