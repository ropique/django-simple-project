from ast import main
from fastapi import FastAPI
import pytest
from ..app import main 
from fastapi.testclient import TestClient

client = TestClient(main.app)

def test_root():

     res = client.get("/")
     print(res.json().get('message'))
     assert res.json().get('message') == "Welcome to our QA engineering fastapi: In '/docs' you can see Documentation (c) Anush Avanesyan"
     assert res.status_code == 200


