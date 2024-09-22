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
    assert response.json()["name"] == kit_body["name"]

# Función para aserciones negativas
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()  # Obtener el token del usuario
    response = post_new_client_kit(kit_body, auth_token)  # Crear el kit
    assert response.status_code == 400


# Pruebas
def test_kit_name_min_length():
    kit_body = get_kit_body(data.one_letter)
    positive_assert(kit_body)

def test_kit_name_max_length():
    kit_body = get_kit_body(data.max_length)
    positive_assert(kit_body)

def test_kit_name_empty():
    kit_body = get_kit_body(data.name_empty)
    negative_assert_code_400(kit_body)

def test_kit_name_too_long():
    kit_body = get_kit_body(data.too_long)
    negative_assert_code_400(kit_body)

def test_kit_name_special_characters():
    kit_body = get_kit_body(data.special_characters)
    positive_assert(kit_body)

def test_kit_name_with_spaces():
    kit_body = get_kit_body(data.name_with_spaces)
    positive_assert(kit_body)

def test_kit_name_numbers():
    kit_body = get_kit_body(data.name_numbers)
    positive_assert(kit_body)

def test_kit_name_missing_parameter():
    negative_assert_code_400(data.missing_parameter)

def test_kit_name_wrong_type():
    kit_body = get_kit_body(data.name_wrong_type)
    negative_assert_code_400(kit_body)