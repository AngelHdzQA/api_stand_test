import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_users_table ():
    return requests.get(configuration.URL_SERVICE+configuration.USERS_TABLE_PATH)
""""
def post_new_user(body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
"""
""""
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
"""


"""response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())#"""


"""def post_products_kit(product_ids):
    return requests.post(configuration.URL_SERVICE+configuration.PRODUCT_KITS_PATH,
                         json=product_ids,
                         headers=data.headers)
response = post_products_kit(data.product_ids)
print(response.status_code)
print(response.json())"""



