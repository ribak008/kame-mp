import requests
import json
from kame.auth import get_token

token = get_token()

# def get_pedido_faltantes(numero_pedido):
#     url = f"https://api.kameone.cl/api/Documento/getPedido/{numero_pedido}"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {token}"
#     }

#     response = requests.get(url, headers=headers)



#     data = json.loads(response.text)


#     print("Documento:", data["Documento"])
#     print("Total:", data["Total"])
#     print("Productos:")
#     for p in data["Detalle"]:
#         if p["CantidadRecEnt"] is None or p["CantidadRecEnt"] == 'None':
#             cantidad_entregada = 0.0
#         else:
#             cantidad_entregada = float(p["CantidadRecEnt"])


#         if cantidad_entregada < p["Cantidad"]:
#             print(f"- {p['Descripcion']}: Cantidad Pedida: {p['Cantidad']}, Cantidad Entregada: {cantidad_entregada}, Faltantes: {p['Cantidad'] - cantidad_entregada}")
            

#     return data


def get_pedido_faltantes(numero_pedido):
    url = f"https://api.kameone.cl/api/Documento/getPedido/{numero_pedido}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token()}"
    }

    try:
        response = requests.get(url, headers=headers)
        
        # Verificar si la respuesta fue exitosa
        if response.status_code == 404:
            return {"error": f"Pedido {numero_pedido} no encontrado"}
        elif response.status_code != 200:
            return {"error": f"Error {response.status_code}: {response.text}"}
        
        data = response.json()
        
        # Verificar si hay datos válidos
        if not data or "Detalle" not in data:
            return {"error": "Pedido sin detalles"}

        productos = []
        
        for p in data["Detalle"]:
            pedida = float(p["Cantidad"])
            entregada = float(p["CantidadRecEnt"] or 0)
            faltantes = pedida - entregada

            if faltantes > 0:  
                productos.append({
                    "Producto": p["Descripcion"],
                    "Pedida": pedida,
                    "Entregada": entregada,
                    "Faltantes": faltantes
                })
        
        return {
            "Documento": data["Documento"],
            "Total": data["Total"],
            "Faltantes": productos
        }
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Error de conexión: {str(e)}"}
    except (KeyError, ValueError) as e:
        return {"error": f"Error al procesar datos: {str(e)}"}
