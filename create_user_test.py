import requests
import data
import pytest
import sender_stand_request_POST


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body['first_name'] = first_name
    return current_body


def possitive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request_POST.post_new_user(user_body)
    print(user_response.json())
    print(user_response.status_code)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request_POST.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request_POST.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

def negative_assert_no_first_name(user_body):
    response = sender_stand_request_POST.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros necesarios"

#PRUEBA 1
def test_create_user_2_letter_in_first_name_get_success_response():
    possitive_assert("Dg")
#PRUEBA 2
def test_create_user_15_letter_in_first_name_get_success_response():
   possitive_assert("Aaaaaaaaaaaaaaa") #15 caracteres
#PRUEBA 3
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")
#PRUEBA 4
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa") #16 caracteres
#Prueba 5
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A aa")
#Prueba 6
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")
#Prueba 7
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")
#PRUEBA 8
def test_create_user_no_first_name_get_error_response():
    user_body= data.user_body.copy()
    user_body.pop("first_name")
    negative_assert_no_first_name(user_body)
#PRUEBA 9
def test_create_user_empty_first_name_get_error_response():
    user_body=get_user_body("")
    negative_assert_no_first_name(user_body)
#PRUEBA 10
def test_create_user_number_type_first_name_get_error_response():
    user_body=get_user_body(12)
    response=sender_stand_request_POST.post_new_user(user_body)
    assert response.status_code == 400



""""
def test_create_user_2_letter_in_first_name_get_success_response():
    # La versión actualizada del cuerpo de solicitud que contiene el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body("Aa")
    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request_POST.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request_POST.get_users_table()
    # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1
    
"""
