import requests
import os
from dotenv import load_dotenv
from cryptography import x509
from cryptography.hazmat.primitives import serialization
import json
# Load environment variables from .env file
load_dotenv()


def get_certificate(username:str):
    url = f"{os.getenv('API_BASE_URL')}/certificates/{username}"
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)
    
    cert_bytes:str = json.loads(response.text)["certBytes"]
    # Remove the "0x" prefix and convert the hex string back to bytes
    cert_bytes:str = bytes.fromhex(cert_bytes[2:])

    # Load the certificate from the DER-encoded bytes
    certificate = x509.load_der_x509_certificate(cert_bytes)

    return certificate