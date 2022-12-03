import os
import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from requests import Response
from pytest_voluptuous import S
from schemas.reqres_schemas import SchemaCreateUser, SchemaLoginUnsuccessful, SchemaLoginSuccessful, SchemaUpdateUser
from utils import attach
from model.users import CreatedUser, UpdatedUser, DeletedUser
from model.auth import AuthSuccessful, AuthUnSuccessful
from framework.reqres import Reqres


load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
TOKEN = os.getenv('token')


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешная авторизация')
def test_login_successful():
    with allure.step("Тестовые данные"):
        attach.add_comment('Данные авторизации пользователя', f' Логин: {LOGIN}')

    with allure.step("Выполнение авторизации"):
        result: Response = Reqres().login(LOGIN, PASSWORD)
        auth = AuthSuccessful(result)

    with allure.step("Проверяем результат"):
        with allure.step('Проверка статус-кода ответа сервера'):
            assert auth.status_code() == 200
        with allure.step('Проверка токена пользователя в ответе сервера'):
            assert auth.token() == TOKEN
        with allure.step('Проверка схемы ответа сервера'):
            assert auth.json == S(SchemaLoginSuccessful)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Неуспешная авторизация (не указан пароль)')
def test_login_unsuccessful():
    with allure.step("Тестовые данные"):
        attach.add_comment('Данные авторизации пользователя', f' Логин: {LOGIN}')

    with allure.step("Выполнение авторизации"):
        result: Response = Reqres().login(LOGIN, '')
        auth = AuthUnSuccessful(result)

    with allure.step("Проверяем результат"):
        with allure.step('Проверка статус-кода ответа сервера'):
            assert auth.status_code() == 400
        with allure.step('Проверка токена пользователя в ответе сервера'):
            assert auth.error() == 'Missing password'
        with allure.step('Проверка схемы ответа сервера'):
            assert auth.json == S(SchemaLoginUnsuccessful)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Добавление нового пользователя')
def test_create_user():
    with allure.step("Тестовые данные"):
        new_user_name = 'Anna Zukowska'
        new_user_job = 'QA'
        attach.add_comment('Данные нового пользователя', f'name = "{new_user_name}", job = "{new_user_job}"')

    with allure.step("Добавление нового пользователя"):
        result: Response = Reqres().create_user(new_user_name, new_user_job)
        created_user = CreatedUser(result)

    with allure.step('Проверка результата'):
        with allure.step('Проверка статус-кода ответа сервера'):
            assert created_user.status_code() == 201
        with allure.step('Проверка имени пользователя в ответе сервера'):
            assert created_user.name() == new_user_name
        with allure.step('Проверка наименования работы в ответе сервера'):
            assert created_user.job() == new_user_job
        with allure.step('Проверка схемы ответа сервера'):
            assert created_user.json == S(SchemaCreateUser)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Изменение данных пользователя')
def test_update_user():
    with allure.step("Тестовые данные"):
        user_id = 2
        new_name = 'Anna Zukowska'
        new_job = 'QA'
        attach.add_comment(f'Новые данные для пользователя c id={user_id}', f'name = "{new_name}", job = "{new_job}"')

    with allure.step("Выполняем изменение данных пользователя"):
        result: Response = Reqres().update_user(user_id, new_name, new_job)
        updated_user = UpdatedUser(result)

    with allure.step("Проверяем результат"):
        with allure.step('Проверка статус-кода ответа сервера'):
            assert updated_user.status_code() == 200
        with allure.step('Проверка имени пользователя в ответе сервера'):
            assert updated_user.name() == new_name
        with allure.step('Проверка наименования работы в ответе сервера'):
            assert updated_user.job() == new_job
        with allure.step('Проверка схемы ответа сервера'):
            assert updated_user.json == S(SchemaUpdateUser)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Удаление пользователя')
def test_delete_user():
    with allure.step("Тестовые данные"):
        user_id = 2
        attach.add_comment(f'Id пользователя', f'{user_id}')

    with allure.step("Выполняем удаление пользователя"):
        result: Response = Reqres().delete_user(user_id)
        deleted_user = DeletedUser(result)

    with allure.step("Проверяем результат"):
        with allure.step('Проверка статус-кода ответа сервера'):
            assert deleted_user.status_code() == 204



