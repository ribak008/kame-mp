import requests
import json
from kame.auth import get_token

token = get_token()

def get_pedido_faltantes(numero_pedido):
    url = f"https://api.kameone.cl/api/Documento/getPedido/{numero_pedido}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)



    data = json.loads(response.text)


    print("Documento:", data["Documento"])
    print("Total:", data["Total"])
    print("Productos:")
    for p in data["Detalle"]:
        if p["CantidadRecEnt"] is None or p["CantidadRecEnt"] == 'None':
            cantidad_entregada = 0.0
        else:
            cantidad_entregada = float(p["CantidadRecEnt"])


        if cantidad_entregada < p["Cantidad"]:
            print(f"- {p['Descripcion']}: Cantidad Pedida: {p['Cantidad']}, Cantidad Entregada: {cantidad_entregada}, Faltantes: {p['Cantidad'] - cantidad_entregada}")
            

    return data
