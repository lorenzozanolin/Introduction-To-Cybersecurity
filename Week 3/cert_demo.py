#!/usr/bin/python3

from cryptography.hazmat.primitives.asymmetric import rsa  # for RSA functionalities
<<<<<<< HEAD
from cryptography.hazmat.primitives.asymmetric import ec  # for RSA functionalities
=======
>>>>>>> f31ca192c1326b42849f42449ae68b83dbde0b8a
from cryptography.hazmat.primitives import serialization  # for PEM encoding

from cryptography import x509  # for handling certificates
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes  # for hash functions

import datetime


# // Generates and saves public key and encrypted private key in specified files

def gen_key(pub_filename, priv_filename):
<<<<<<< HEAD
    #priv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)  # key size must be at least 2048
    priv_key = ec.generate_private_key(ec.SECP256R1())
=======
    priv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)  # key size must be at least 2048

>>>>>>> f31ca192c1326b42849f42449ae68b83dbde0b8a
    pub_key = priv_key.public_key()

    l = priv_key.key_size

    pem = priv_key.private_bytes(encoding=serialization.Encoding.PEM,
                                 format=serialization.PrivateFormat.PKCS8,
                                 encryption_algorithm=serialization.BestAvailableEncryption(
                                     b'secretpassword'))  # the private is encrypted using AES

    pem1 = pub_key.public_bytes(encoding=serialization.Encoding.PEM,
                                format=serialization.PublicFormat.SubjectPublicKeyInfo)  # extract public key bytes

    with open(pub_filename, 'wb') as pem_out:
        pem_out.write(pem1)

    with open(priv_filename, 'wb') as pem_out:
        pem_out.write(pem)

    return priv_key


# Generating a certificate signing request which is then sent to CA to obtain certificate
# inputs: private key and CSR filename
def gen_csr(key, csr_filename):
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IT"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Italy"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Udine"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Zano"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"zanolinlorenzo.com"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            # Describe what sites for which we want this certificate
            x509.DNSName(u"zanolinlorenzo.com"),
            x509.DNSName(u"www.zanolinlorenzo.com"),
            #x509.DNSName(u"subdomain.mysite.com"),
        ]),
        critical=False,
        # Sign the CSR with our private key.
    ).sign(key, hashes.SHA256())  # different hash function can be used here

    with open(csr_filename, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


# // issue a self signed certificate
# inputs:  private key and certificate file name
def issue_cert(key, cert_filename):
    # self signing means subject and issuer of the certificates are the same
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IT"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Italy"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Udine"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Zano"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"zanolinlorenzo.com"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(issuer).public_key(
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 30 days
        datetime.datetime.utcnow() + datetime.timedelta(days=30)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
        critical=False,
        # Sign our certificate with our private key
    ).sign(key, hashes.SHA256())

    with open(cert_filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def main():
    key = gen_key('rsa_pubkey.pem', 'rsa_privkey.pem')  # filename should have .pem extension

    gen_csr(key, "mycsr.pem")  # filename should have .pem extension

    issue_cert(key, "mycert.pem")  # filename should have .pem extension


if __name__ == "__main__":
    main()