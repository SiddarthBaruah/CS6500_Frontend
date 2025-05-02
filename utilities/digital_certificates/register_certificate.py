import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


def register_certificate(user_name:str,cert:str):
    url = f"{os.getenv('API_BASE_URL')}/certificates"
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "user": user_name,
        "certBytes": cert
    }

    response = requests.post(url, json=data, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    return response.text