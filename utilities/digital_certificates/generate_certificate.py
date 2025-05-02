from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from datetime import datetime, timedelta




def generate_certificate(user_name: str):
    # 1. Simulate CA root key (self-signed)
    ca_key = ec.generate_private_key(ec.SECP256R1())
    ca_name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, user_name),
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Tamil Nadu"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Chennai"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"IIT Madras"),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, u"ee21b128@smail.iitm.ac.in"),
    ])

    ca_cert = (
        x509.CertificateBuilder()
        .subject_name(ca_name)
        .issuer_name(ca_name)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
    )
    # Function to create a user certificate signed by CA
    def generate_user_cert(common_name: str):
        user_key = ec.generate_private_key(ec.SECP256R1())
        user_name = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ])

        user_csr = (
            x509.CertificateSigningRequestBuilder()
            .subject_name(user_name)
            .sign(user_key, hashes.SHA256())
        )

        user_cert = (
            x509.CertificateBuilder()
            .subject_name(user_csr.subject)
            .issuer_name(ca_cert.subject)
            .public_key(user_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.utcnow())
            .not_valid_after(datetime.utcnow() + timedelta(days=90))
            .sign(ca_key, hashes.SHA256())
        )

        return user_key, user_cert
    user_key, user_cert = generate_user_cert(user_name)
    
    # Save the user private key to a file
    with open(f"user_data/{user_name}_key.pem", "wb") as key_file:
        key_file.write(
            user_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    return user_key, user_cert