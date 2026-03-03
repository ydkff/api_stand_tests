
import configuration
import requests
import data


def post_new_user(body):             # Crea un nuevo usuario en el sistem
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def get_users_table():              # Obtiene todos los usuarios registrados en la tabla
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)