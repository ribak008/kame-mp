# import requests
# import time
# import json
# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Cargar variables de entorno desde .env
# load_dotenv()

# TOKEN_PATH = Path(__file__).parent / "token.json"

# CLIENT_ID = os.getenv("CLIENT_ID_L")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET_L")
# AUTH_URL = os.getenv("AUTH_URL", "https://api.kameone.cl/oauth/token")
# AUDIENCE = os.getenv("AUDIENCE", "https://api.kameone.cl/api")

# def token_file_for_client():
#     if not CLIENT_ID:
#         raise Exception("CLIENT_ID no definido")
#     return Path(__file__).parent / f"token_{CLIENT_ID[:8]}.json"



# def request_new_token():
#     payload = {
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "audience": AUDIENCE,
#         "grant_type": "client_credentials",
#     }

#     res = requests.post(AUTH_URL, json=payload)

#     if res.status_code != 200:
#         raise Exception(f"❌ Error obteniendo token nuevo: {res.text}")

#     data = res.json()

#     token_data = {
#         "access_token": data["access_token"],
#         "expires_at": time.time() + data["expires_in"],  # +24 Hrs
#     }

#     # crear token.json correctamente
#     with open(TOKEN_PATH, "w", encoding="utf-8") as f:
#         json.dump(token_data, f, indent=2)

#     print("🔄 Se generó un token nuevo y se guardó en token.json")

#     return token_data["access_token"]


# def get_token():
#     # Si token.json existe, tratar de leerlo
#     if TOKEN_PATH.exists():
#         try:
#             with open(TOKEN_PATH, "r", encoding="utf-8") as f:
#                 data = json.load(f)

#             # token todavía válido
#             if time.time() < data["expires_at"]:
#                 return data["access_token"]
#             else:
#                 print("⏳ Token expirado, generando uno nuevo…")
#         except Exception as e:
#             print("⚠ Error leyendo token.json, generando uno nuevo:", e)

#     # si no existe o hubo error → generar uno nuevo
#     return request_new_token()



import requests
import time
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = os.getenv("AUTH_URL", "https://api.kameone.cl/oauth/token")
AUDIENCE = os.getenv("AUDIENCE", "https://api.kameone.cl/api")


def token_file_for_client():
    if not CLIENT_ID:
        raise Exception("CLIENT_ID no definido")
    return Path(__file__).parent / f"token_{CLIENT_ID[:8]}.json"


def request_new_token():
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials",
    }

    res = requests.post(AUTH_URL, json=payload)

    if res.status_code != 200:
        raise Exception(f"❌ Error obteniendo token nuevo: {res.text}")

    data = res.json()

    token_data = {
        "access_token": data["access_token"],
        "expires_at": time.time() + data["expires_in"],
    }

    token_path = token_file_for_client()

    with open(token_path, "w", encoding="utf-8") as f:
        json.dump(token_data, f, indent=2)

    print(f"🔐 Token generado: {token_path.name}")

    return token_data["access_token"]


def get_token():
    token_path = token_file_for_client()

    if token_path.exists():
        try:
            with open(token_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if time.time() < data["expires_at"]:
                return data["access_token"]
            else:
                print("⏳ Token expirado, generando uno nuevo…")
        except Exception:
            print("⚠ Token corrupto, regenerando…")

    return request_new_token()