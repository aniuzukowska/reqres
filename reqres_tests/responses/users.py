import allure
from pytest_voluptuous import S
from requests import Response

from reqres_tests.schemas.reqres_schemas import SchemaCreateUser, SchemaUpdateUser


class CreatedUser:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def name(self):
        return self.response.json()['name']

    def job(self):
        return self.response.json()['job']

    def assert_(self, new_user_name, new_user_job):
        with allure.step('Проверка результата'):
            with allure.step('Проверка статус-кода ответа сервера'):
                assert self.status_code() == 201
            with allure.step('Проверка имени пользователя в ответе сервера'):
                assert self.name() == new_user_name
            with allure.step('Проверка наименования работы в ответе сервера'):
                assert self.job() == new_user_job
            with allure.step('Проверка схемы ответа сервера'):
                assert self.json == S(SchemaCreateUser)


class UpdatedUser:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def name(self):
        return self.response.json()['name']

    def job(self):
        return self.response.json()['job']

    def assert_(self, new_name, new_job):
        with allure.step("Проверяем результат"):
            with allure.step('Проверка статус-кода ответа сервера'):
                assert self.status_code() == 200
            with allure.step('Проверка имени пользователя в ответе сервера'):
                assert self.name() == new_name
            with allure.step('Проверка наименования работы в ответе сервера'):
                assert self.job() == new_job
            with allure.step('Проверка схемы ответа сервера'):
                assert self.json == S(SchemaUpdateUser)



class DeletedUser:
    def __init__(self, response: Response):
        self.response = response

    def status_code(self):
        return self.response.status_code

    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step('Проверка статус-кода ответа сервера'):
                assert self.status_code() == 204


