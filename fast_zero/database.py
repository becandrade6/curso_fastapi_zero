from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


# Assinalamos que não é pra testar isso pq usamos
# outro get_session nos testes
def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session
