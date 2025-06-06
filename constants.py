BASE_URL = "https://stellarburgers.nomoreparties.site/api"
USER_URL = BASE_URL + "/auth/user"
USER_LOGIN_URL = BASE_URL + "/auth/login"
USER_REGISTER_URL = BASE_URL + "/auth/register"
ORDER_URL = BASE_URL + "/orders"
INGREDIENTS_URL = BASE_URL + "/ingredients"


USER_EXIST_ERROR_MESSAGE = 'User already exists'
USER_CREATE_MISSING_CREDS_ERROR_MESSAGE = 'Email, password and name are required fields'
USER_LOGIN_WRONG_CREDS_ERROR_MESSAGE = 'email or password are incorrect'
USER_EDIT_NO_AUTH_ERROR_MESSAGE = 'You should be authorised'
ORDER_CREATE_NO_INGREDIENTS_ERROR_MESSAGE = 'Ingredient ids must be provided'
GET_ORDER_NO_AUTH_ERROR_MESSAGE = 'You should be authorised'