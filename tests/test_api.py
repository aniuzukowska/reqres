import allure
from allure_commons.types import Severity
from requests import Response
from pytest_voluptuous import S
from schemas.reqres import SchemaCreateUser, SchemaLoginUnsuccessful, SchemaLoginSuccessful, SchemaUpdateUser
from utils import attach


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешная авторизация')
def test_login_successful(reqres_session):
    with allure.step("Тестовые данные"):
        user_credential = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        attach.add_comment('Данные авторизации пользователя', f'{user_credential}')

    with allure.step("Выполнение авторизации"):
        result: Response = reqres_session.post(
            url='/api/login',
            json=user_credential
        )
        attach.add_body_request(result)
        attach.add_curl(result)
        attach.add_response(result)

    with allure.step("Проверяем результат"):
        assert result.status_code == 200
        attach.add_comment('Статус код ответа сервера: корректен',
                           f'Ожидаемый результат: 200, Фактический результат: {result.status_code}')
        assert result.json()['token'] == 'QpwL5tke4Pnpja7X4'
        attach.add_comment('Токен в ответе сервера: корректен',
                           f'Ожидаемый результат: "QpwL5tke4Pnpja7X4" , Фактический результат: "{result.json()["token"]}"')
        assert result.json() == S(SchemaLoginSuccessful)
        attach.add_comment('Схема ответа: корректна', 'Все обязательные поля присутствуют, лишние поля отсутствуют')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Неуспешная авторизация (не указан пароль)')
def test_login_unsuccessful(reqres_session):
    with allure.step("Тестовые данные"):
        user_email = {'email': 'peter@klaven'}
        attach.add_comment('Email пользователя', f'{user_email}')

    with allure.step("Попытка авторизации без пароля"):
        result: Response = reqres_session.post(
            url='/api/login',
            json=user_email
        )
        attach.add_body_request(result)
        attach.add_curl(result)
        attach.add_response(result)

    with allure.step("Проверяем результат"):
        assert result.status_code == 400
        attach.add_comment('Статус код ответа сервера: корректен',
                           f'Ожидаемый результат: 400, Фактический результат: {result.status_code}')
        assert result.json()['error'] == 'Missing password'
        attach.add_comment('Текст ошибки в ответе сервера: корректен',
                           f'Ожидаемый результат: "Missing password" , Фактический результат: "{result.json()["error"]}"')
        assert result.json() == S(SchemaLoginUnsuccessful)
        attach.add_comment('Схема ответа: корректна', 'Все обязательные поля присутствуют, лишние поля отсутствуют')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователями')
@allure.title('Добавление нового пользователя')
def test_create_user(reqres_session):
    with allure.step("Тестовые данные"):
        new_user = {'name': 'Anna Zukowska', 'job': 'QA'}
        attach.add_comment('Данные нового пользователя', f'{new_user}')

    with allure.step("Добавление нового пользователя"):
        result: Response = reqres_session.post(
            url='/api/users',
            json=new_user
    )
        attach.add_body_request(result)
        attach.add_curl(result)
        attach.add_response(result)

    with allure.step("Проверяем результат"):
        assert result.status_code == 201
        attach.add_comment('Статус код ответа сервера: корректен',
                           f'Ожидаемый результат: 201, Фактический результат: {result.status_code}')
        assert result.json()['name'] == new_user['name']
        attach.add_comment('Имя пользователя в ответе сервера: корректно',
                           f'Ожидаемый результат: {new_user["name"]}, Фактический результат: {result.json()["name"]}')
        assert result.json()['job'] == new_user['job']
        attach.add_comment('Наименование работы в ответе сервера: корректно',
                           f'Ожидаемый результат: {new_user["job"]}, Фактический результат: {result.json()["job"]}')
        assert result.json() == S(SchemaCreateUser)
        attach.add_comment('Схема ответа: корректна', 'Все обязательные поля присутствуют, лишние поля отсутствуют')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователями')
@allure.title('Изменение данных пользователя')
def test_update_patch_user(reqres_session):
    with allure.step("Тестовые данные"):
        user_id = 2
        new_data_for_user = {'name': 'Anna Zukowska', 'job': 'QA'}
        attach.add_comment(f'Новые данные пользователя c id={user_id}', f'{new_data_for_user}')

    with allure.step("Выполняем изменение данных пользователя"):
        result: Response = reqres_session.patch(
            url=f'/api/users/{user_id}',
            json=new_data_for_user
        )
        attach.add_body_request(result)
        attach.add_curl(result)
        attach.add_response(result)

    with allure.step("Проверяем результат"):
        assert result.status_code == 200
        attach.add_comment('Статус код ответа сервера: корректен',
                           f'Ожидаемый результат: 200, Фактический результат: {result.status_code}')
        assert result.json()['name'] == new_data_for_user['name']
        attach.add_comment('Имя пользователя в ответе сервера: корректно',
                           f'Ожидаемый результат: {new_data_for_user["name"]}, Фактический результат: {result.json()["name"]}')
        assert result.json()['job'] == new_data_for_user['job']
        attach.add_comment('Наименование работы в ответе сервера: корректно',
                           f'Ожидаемый результат: {new_data_for_user["job"]}, Фактический результат: {result.json()["job"]}')
        assert result.json() == S(SchemaUpdateUser)
        attach.add_comment('Схема ответа: корректна', 'Все обязательные поля присутствуют, лишние поля отсутствуют')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователями')
@allure.title('Удаление пользователя')
def test_delete_user(reqres_session):
    with allure.step("Тестовые данные"):
        user_id = 2
        attach.add_comment(f'Id пользователя', f'{user_id}')

    with allure.step("Выполняем удаление пользователя"):
        result: Response = reqres_session.delete(f'/api/users/{user_id}')
        attach.add_curl(result)

    with allure.step("Проверяем результат"):
        assert result.status_code == 204
        attach.add_comment('Статус код ответа сервера: корректен',
                           f'Ожидаемый результат: 204, Фактический результат: {result.status_code}')


