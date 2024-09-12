from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='becandrade', email='mail@mail.com', password='senha123'
    )

    # Cria um espaço de staging que vai adicionando ali
    # (area de transferencia) até dar commit
    session.add(user)
    # Pega tudo que demos add e faz a persistência
    session.commit()

    # Session, vai la no DB e pega um registro
    # O scalar faz o mapeamento e retorna o objeto python ja
    result = session.scalar(select(User).where(User.email == 'mail@mail.com'))

    # Atualiza o objeto user com os dados criados la no DB
    # "Sincroniza" esse objeto com o do DB
    # session.refresh(user)

    assert result.username == 'becandrade'
