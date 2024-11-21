import sender_stand_request
import data

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # Comprobar que el resultado de la solicitud se guarda en users_table_response
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(first_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"







    # Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
    def get_kit_body(name):
        # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
        current_body = data.kit_body.copy()
        # Se cambia el valor del parámetro name
        current_body["name"] = name
        # Se devuelve un nuevo diccionario con el valor name requerido
        return current_body


    # Función de prueba positiva
    def positive_assert(name):
        # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
        kit_body = get_kit_body(name)
        # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
        kit_response = sender_stand_request.post_new_client_kit(kit_body)

        # Comprueba si el código de estado es 201
        assert kit_response.status_code == 201
        # Comprueba que el campo authToken está en la respuesta y contiene un valor
        assert kit_response.json()["authToken"] != ""

        # Comprobar que el resultado de la solicitud se guarda en users_table_response
        users_table_response = sender_stand_request.get_users_table()

        # String que debe estar en el cuerpo de respuesta
        str_kit = kit_body["name"] + ",,," + user_response.json()["authToken"]

        # Comprueba si el usuario o usuaria existe y es único/a
        assert users_table_response.text.count(str_kit) == 1

    # Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
    def negative_assert_symbol(name):
        # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
        kit_body = get_kit_body(name)

        # El resultado se guarda en la variable response
        response = sender_stand_request.post_new_client_kit(kit_body)

        # Comprueba si el código de estado es 400
        assert response.status_code == 400

        # Comprueba que el atributo code en el cuerpo de respuesta es 400
        assert response.json()["code"] == 400
        # Comprueba el atributo message en el cuerpo de respuesta
        assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos. " \


    # Función de prueba negativa cuando el error es ""No se han aprobado todos los parámetros requeridos""
    def negative_assert_no_name(kit_body):
        # El resultado se guarda en la variable response
        response = sender_stand_request.post_new_client_kit(kit_body)

        # Comprueba si el código de estado es 400
        assert response.status_code == 400

        # Comprueba que el atributo code en el cuerpo de respuesta es 400
        assert response.json()["code"] == 400
        # Comprueba el atributo message en el cuerpo de respuesta
        assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

    # Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
    def test_create_kit_1_letter_in_name_get_success_response():
        positive_assert(data.one_letter)

    # Prueba 2. Kit creado con éxito. El parámetro name contiene 15 caracteres
    def test_create_kit_511_letter_in_name_get_success_response():
        positive_assert(data.kit_511_letter)

    # Prueba 3. Error. El parámetro contiene un string vacío
    def test_create_kit_empty_name_get_error_response():
        # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
        kit_body = get_kit_body(data.kit_vacio)
        # Comprueba la respuesta
        negative_assert_no_name(kit_body)

    # Prueba 4. Error. El parámetro name contiene 512 carácteres
    def test_create_kit_512_letter_in_name_get_error_response():
        negative_assert_symbol(data.kit_512_letter)

    # Prueba 5. Error. El parámetro name contiene un string de caracteres especiales
    def test_create_kit_has_special_symbol_in_name_get_error_response():
        positive_assert(data.kit_caract_special)

    # Prueba 6. Error
    # El parámetro "name" contiene palabras con espacios
    def test_create_kit_has_space_in_name_get_error_response():
        positive_assert(data.kit_spacio)

    # Prueba 7. Error. El parámetro name permite numeros
    def test_create_kit_has_number_in_name_get_error_response():
        positive_assert(data.kit_number)

    # Prueba 8. Error. Falta el parámetro name en la solicitud
    def test_create_kit_no_name_get_error_response():
        # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
        kit_body = data.kit_body.copy()
        # El parámetro "name" se elimina de la solicitud
        kit_body.pop("name")
        # Comprueba la respuesta
        negative_assert_no_name(kit_body)

    # Prueba 9. Error. Se ha pasado un tipo de parámetro diferente (número)
    def test_create_kit_diferent_in_name_get_error_response():
            negative_assert_symbol(data.kit_diferent)






