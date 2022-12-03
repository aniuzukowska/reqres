from requests import Response


class AuthSuccessful:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def token(self):
        return self.response.json()['token']


class AuthUnSuccessful:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code

    def error(self):
        return self.response.json()['error']

