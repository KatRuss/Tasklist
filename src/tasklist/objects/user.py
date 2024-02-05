"""_summary_"""

from src.tasklist.login.encrypt import (
    caeser_decrypt,
    caeser_encrypt,
    get_key_from_string,
    get_key_string,
    generate_key,
)


class User:
    """Data Object for the user and their password data"""

    def __init__(self, full_name="", username="", password="") -> None:
        self.full_name: str = full_name
        self.username: str = username

        if password != "":
            self.set_password(password)

    def __str__(self) -> str:
        return self.full_name

    def set_name(self, new_name):
        """_summary_"""
        self.full_name = new_name

    def set_username(self, new_username):
        """_summary_"""
        self.username = new_username

    def set_password(self, password):
        """_summary_"""
        self.pass_key: str = get_key_string(generate_key(len(password)))
        self.password: str = caeser_encrypt(
            password, get_key_from_string(self.pass_key)
        )

    def get_name(self):
        """_summary_"""
        return self.full_name

    def get_username(self):
        """_summary_"""
        return self.username

    def get_password(self):
        """_summary_"""
        return caeser_decrypt(self.password, get_key_from_string(self.pass_key))

    def get_pass_key(self):
        """_Summary_"""
        return self.pass_key
