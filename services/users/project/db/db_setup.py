from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from project.api.models import Base

engine = create_engine("postgresql://postgres:postgres@users-db:5432/users", future=True)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

with engine.begin() as conn:
    Base.metadata.create_all(conn)