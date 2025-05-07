import requests
import os
from dotenv import load_dotenv
import json
# Load environment variables from .env file
load_dotenv()

def retrieve_messages(prime_user, friend):
    url =  f"{os.getenv('API_BASE_URL')}/messages/1"
    headers = {
        "Content-Type": "application/json",
    }
    sender_msg_url = {
		"sender": prime_user,
		"receiver": friend
	}
    reciever_msg_url = {
		"sender": friend,
		"receiver": prime_user
	}
    try:
        sender_msges=  json.loads(requests.get(url=url, json= sender_msg_url, headers=headers).text)
        reciever_msges= json.loads(requests.get(url=url, json= reciever_msg_url, headers=headers).text)
        return sender_msges, reciever_msges
    except Exception as e:
        print(e)

