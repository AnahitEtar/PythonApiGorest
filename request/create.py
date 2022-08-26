import requests
import json
from self import self
from config import *


class CreateUser:

    def create_user(self):
        mydata1 = open("../testdata.json", "r").read()
        response = requests.post(URL, data=json.loads(mydata1), headers=HED)
        response_body = response.json()
        print(response_body)
        return response_body


CreateUser.create_user(self)
