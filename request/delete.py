import requests
import json
from self import self
from config import *


class DeleteUser:
    def delete_user(self):
        response = requests.delete(f"{URL}//17", headers=HED)
        response_body=response.json()
        print(response_body)
        return response_body

DeleteUser.delete_user(self)
