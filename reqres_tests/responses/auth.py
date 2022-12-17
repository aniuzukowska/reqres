import os
import allure
from dotenv import load_dotenv
from requests import Response
from reqres_tests.schemas.reqres_schemas import SchemaCreateUser, SchemaLoginUnsuccessful, SchemaLoginSuccessful, SchemaUpdateUser
from pytest_voluptuous import S

load_dotenv()
TOKEN = os.getenv('token')


class AuthSuccessful:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def token(self):
        return self.response.json()['token']

    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step('Проверка статус-кода ответа сервера'):
                assert self.status_code() == 200
            with allure.step('Проверка токена пользователя в ответе сервера'):
                assert self.token() == TOKEN
            with allure.step('Проверка схемы ответа сервера'):
                assert self.json == S(SchemaLoginSuccessful)


class AuthUnSuccessful:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def error(self):
        return self.response.json()['error']

    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step('Проверка статус-кода ответа сервера'):
                assert self.status_code() == 400
            with allure.step('Проверка отсутствия токена пользователя в ответе сервера'):
                assert self.error() == 'Missing password'
            with allure.step('Проверка схемы ответа сервера'):
                assert self.json == S(SchemaLoginUnsuccessful)




