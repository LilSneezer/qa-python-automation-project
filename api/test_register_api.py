import requests
from config.endpoints import AppUrls, ApiEndpoints
import os
from dotenv import load_dotenv

load_dotenv()
url = f"{AppUrls.BASE_API_URL}{ApiEndpoints.REGISTER}"

def test_success_register():
    payload = {
        "email": os.getenv("LOGIN_USER_EMAIL"),
        "password": os.getenv("LOGIN_USER_PASSWORD")
    }
    response = requests.post(url, json = payload)
    response_json = response.json()

    assert response.status_code == 200

    assert "id" in response_json
    assert "token" in response_json

    assert isinstance(response_json["id"], int)
    assert response_json["token"] != ""

def test_register_without_pass():
    payload = {
        "email": os.getenv("LOGIN_USER_EMAIL"),
        "password": ""
    }
    response = requests.post(url, json = payload)
    response_json = response.json()

    assert response.status_code == 400
    assert "error" in response_json
    assert response_json["error"] != ""

def test_register_without_login():
    payload = {
        "email": "",
        "password": os.getenv("LOGIN_USER_PASSWORD")
    }
    response = requests.post(url, json = payload)
    response_json = response.json()

    assert response.status_code == 400
    assert "error" in response_json
    assert response_json["error"] != ""

def test_register_with_incorrect_login():
    payload = {
        "email": os.getenv("INCORRECT_LOGIN_USER_EMAIL"),
        "password": os.getenv("LOGIN_USER_PASSWORD")
    }
    response = requests.post(url, json = payload)
    response_json = response.json()

    assert response.status_code == 400
    assert "error" in response_json
    assert response_json["error"] != ""

def test_register_with_incorrect_pass():
    payload = {
        "email": os.getenv("LOGIN_USER_EMAIL"),
        "password": os.getenv("INCORRECT_LOGIN_USER_PASSWORD")
    }
    response = requests.post(url, json = payload)
    response_json = response.json()

    assert response.status_code == 400
    assert "error" in response_json
    assert response_json["error"] != ""

