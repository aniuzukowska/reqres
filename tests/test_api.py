import os
import allure
import pytest
from allure_commons.types import Severity
from dotenv import load_dotenv
from requests import Response
from reqres_tests.requests.reqres import Reqres
from reqres_tests.responses.auth import AuthSuccessful, AuthUnSuccessful
from reqres_tests.responses.users import CreatedUser, UpdatedUser, DeletedUser

load_dotenv()
LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешная авторизация')
def test_login_successful():
    result = Reqres().login(LOGIN, PASSWORD)
    AuthSuccessful(result).assert_()


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Неуспешная авторизация (не указан пароль)')
def test_login_unsuccessful():
    result = Reqres().login(LOGIN, '')
    AuthUnSuccessful(result).assert_()


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Добавление нового пользователя')
@pytest.mark.parametrize(['name', 'job'], [('Anna Zukowska', 'QA'), ('Anna', '')])
def test_create_user(name, job):
    token = Reqres().get_token(LOGIN, PASSWORD)
    result = Reqres().create_user(name=name, job=job, token=token)
    CreatedUser(result).assert_(name, job)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Изменение данных пользователя')
def test_update_user():
    token = Reqres().get_token(LOGIN, PASSWORD)
    result = Reqres().update_user(user_id=2, name='Anna Zukowska', job='QA', token=token)
    UpdatedUser(result).assert_('Anna Zukowska', 'QA')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('API-тесты reqres.in')
@allure.story('Действия с пользователем')
@allure.title('Удаление пользователя')
def test_delete_user():
    token = Reqres().get_token(LOGIN, PASSWORD)
    result = Reqres().delete_user(user_id=2, token=token)
    DeletedUser(result).assert_()









