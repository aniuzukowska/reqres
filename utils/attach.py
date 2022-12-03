import allure
import curlify
from requests import Response
import json


def add_curl(response: Response):
    curl_message = curlify.to_curl(response.request)
    allure.attach(
        body=curl_message.encode('utf-8'),
        name=f'CURL (status_code={response.status_code})',
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )


def add_body_request(response: Response):
    allure.attach(
        body=response.request.body,
        name='Request body',
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )


def add_response(response: Response):
    allure.attach(
        body=json.dumps(response.json(), indent=4),
        name=f'Response body (status_code={response.status_code})',
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )


def add_comment(name, body):
    allure.attach(
        body=body,
        name=name,
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )
