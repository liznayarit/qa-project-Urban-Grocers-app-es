import sender_stand_request
import data



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
        # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
        kit_response = sender_stand_request.post_new_client_kit(kit_body)

        # Comprueba si el código de estado es 201
        assert kit_response.status_code == 201
        assert kit_response.json()["name"] == name









    # Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
    def negative_assert_symbol(name):
        # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
        kit_body = get_kit_body(name)

        # El resultado se guarda en la variable response
        response = sender_stand_request.post_new_client_kit(kit_body)

        # Comprueba si el código de estado es 400
        assert response.status_code == 400






    # Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
    def test_create_kit_1_letter_in_name_get_success_response():
        positive_assert(data.one_letter)

    # Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
    def test_create_kit_511_letter_in_name_get_success_response():
        positive_assert(data.kit_511_letter)

    # Prueba 3. Error. El parámetro contiene un string vacío
    def test_create_kit_empty_name_get_error_response():
        negative_assert_symbol(data.kit_vacio)

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
        negative_assert_symbol(None)

    # Prueba 9. Error. Se ha pasado un tipo de parámetro diferente (número)
    def test_create_kit_diferent_in_name_get_error_response():
            negative_assert_symbol(data.kit_diferent)






