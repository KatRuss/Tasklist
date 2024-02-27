"""
Password encripytion for the purposes of of the pass_check system.
For the purposes of this assignemnt this will be in the form of a
caeser cypher to get the point across of these passwords being encrpyted when being saved.
"""

import random
import math

stringset = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789': ")


def generate_key(string_length: int) -> list:
    """Generated a key list of a given length"""
    key = []

    for _ in range(string_length):
        key.append(math.floor(random.randrange(1, len(stringset))))

    return key


def get_key_string(key: list) -> str:
    """Gets the key as a string"""
    key_string = ""

    for _, item in enumerate(key):
        key_string += stringset[item]

    return key_string


def get_key_from_string(string: str) -> list:
    """Creates a keylist from a string"""
    new_list = []
    for char in string:
        new_list.append(stringset.index(char))
    return new_list


def caeser_encrypt(text: str, key: list):
    """Encrypts text using a ceaser cypher"""
    new_text = ""
    split = list(text)

    for x, item in enumerate(split):
        position = stringset.index(item)
        for _ in range(key[x]):
            if position + 1 >= len(stringset):
                position = 0
            else:
                position += 1
        new_text += stringset[position]

    return new_text


def caeser_decrypt(text: str, key: list):
    """"""
    new_text = ""
    split = list(text)

    for x, item in enumerate(split):
        position = stringset.index(item)
        for _ in range(key[x]):
            if position - 1 <= 0:
                position = len(stringset)
            else:
                position -= 1
        new_text += stringset[position]
    return new_text
    # TODO: Find out what is causing the problem where passwords
    # are sometimes being decrypted with one letter wrong.
    # Possibly just rewrite this whole encryption system.
