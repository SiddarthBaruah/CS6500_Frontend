import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()
def get_all_users():
    url = f"{os.getenv('API_BASE_URL')}/certificates/"
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)
    
    #converting to list
    text= response.text
    text= text[1:-1].split(',')
    users= []
    for user in text:
        users.append(user[1:-1])
    return users