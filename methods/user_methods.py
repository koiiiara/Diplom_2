import requests
from constants import USER_REGISTER_URL, USER_URL, USER_LOGIN_URL


class UserMethods:

    def create_user(self, email, name, password):
        payload = {}
        if name:
            payload["name"] = name
        if password:
            payload["password"] = password
        if email:
            payload["email"] = email

        response = requests.post(USER_REGISTER_URL, data=payload)
        return response.status_code, response.json()

    def delete_user(self, token):
        headers = {
            'Authorization': token,
        }
        response = requests.delete(USER_URL, headers=headers)
        return response.status_code, response.json()

    def login_user(self, email, password):
        payload = {}
        if password:
            payload["password"] = password
        if email:
            payload["email"] = email

        response = requests.post(USER_LOGIN_URL, data=payload)
        return response.status_code, response.json()

    def edit_user(self, token, email=None, name=None, password=None):
        payload = {}
        if name:
            payload["name"] = name
        if password:
            payload["password"] = password
        if email:
            payload["email"] = email

        if token:
            headers = {"Authorization": token}
            response = requests.patch(USER_URL, headers=headers, data=payload)
        else:
            response = requests.patch(USER_URL, data=payload)
        return response.status_code, response.json()

    def get_user_info(self, token):
        headers = {
            'Authorization': token,
        }
        response = requests.get(USER_URL, headers=headers)
        return response.status_code, response.json()
