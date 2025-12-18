import requests
import json
from kame.auth import get_token

token = get_token()

def list_unidad_negocio():
    url = "https://api.kameone.cl/api/Maestro/getListUnidadNegocio"

    payload={}
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"}


    response = requests.request("GET", url, headers=headers, data=payload)


    data = json.loads(response.text)

    print(data)