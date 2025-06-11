import copy
import pytest
import allure

from constants import USER_EXIST_ERROR_MESSAGE, USER_CREATE_MISSING_CREDS_ERROR_MESSAGE
from methods.user_methods import UserMethods


@allure.suite("User")
@allure.sub_suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания уникального пользователя с валидными данными")
    def test_create_user_valid_data_success(self, generate_user_for_create):
        user_methods = UserMethods()
        email = generate_user_for_create["email"]
        password = generate_user_for_create["password"]
        name = generate_user_for_create["name"]
        status_code, response_json = user_methods.create_user(email, name, password)
        assert status_code == 200 and response_json["success"] == True

    @allure.title("Создание дубликата пользователя")
    @allure.description("Проверка ошибки при создании пользователя с уже существующими реквизитами")
    def test_create_user_duplicate_error(self, create_user):
        user_methods = UserMethods()
        email = create_user["email"]
        password = create_user["password"]
        name = create_user["name"]
        status_code, response_json = user_methods.create_user(email, name, password)
        assert (status_code == 403 and
                response_json["success"] == False and
                response_json["message"] == USER_EXIST_ERROR_MESSAGE)

    @pytest.mark.parametrize("empty_field", ["name", "password"])
    def test_create_courier_without_login_error(self, generate_user_for_create, empty_field):
        allure.dynamic.title(f"Создание пользователя без поля {empty_field}")
        allure.dynamic.description(f"Проверка ошибки при создании пользователя без заполнения поля {empty_field}")
        user_methods = UserMethods()
        user_data = copy.deepcopy(generate_user_for_create)
        user_data[empty_field] = None
        status_code, response_json = user_methods.create_user(user_data["email"],
                                                              user_data["password"],
                                                              user_data["name"])
        assert (status_code == 403 and
                response_json["success"] == False and
                response_json["message"] == USER_CREATE_MISSING_CREDS_ERROR_MESSAGE)
