import allure
import requests
from config.endpoints import AppUrls, ApiEndpoints

url = f"{AppUrls.BASE_API_URL}{ApiEndpoints.USERS}"

@allure.title("Проверка успешного получения данных пользователя")
def test_status_code_is_200():
    with allure.step("1. Отправка GET-запроса на сервер"):
        response = requests.get(f"{url}/2")
    
    with allure.step("2. Проверка статус-кода в ответе"):
        assert response.status_code == 200

@allure.title("Проверка структуры и конкретных данных пользователя")
def test_user_data_contains_correct_fields():
    with allure.step("1. Отправка GET-запроса на сервер"):
        response = requests.get(f"{url}/2")

    with allure.step("2. Превращаем JSON-ответ сервера в объект Python"):
        response_json = response.json()

    with allure.step("3. Проверяем, что в ответе есть блок 'data'"):
        assert "data" in response_json

    with allure.step("4. Извлекаем данные пользователя"):
        user_data = response_json["data"]

    with allure.step("5. Проверяем конкретные значения полей для пользователя с ID 2"):
        assert user_data["id"] == 2
        assert user_data["email"] == "janet.weaver@reqres.in"
        assert user_data["first_name"] == "Janet"
        assert user_data["last_name"] == "Weaver"

@allure.title("Проверка заголовков ответа (Headers)")
def test_response_headers():
    with allure.step("1. Отправка GET-запроса на сервер"):
        response = requests.get(f"{url}/2")

    with allure.step("2. Проверям, что тип контента - application/json"):
        assert "application/json" in response.headers["Content-Type"]

    with allure.step("3. Проверяем, что в заголовках присутствует имя сервера"):
        assert "Server" in response.headers