import allure
from requests import Session
from utils import attach


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with allure.step(f'Выполнен запрос {method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            attach.add_body_request(response)
            attach.add_curl(response)
            attach.add_response(response)
            return response

