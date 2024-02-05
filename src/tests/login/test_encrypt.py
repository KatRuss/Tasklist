"""_summary_"""

from src.tasklist.login.encrypt import (
    generate_key,
    get_key_from_string,
    get_key_string,
    caeser_encrypt,
    caeser_decrypt,
)

def test_ceaser_full():
    """Tests all functionality of encript.py"""
    key_phrase = "Hello World"
    test_encript = ""
    test_key = []

    print("Generating Test Key")
    test_key = generate_key(len(key_phrase))
    assert len(test_key) == len(key_phrase)
    assert isinstance(test_key, list)

    print("Test Encrypyion Step")
    test_encript = caeser_encrypt(key_phrase, test_key)
    assert len(test_encript) == len(key_phrase)
    assert isinstance(test_encript, str)
    assert test_encript != key_phrase

    print("Test Decryption Step")
    assert caeser_decrypt(test_encript,test_key) == key_phrase

    print("Key Access Tests")
    key_string = get_key_string(test_key)
    assert get_key_from_string(key_string) == test_key
