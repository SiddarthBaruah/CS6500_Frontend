from typing import Tuple
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from datetime import datetime, timedelta
from utilities.digital_certificates.register_certificate import register_certificate
from utilities.digital_certificates.register_private_key import register_private_key

def certificate_to_hex_string(certificate: x509.Certificate) -> str:
    cert_bytes = certificate.public_bytes(serialization.Encoding.DER)
    return "0x" + cert_bytes.hex()

def generate_and_register_certificate(user_name: str) -> Tuple[ec.EllipticCurvePrivateKey, x509.Certificate, str]:
    # CA root key (self-signed)
    ca_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(ec.SECP256R1())
    ca_name: x509.Name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, user_name),
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Tamil Nadu"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Chennai"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"IIT Madras"),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, u"ee21b128@smail.iitm.ac.in"),
    ])

    ca_cert: x509.Certificate = (
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

    def generate_user_cert(common_name: str) -> Tuple[ec.EllipticCurvePrivateKey, x509.Certificate]:
        user_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(ec.SECP256R1())
        user_name: x509.Name = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ])

        csr: x509.CertificateSigningRequest = (
            x509.CertificateSigningRequestBuilder()
            .subject_name(user_name)
            .sign(user_key, hashes.SHA256())
        )

        user_cert: x509.Certificate = (
            x509.CertificateBuilder()
            .subject_name(csr.subject)
            .issuer_name(ca_cert.subject)
            .public_key(user_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.utcnow())
            .not_valid_after(datetime.utcnow() + timedelta(days=90))
            .sign(ca_key, hashes.SHA256())
        )

        return user_key, user_cert

    # Generate user key and certificate
    user_key, user_cert = generate_user_cert(user_name)

    
    register_private_key(user_name=user_name, user_key=user_key)
    transactionHash= register_certificate(user_name=user_name, cert= certificate_to_hex_string(user_cert))

    return user_key, user_cert, transactionHash
