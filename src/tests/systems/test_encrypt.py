"""Encryption Unit Testing"""

from src import encrypt


def test_ceaser_full():
    """Tests all functionality of encript.py"""
    key_phrase = "Hello World"
    test_encript = ""
    test_key = []

    print("Generating Test Key")
    test_key = encrypt.generate_key()
    assert isinstance(test_key, bytes)

    print("Test Encrypyion Step")
    test_encript = encrypt.encrypt(key_phrase, test_key)
    assert isinstance(test_encript, bytes)
    assert test_encript != key_phrase

    print("Test Decryption Step")
    assert encrypt.decrypt(test_encript, test_key) == key_phrase
