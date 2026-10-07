import requests
from config.endpoints import AppUrls, ApiEndpoints

url = f"{AppUrls.BASE_API_URL}{ApiEndpoints.USERS}"

def test_status_code_is_200():
    """Тест 1: Проверка успешного кода ответа (200 OK)"""
    # 1. Отправляем GET-запрос к эндпоинту
    response = requests.get(f"{url}/2")
    
    # 2. Проверяем, что сервер вернул статус 200
    assert response.status_code == 200


def test_user_data_contains_correct_fields():
    """Тест 2: Проверка структуры и конкретных данных пользователя"""
    response = requests.get(f"{url}/2")
    
    # Превращаем JSON-ответ сервера в удобный словарь Python
    response_json = response.json()
    
    # Проверяем, что в ответе есть блок 'data'
    assert "data" in response_json
    
    # Извлекаем данные пользователя
    user_data = response_json["data"]
    
    # Проверяем конкретные значения полей для пользователя с ID 2
    assert user_data["id"] == 2
    assert user_data["email"] == "janet.weaver@reqres.in"
    assert user_data["first_name"] == "Janet"
    assert user_data["last_name"] == "Weaver"


def test_response_headers():
    """Тест 3: Проверка заголовков ответа (Headers)"""
    response = requests.get(f"{url}/2")
    
    # Проверяем тип контента — сервер должен возвращать именно JSON
    assert "application/json" in response.headers["Content-Type"]
    
    # Проверяем, что в заголовках присутствует имя сервера
    assert "Server" in response.headers