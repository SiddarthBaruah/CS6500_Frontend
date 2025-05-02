from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def register_private_key(user_name:str, user_key: ec.EllipticCurvePrivateKey):
    # Save the user private key to a file
    key_path: str = f"user_data/{user_name}_key.pem"
    with open(key_path, "wb") as key_file:
        key_file.write(
            user_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )