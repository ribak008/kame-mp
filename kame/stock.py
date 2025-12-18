import requests
import json
from kame.auth import get_token

token = get_token()

def list_stock():

    url = "https://api.kameone.cl/api/Inventario/getStock"

    payload={}
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    
    data = json.loads(response.text)
    print(data)

