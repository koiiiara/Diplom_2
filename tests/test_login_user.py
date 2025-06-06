import copy
import pytest
import allure

from constants import USER_LOGIN_WRONG_CREDS_ERROR_MESSAGE
from methods.user_methods import UserMethods
from helpers import generate_random_string


@allure.suite("User")
@allure.sub_suite("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Успешная авторизация пользователя")
    @allure.description("Проверка успешной авторизации пользователя с валидными данными")
    def test_login_user_valid_data_success(self, create_user):
        user_methods = UserMethods()
        email = create_user["email"]
        password = create_user["password"]
        status_code, response_json = user_methods.login_user(email, password)
        assert status_code == 200 and response_json["success"] == True

    @pytest.mark.parametrize("wrong_field", ["email", "password"])
    def test_login_user_with_wrong_creds_error(self, wrong_field, create_user):
        allure.dynamic.title(f"Авторизация пользователя без поля {wrong_field}")
        allure.dynamic.description(f"Проверка ошибки при авторизации пользователя без заполнения поля {wrong_field}")
        user_methods = UserMethods()
        user_data = copy.deepcopy(create_user)
        user_data[wrong_field] += generate_random_string(4)
        status_code, response_json = user_methods.login_user(user_data["email"], user_data["password"])
        assert (status_code == 401 and
                response_json["success"] == False and
                response_json["message"] == USER_LOGIN_WRONG_CREDS_ERROR_MESSAGE)
