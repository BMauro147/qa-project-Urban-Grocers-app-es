import configuration
import data
import requests


def post_new_user(body):
    response= requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers)
    return response


def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()  # Usar los encabezados definidos en data.py
    headers["Authorization"] = f"Bearer {auth_token}"  # Añadir el token de autenticación

    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers)

    return response
