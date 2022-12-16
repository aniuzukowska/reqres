import os
import allure
from requests import Response
from reqres_tests.utils import attach
from reqres_tests.utils.base_session import BaseSession


class Reqres:
    def __init__(self):
        self.reqres = BaseSession(base_url=os.getenv('api_url'))

    def login(self, login, password) -> Response:
        with allure.step("Выполнение авторизации"):
            response = self.reqres.post(
                url='/api/login',
                json={
                   "email": login,
                   "password": password
                }
         )
            attach.add_body_request(response)
            attach.add_curl(response)
            attach.add_response(response)
        return response

    def get_token(self, login, password):
        with allure.step("Получаем токен авторизации"):
            response = self.reqres.post(
                url='/api/login',
                json={
                    "email": login,
                    "password": password
                }
            )
            attach.add_comment('Получен token', f'{response.json()["token"]}')
            return {'token': f'{response.json()["token"]}'}

    def create_user(self, name, job, token) -> Response:
        with allure.step("Добавление нового пользователя"):
            response = self.reqres.post(
                url='/api/users',
                json={
                    'name': name,
                    'job': job
                },
                cookies=token
            )
            attach.add_body_request(response)
            attach.add_curl(response)
            attach.add_response(response)
            return response

    def update_user(self, user_id, name, job, token) -> Response:
        with allure.step("Выполняем изменение данных пользователя"):
            response = self.reqres.patch(
                url=f'/api/users/{user_id}',
                json={
                    'name': name,
                    'job': job
                },
                cookies=token
            )
            attach.add_body_request(response)
            attach.add_curl(response)
            attach.add_response(response)
            return response


    def delete_user(self, user_id, token) -> Response:
        with allure.step("Выполняем удаление пользователя"):
            response = self.reqres.delete(f'/api/users/{user_id}', cookies=token)
            attach.add_curl(response)
            return response

