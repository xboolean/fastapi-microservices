import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:postgres@users-db:5432/users')
Session = sessionmaker(engine)



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

with engine.begin() as conn:
    Base.metadata.create_all(conn)

app = FastAPI()

@app.get('/users/ping/')
async def ping_pong():
    return {"ping": "pong"}