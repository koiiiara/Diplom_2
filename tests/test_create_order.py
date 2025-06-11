import allure

from constants import ORDER_CREATE_NO_INGREDIENTS_ERROR_MESSAGE
from helpers import get_random_ingredients_ids
from methods.order_methods import OrderMethods

@allure.suite("Order")
@allure.sub_suite("Создание заказа")
class TestCreateOrder:

    @allure.title(f"Создание заказа с авторизацией")
    @allure.description(f"Проверка успешного создания заказа с авторизацией")
    def test_create_order_auth_success(self, create_user):
        token = create_user["token"]
        ingredients = get_random_ingredients_ids(3)
        order_methods = OrderMethods()
        status_code, response = order_methods.create_order(ingredients, token)
        assert status_code == 200 and response.json()["success"] == True

    @allure.title(f"Создание заказа без авторизации")
    @allure.description(f"Проверка успешного создания заказа без авторизации")
    def test_create_order_no_auth_success(self, create_user):
        ingredients = get_random_ingredients_ids(3)
        order_methods = OrderMethods()
        status_code, response = order_methods.create_order(ingredients, "")
        assert (status_code == 200
                and response.json()["success"] == True
                and "_id" not in response.json()["order"] )

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
