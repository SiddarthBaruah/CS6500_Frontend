from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def get_private_key(username:str) -> ec.EllipticCurvePrivateKey:
    # Adjust this to match how you named the file:
    key_path: str = f"user_data/{username}_key.pem"

    # 1. Read the PEM-encoded key bytes
    with open(key_path, "rb") as key_file:
        pem_data: bytes = key_file.read()

    # 2. Deserialize into an EllipticCurvePrivateKey
    private_key: ec.EllipticCurvePrivateKey = serialization.load_pem_private_key(
        pem_data,
        password=None  # Use a bytes password if you encrypted the key
    )
    return private_key

