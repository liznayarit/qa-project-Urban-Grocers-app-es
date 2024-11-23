import configuration
import requests
import data



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(kit_body):
    headers = data.headers.copy()
    auth_token = post_new_user(data.user_body)
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=kit_body,  # inserta el cuerpo de solicitud
                         headers=headers)  # inserta los encabezados

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())


