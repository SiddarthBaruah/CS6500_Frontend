from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

def decrypt_message(encrypted_message:dict, chain_keys:list):
    iter= encrypted_message["iter"]
    if len(chain_keys)>=iter:
        chain_key = chain_keys[iter-2]
    else:
        prev= chain_keys[-1]
        while len(chain_keys)!=iter:
            hkdf_chain = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=f'chain key {iter}'.encode(),
            )
            ck = hkdf_chain.derive(prev)
            chain_keys.append(ck)
            prev = ck
        chain_key= chain_keys[-2]
    nonce= base64.b64decode(encrypted_message["nonce"])
    ciphertext= base64.b64decode(encrypted_message["ciphertext"])
    aesgcm = AESGCM(chain_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext,associated_data= None)
    return plaintext.decode("utf-8") , chain_keys

