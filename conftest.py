import pytest

from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from helpers import generate_user, get_random_ingredients_ids


@pytest.fixture()
def generate_user_for_create():
    user_data = generate_user()
    yield user_data
    user_methods = UserMethods()
    if "token" in user_data:
        info_status_code, _ = user_methods.get_user_info(user_data["token"])
        if info_status_code == 200:
            del_status_code, del_response = user_methods.delete_user(user_data["token"])
            if del_status_code != 202:
                raise RuntimeError(
                    f"Не удалось удалить тестового пользователя после теста: {del_status_code}, {del_response}"
                )


@pytest.fixture
def create_user(generate_user_for_create):
    user_methods = UserMethods()
    email = generate_user_for_create["email"]
    password = generate_user_for_create["password"]
    name = generate_user_for_create["name"]
    status_code, response_json = user_methods.create_user(email, name, password)
    if status_code == 200:
        generate_user_for_create["token"] = response_json["accessToken"]
        yield generate_user_for_create
    else:
        raise RuntimeError(
            f"Не удалось создать пользователя: {status_code}, {response_json}"
        )


@pytest.fixture()
def create_orders(create_user):
    token = create_user["token"]
    order_methods = OrderMethods()

    ingredients_sets = [get_random_ingredients_ids(3),
                        get_random_ingredients_ids(5)]
    orders = []
    for ingredient_set in ingredients_sets:
        _, result = order_methods.create_order(ingredient_set, token)
        orders.append(result)
    return create_user, orders
