import random
import string

from methods.order_methods import OrderMethods


def generate_user():
    # генерируем email, пароль и имя пользователя
    email = generate_random_string(10) + "@" + "yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    # возвращаем список
    return {
        "email": email,
        "password": password,
        "name": name
    }


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def get_random_ingredients_ids(count):
    order_methods = OrderMethods()
    ingredients_full = order_methods.get_ingredients()
    ingredients = []
    for i in range(count):
        ingredient = random.choice(ingredients_full)
        ingredients.append(ingredient["_id"])
    return ingredients
