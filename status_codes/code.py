import json
import requests
from self import self

from config import *


class StatusCode:
    def status_code_400(self):
        mydata1 = open("../testdata1.json", "r").read()
        response = requests.put(f"{URL}//23", data=json.loads(mydata1), headers=HED)
        response_body = response.json()
        print(response_body)
        return response_body

    def status_code_401(self):
        mydata1 = open("../testdata1.json", "r").read()
        response = requests.post(URL, data=json.loads(mydata1))
        response_body = response.json()
        print(response_body)
        return response_body

    def status_code_404(self):
        mydata2 = open('../testdataput.json', "r").read()
        response = requests.delete(f"{URL}//190", data=json.loads(mydata2), headers=HED)
        response_body = response.json()
        print(response_body)
        return response_body

    def status_code_422(self):
        mydata1 = open("../testdata.json", "r").read()
        response = requests.post(URL, data=json.loads(mydata1), headers=HED)
        response_body = response.json()
        print(response_body)
        return response_body


StatusCode.status_code_400(self)
StatusCode.status_code_401(self)
StatusCode.status_code_404(self)
StatusCode.status_code_422(self)