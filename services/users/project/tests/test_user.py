from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..main import app, Base, engine, get_settings
import os
import json
from ..config import Settings, get_settings

def get_settings():
    settings = Settings(db_url=os.environ.get("test_db_url"))
    print(f"Loading settings: {settings.env_name}")
    return settings


app.dependency_overrides[get_settings] = get_settings()

@app.on_event("startup")
async def startup_event():
    with engine.begin() as conn:
        Base.metadata.create_all(conn)

@app.on_event("shutdown")
def shutdown_event():
    with engine.begin() as conn:
        Base.metadata.drop_all(bind=engine)

def test_client():
    with TestClient(app) as client:
        response = client.post('/users/', json = {"username": "lixach", "email": "ex@ex.com"})
    assert response.status_code == 201
    assert response.json() == {"username": "lixach", "email": "ex@ex.com"}