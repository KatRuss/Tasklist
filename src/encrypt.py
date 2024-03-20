"""
Password encripytion for the purposes of of the pass_check system.
"""

import base64
import cryptography.fernet as cypt


# Old Verison. Change later
def generate_key() -> bytes:
    """Generated a key list of a given length"""
    key = cypt.Fernet.generate_key()
    print(key)
    return key


def encrypt(text: str, key: bytes):
    """Encrypts texts with Fernet"""
    print(key)
    f = cypt.Fernet(key)
    new_text = f.encrypt(text.encode())
    return new_text


def decrypt(text: bytes, key: bytes):
    "Decrypt texts with Fernet"

    f = cypt.Fernet(key)
    new_text = f.decrypt(text).decode()
    return new_text
