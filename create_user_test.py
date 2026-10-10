import sender_stand_request
import data 
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body 

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == (
        "Имя пользователя введено некорректно. Имя может содержать только "
        "русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов"
    )


def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"
    # Тест 1. Успешное создание пользователя
    # Параметр firstName состоит из 2 символов
def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    # Тест 2. Успешное создание пользователя
# Параметр firstName состоит из 15 символов
def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Ааааааааааааааа")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
# Тест 3. Ошибка
# Параметр firstName состоит из 1 символа
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("А")
    # Тест 4. Ошибка
# Параметр firstName состоит из 16 символов
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")
    # Тест 5. Успешное создание пользователя
# Параметр firstName состоит из английских букв
def test_create_user_english_letter_in_first_name_get_success_response():
    user_body = get_user_body("QWErty")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    # Тест 6. Успешное создание пользователя
# Параметр firstName состоит из русских букв
def test_create_user_russian_letter_in_first_name_get_success_response():
    user_body = get_user_body("Мария")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    # Тест 7. Ошибка
# Параметр firstName состоит из строки с пробелом
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Человек и Ко")
    # Тест 8. Ошибка
# Параметр firstName состоит из строки со спецсимволами
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")
    # Тест 9. Ошибка
# Параметр firstName состоит из строки с цифрами
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")
    # Тест 10. Ошибка
# В запросе нет параметра firstName
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)
    # Тест 11. Ошибка
# Параметр firstName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)
    # Тест 12. Ошибка
# Тип параметра firstName — число
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
