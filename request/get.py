import requests
from self import self
from config import *


class GetUsers:
    def get_users(self):
        response = requests.get(URL)
        response_body = response.json()
        print(response_body)
        return response_body


GetUsers.get_users(self)
