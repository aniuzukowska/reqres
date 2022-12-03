from requests import Response


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


class DeletedUser:
    def __init__(self, response: Response):
        self.response = response

    def status_code(self):
        return self.response.status_code

