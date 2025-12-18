import requests
import json
from kame.auth import get_token   # si lo tienes separado

token = get_token()

tipo_documento = "GE"   # FACTURA ELECTRÓNICA (ejemplo)
numero_documento = 929 # Folio

url = f"https://api.kameone.cl/api/Documento/getVenta/{tipo_documento}/{numero_documento}"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print("STATUS:", response.status_code)
print("RAW RESPONSE:", repr(response.text))


