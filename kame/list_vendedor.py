import requests
from kame.auth import get_token
import json


token = get_token()

def list_vendedor():
    url = "https://api.kameone.cl/api/Maestro/getListVendedor"

    payload={}
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    

    data = json.loads(response.text)

    print(data)



