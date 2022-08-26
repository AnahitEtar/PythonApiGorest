import requests
import json
from self import self
from config import *


class UpdateUser:

    def update_user(self):
        mydata2 = open('../testdataput.json', "r").read()
        response = requests.put(f"{URL}//17", data=json.loads(mydata2), headers=HED)
        response_body = response.json()
        print(response_body)
        return response_body


UpdateUser.update_user(self)