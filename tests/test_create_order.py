import allure
import pytest

from constants import ORDER_CREATE_NO_INGREDIENTS_ERROR_MESSAGE
from helpers import get_random_ingredients_ids
from methods.order_methods import OrderMethods

@allure.suite("Order")
@allure.sub_suite("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("auth", [True, False])
    def test_create_order_auth_success(self, create_user, auth):
        if auth:
            token = create_user["token"]
            allure_substring = "с авторизацией"
        else:
            token = ""
            allure_substring = "без авторизации"
        allure.dynamic.title(f"Создание заказа {allure_substring}")
        allure.dynamic.description(f"Проверка успешного создания заказа {allure_substring} пользователя")

        ingredients = get_random_ingredients_ids(3)
        order_methods = OrderMethods()
        status_code, response = order_methods.create_order(ingredients, token)
        assert status_code == 200 and response.json()["success"] == True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки при создании заказа без ингредиентов")
    def test_create_order_no_ingredients_error(self, create_user):
        token = create_user["token"]
        order_methods = OrderMethods()
        status_code, response = order_methods.create_order([], token)
        assert (status_code == 400 and
                response.json()["success"] == False and
                response.json()["message"] == ORDER_CREATE_NO_INGREDIENTS_ERROR_MESSAGE)

    @allure.title("Создание заказа с неверным id ингредиента")
    @allure.description("Проверка ошибки при создании заказа с неверным id ингредиента")
    def test_create_order_wrong_ingredients_error(self, create_user):
        token = create_user["token"]
        order_methods = OrderMethods()
        ingredients = [
            "00000000",
            "11111111"
        ]
        status_code, _ = order_methods.create_order(ingredients, token)
        assert status_code == 500
