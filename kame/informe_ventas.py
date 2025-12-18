import requests
import json
from kame.auth import get_token

token = get_token()

def list_unidad_negocio(mes):
    url = f"https://api.kameone.cl/api/Documento/getInformeVentas?page=1&per_page=100&fechaDesde={2024-01-01}&fechaHasta={2024-12-31}"

    payload={}
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"}


    response = requests.request("GET", url, headers=headers, data=payload)


    data = json.loads(response.text)

    print(data)