
import pytest
from jose import jwt
from app import schemas
from app.main import app
from fastapi.testclient import TestClient
from app.config import settings

client = TestClient(app)

def test_root():

     res = client.get("/")
     print(res.json().get('message'))
     assert res.json().get('message') == "Welcome to our QA engineering fastapi: In '/docs' you can see Documentation (c) Anush Avanesyan"
     assert res.status_code == 200