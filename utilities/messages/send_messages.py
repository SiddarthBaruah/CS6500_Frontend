import requests
import os
from dotenv import load_dotenv
import json
# Load environment variables from .env file
load_dotenv()

def send_message(username:str, reciever:str, msg_data):
    url = f"{os.getenv('API_BASE_URL')}/messages/"
    data = {
        "sender": username,
        "receiver": reciever,
        "signedMessage": msg_data
    }
    headers = {
        "Content-Type": "application/json",
    }

    try:
        requests.post(url=url, json=data, headers=headers)
    except Exception as e:
        print(e)