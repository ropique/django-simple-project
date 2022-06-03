from fastapi import FastAPI
import pytest
from app.main import app
from fastapi.testclient import TestClient
from jose import jwt
from app import schemas
from app.config import settings

client = TestClient(app)


def test_root():

     res = client.get("/")
    #  res = client.get("https://fastapi-anush.herokuapp.com/")
     print(res.json().get('message'))
     assert res.json().get('message') == "Welcome to our QA engineering fastapi: In '/docs' you can see Documentation (c) Anush Avanesyan"
     assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/", json={"email": "test@gmail.com", "password": "password123", "company": "IM"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@gmail.com"
    assert res.status_code == 201


