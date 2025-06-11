import pytest
import allure

from constants import GET_ORDER_NO_AUTH_ERROR_MESSAGE
from methods.order_methods import OrderMethods


@allure.suite("Order")
@allure.sub_suite("Получение списка заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов пользователя с авторизацией")
    @allure.description("Проверка успешного получения списка заказов конкретного пользователя с авторизацией")
    def test_get_user_orders_auth_success(self, create_orders):
        user_date, orders = create_orders
        token = user_date["token"]
        order_methods = OrderMethods()
        status_code, response_json = order_methods.get_user_orders(token)
        assert status_code == 200 and len(response_json["orders"]) == len(orders)

    @allure.title("Получение списка заказов пользователя без авторизации")
    @allure.description("Проверка ошибки при попытке получения списка заказов конкретного пользователя без авторизации")
    def test_get_user_orders_no_auth_error(self, create_orders):
        _, orders = create_orders
        order_methods = OrderMethods()
        status_code, response_json = order_methods.get_user_orders("")
        assert (status_code == 401 and
                response_json["success"] == False and
                response_json["message"] == GET_ORDER_NO_AUTH_ERROR_MESSAGE)
