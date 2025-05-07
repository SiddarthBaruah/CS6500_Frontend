from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

def encrypt_message(msg: str, aes_key: bytes, iter: int):
    # generate a random 96-bit nonce
    nonce = os.urandom(12)
    aesgcm = AESGCM(aes_key)
    ciphertext = aesgcm.encrypt(nonce, msg.encode("utf-8"), associated_data=None)

    # Base64-encode the raw bytes so they become JSON-safe strings
    b64_ct = base64.b64encode(ciphertext).decode("utf-8")
    b64_nonce = base64.b64encode(nonce).decode("utf-8")

    return {
        "ciphertext": b64_ct,
        "nonce": b64_nonce,
        "iter": iter
    }
