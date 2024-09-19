import data
import pytest
from sender_stand_request import post_new_user, post_new_client_kit



def get_new_user_token():
    user_body = data.user_body.copy()
    response = post_new_user(user_body)
    if response.status_code==201:
        return response.json().get('authToken')
    else:
        pytest.fail(f"Error al crear usuario. Código de estado:{response.status_code}, Respuesta:{response.json()}")

def get_kit_body(name):
    return {
        "name": name,
        "card": {
            "id": 1,
            "nombre": "Para la situación"
        },
        "productsList": None,
        "id": 1,
        "productsCount": 0
    }
def positive_assert(kit_body):
    auth_token = get_new_user_token()  # Obtener el token del usuario
    response = post_new_client_kit(kit_body, auth_token)  # Crear el kit
    assert response.status_code == 201
    assert response.json().get("name") == kit_body["name"]
    print()
    print(f"Código de respuesta {response.status_code}")
# Función para aserciones negativas
def negative_assert_code_400(kit_body):
    response = post_new_user(kit_body)
    assert response.status_code == 400
    print()
    print(f"Código de respuesta {response.status_code}")

# Pruebas
def test_kit_name_min_length():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_kit_name_max_length():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

def test_kit_name_empty():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_kit_name_too_long():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

def test_kit_name_special_characters():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

def test_kit_name_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_kit_name_missing_parameter():
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_kit_name_wrong_type():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)