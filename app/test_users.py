import pytest
from jose import jwt
from app import schemas

from config import settings


def test_root(client):

     res = client.get("/")
     print(res.json().get('message'))
     assert res.json().get('message') == 'Hello World'
     assert res.status_code == 200


