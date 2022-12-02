import allure
from allure_commons.types import Severity
from requests import Response
from pytest_voluptuous import S
from schemas.reqres import SchemaCreateUser
from utils import attach


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователями')
@allure.title('Добавление нового пользователя')
def test_create_user(reqres_session):
    with allure.step("Данные нового пользователя"):
        new_user = {'name': 'Anna Zukowska', 'job': 'QA'}
        attach.add_comment('Тестовые данные', f'{new_user}')

    with allure.step("Добавление нового пользователя"):
        result: Response = reqres_session.post(
            url='/api/users',
            json=new_user
    )

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
        attach.add_comment('Схема ответа: корректна', 'Все обязательные поля присутствуют, лишние поля отсусттвуют')





