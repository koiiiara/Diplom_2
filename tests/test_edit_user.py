import copy

import pytest
import allure

from constants import USER_EDIT_NO_AUTH_ERROR_MESSAGE
from methods.user_methods import UserMethods
from helpers import generate_random_string


@allure.suite("User")
@allure.sub_suite("Изменение данных пользователя")
class TestEditUser:

    @pytest.mark.parametrize("edit_field", ["email", "name", "password"])
    def test_edit_user_with_auth_success(self, create_user, edit_field):
        allure.dynamic.title(f"Изменение поля {edit_field} авторизованного пользователя")
        allure.dynamic.description(
            f"Проверка успешного изменения поля {edit_field} в информации авторизованного пользователя")
        user_methods = UserMethods()
        user_data = copy.deepcopy(create_user)
        user_data[edit_field] = generate_random_string(4) + user_data[edit_field]
        status_code, response_json = user_methods.edit_user(user_data["token"],
                                                            user_data["email"],
                                                            user_data["name"],
                                                            user_data["password"])
        response_user_data = response_json["user"]
        assert (status_code == 200 and response_json["success"] == True
                and response_user_data["name"] == user_data["name"]
                and response_user_data["email"] == user_data["email"])

    @pytest.mark.parametrize("edit_field", ["email", "name", "password"])
    def test_edit_user_no_auth_error(self, generate_user_for_create, edit_field):
        allure.dynamic.title(f"Изменение поля {edit_field} неавторизованного пользователя")
        allure.dynamic.description(
            f"Проверка ошибки при попытке изменения поля {edit_field} неавторизованного пользователя")
        user_methods = UserMethods()
        user_data = copy.deepcopy(generate_user_for_create)
        user_data[edit_field] = generate_random_string(4) + user_data[edit_field]
        status_code, response_json = user_methods.edit_user("",
                                                            user_data["email"],
                                                            user_data["name"],
                                                            user_data["password"])
        assert (status_code == 401 and
                response_json["success"] == False and
                response_json["message"] == USER_EDIT_NO_AUTH_ERROR_MESSAGE)
