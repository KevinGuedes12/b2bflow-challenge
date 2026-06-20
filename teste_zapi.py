import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = (
    f"https://api.z-api.io/instances/"
    f"{os.getenv('ZAPI_INSTANCE_ID')}"
    f"/token/{os.getenv('ZAPI_INSTANCE_TOKEN')}"
    "/send-text"
)

payload = {
    "phone": "5592994441097",
    "message": "Teste desafio b2bflow"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)