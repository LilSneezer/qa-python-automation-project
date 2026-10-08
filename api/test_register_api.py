import allure
import requests
from config.endpoints import AppUrls, ApiEndpoints
import os
from dotenv import load_dotenv

load_dotenv()
url = f"{AppUrls.BASE_API_URL}{ApiEndpoints.REGISTER}"

@allure.title("Проверка успешной регистрации с валидными данными")
def test_success_register():
    with allure.step("1. Подготовка тестовых данных"):
        payload = {
            "email": os.getenv("LOGIN_USER_EMAIL"),
            "password": os.getenv("LOGIN_USER_PASSWORD")
        }
    with allure.step("2. Отправка POST-запроса на сервер"):
        response = requests.post(url, json = payload)
        response_json = response.json()
        
    with allure.step("3. Проверка статус-кода и токена в ответе"):
        assert response.status_code == 200

        assert "id" in response_json
        assert "token" in response_json

        assert isinstance(response_json["id"], int)
        assert response_json["token"] != ""

@allure.title("Проверка неуспешной регистрации без пароля")
def test_register_without_pass():
    with allure.step("1. Подготовка тестовых данных"):
        payload = {
            "email": os.getenv("LOGIN_USER_EMAIL"),
            "password": ""
        }
    with allure.step("2. Отправка POST-запроса на сервер"):
        response = requests.post(url, json = payload)
        response_json = response.json()

    with allure.step("3. Проверка статус-кода и наличие ошибки"):
        assert response.status_code == 400
        assert "error" in response_json
        assert response_json["error"] != ""

@allure.title("Проверка неуспешной регистрации без логина")
def test_register_without_login():
    with allure.step("1. Подготовка тестовых данных"):
        payload = {
            "email": "",
            "password": os.getenv("LOGIN_USER_PASSWORD")
        }

    with allure.step("2. Отправка POST-запроса на сервер"):
        response = requests.post(url, json = payload)
        response_json = response.json()

    with allure.step("3. Проверка статус-кода и наличие ошибки"):
        assert response.status_code == 400
        assert "error" in response_json
        assert response_json["error"] != ""

@allure.title("Проверка неуспешной регистрации с некорректным логином")
def test_register_with_incorrect_login():
    with allure.step("1. Подготовка тестовых данных"):
        payload = {
            "email": os.getenv("INCORRECT_LOGIN_USER_EMAIL"),
            "password": os.getenv("LOGIN_USER_PASSWORD")
        }

    with allure.step("2. Отправка POST-запроса на сервер"):
        response = requests.post(url, json = payload)
        response_json = response.json()

    with allure.step("3. Проверка статус-кода и наличие ошибки"):
        assert response.status_code == 400
        assert "error" in response_json
        assert response_json["error"] != ""

@allure.title("Проверка неуспешной регистрации с некорректным паролем")
def test_register_with_incorrect_pass():
    with allure.step("1. Подготовка тестовых данных"):
        payload = {
            "email": os.getenv("LOGIN_USER_EMAIL"),
            "password": os.getenv("INCORRECT_LOGIN_USER_PASSWORD")
        }

    with allure.step("2. Отправка POST-запроса на сервер"):
        response = requests.post(url, json = payload)
        response_json = response.json()

    with allure.step("3. Проверка статус-кода и наличие ошибки"):
        assert response.status_code == 400
        assert "error" in response_json
        assert response_json["error"] != ""

