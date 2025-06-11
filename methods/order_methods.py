import allure
import requests

from constants import ORDER_URL, INGREDIENTS_URL


class OrderMethods:

    @allure.step("Создаем заказ")
    def create_order(self, ingredients, token):
        payload = {"ingredients": ingredients}
        if token:
            headers = {"Authorization": token}
            response = requests.post(ORDER_URL, data=payload, headers=headers)
        else:
            response = requests.post(ORDER_URL, data=payload)
        return response.status_code, response

    @allure.step("Получаем список всех ингредиентов")
    def get_ingredients(self):
        response = requests.get(INGREDIENTS_URL)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return None

    @allure.step("Получаем список всех заказов пользователя")
    def get_user_orders(self, token):
        if token:
            headers = {"Authorization": token}
            response = requests.get(ORDER_URL, headers=headers)
        else:
            response = requests.get(ORDER_URL)
        return response.status_code, response.json()
