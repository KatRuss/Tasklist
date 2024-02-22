"""_summary_"""

import encrypt as encrypt


def test_ceaser_full():
    """Tests all functionality of encript.py"""
    key_phrase = "Hello World"
    test_encript = ""
    test_key = []

    print("Generating Test Key")
    test_key = encrypt.generate_key(len(key_phrase))
    assert len(test_key) == len(key_phrase)
    assert isinstance(test_key, list)

    print("Test Encrypyion Step")
    test_encript = encrypt.caeser_encrypt(key_phrase, test_key)
    assert len(test_encript) == len(key_phrase)
    assert isinstance(test_encript, str)
    assert test_encript != key_phrase

    print("Test Decryption Step")
    assert encrypt.caeser_decrypt(test_encript, test_key) == key_phrase

    print("Key Access Tests")
    key_string = encrypt.get_key_string(test_key)
    assert encrypt.get_key_from_string(key_string) == test_key
