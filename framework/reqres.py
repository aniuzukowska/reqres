import os
from dotenv import load_dotenv
from requests import Response
from utils import attach
from utils.base_session import BaseSession

load_dotenv()


class Reqres:
    def __init__(self):
        self.reqres = BaseSession(base_url=os.getenv('api_url'))

    def login(self, login, password) -> Response:
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

    def create_user(self, name, job) -> Response:
        response = self.reqres.post(
            url='/api/users',
            json={
                'name': name,
                'job': job
            }
        )
        attach.add_body_request(response)
        attach.add_curl(response)
        attach.add_response(response)
        return response

    def update_user(self, user_id, name, job) -> Response:
        response = self.reqres.patch(
            url=f'/api/users/{user_id}',
            json={
                'name': name,
                'job': job
            }
        )
        attach.add_body_request(response)
        attach.add_curl(response)
        attach.add_response(response)
        return response


    def delete_user(self, user_id) -> Response:
        response = self.reqres.delete(f'/api/users/{user_id}')
        attach.add_curl(response)
        return response

