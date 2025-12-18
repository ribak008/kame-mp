import requests
import json
from kame.auth import get_token

token = get_token()

def get_pedido(numero_pedido):
    url = f"https://api.kameone.cl/api/Documento/getPedido/{numero_pedido}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    # print("STATUS:", response.status_code)
    # print("HEADERS:", response.headers)
    # print("RAW RESPONSE:", repr(response.text))

    data = json.loads(response.text)

    # print(data)
    # print(data["Total"])


    # productos = data["Detalle"]

    # for p in productos:
    #     print(p["Descripcion"], p["Cantidad"], p["Total"])

    print("Documento:", data["Documento"])
    print("Total:", data["Total"])
    print("Productos:")
    for p in data["Detalle"]:
        print(f"- {p['Descripcion']}: {p['Cantidad']} x {p['PrecioUnitario']} = {p['Total']}")
    
    

