from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


# Mapeamos a classe de dados para que seja compativel com o banco
# Usamos o Mapped para mapear e o mapped_column para falar coisas do SQL
# init=False diz que ele(banco)que vai ir preenchendo esse cara, nao passo o id
# func.now() é uma função do sqlalchemy que vai pegar o horario atual la
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
