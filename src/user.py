"""Module containing the class object for Users"""

from __future__ import annotations
from pathlib import Path
import sys

import yaml

import encrypt
import t_consts
import u_input
import t_format


class User:
    """Data Object for the user and their password data"""

    def __init__(self, full_name="", username="", password="") -> None:
        self.full_name: str = full_name
        self.username: str = username
        self.password: str = password
        self.pass_key: str = ""

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
        self.pass_key: str = encrypt.get_key_string(encrypt.generate_key(len(password)))
        self.password: str = encrypt.caeser_encrypt(
            password, encrypt.get_key_from_string(self.pass_key)
        )

    def get_name(self):
        """_summary_"""
        return self.full_name

    def get_username(self):
        """_summary_"""
        return self.username

    def get_password(self):
        """_summary_"""
        return encrypt.caeser_decrypt(
            self.password, encrypt.get_key_from_string(self.pass_key)
        )

    def get_pass_key(self):
        """_Summary_"""
        return self.pass_key


def read_users_from_yaml(yaml_file: Path):
    """_summary_

    Args:
        yamlFile (str): _description_
    """

    with open(yaml_file, "r", encoding="utf8") as stream:

        data = yaml.safe_load(stream)
        if data is not None:
            t_consts.user_list.clear()  # Avoid Duplicate Data
            for item in data:
                new_user = User()
                new_user.full_name = item["name"]
                new_user.username = item["username"]
                new_user.password = item["password"]
                new_user.pass_key = item["key"]
                t_consts.user_list.append(new_user)


def write_user_to_yaml(yaml_file: str, usr: User):
    """_summary_

    Args:
        yamlFile (str): _description_
        user (User): _description_
    """

    with open(yaml_file, "a", encoding="utf8") as stream:

        stream.write("\n- \n")
        stream.write(f'  name: "{usr.get_name()}" \n')
        stream.write(f'  username: "{usr.get_username()}" \n')
        stream.write(f'  password: "{usr.password}" \n')
        stream.write(f'  key: "{usr.pass_key}" \n')


def create_new_user() -> None:
    """_summary_

    Args:
        username (str): _description_
    """
    if u_input.binary_choice_input("Would you like to create a new profile?") is True:

        # Get Username
        username = u_input.typed_input(
            "New Username", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])"
        )
        # Get Password
        password = u_input.typed_input("New Password")
        # Get real name
        name = u_input.typed_input(
            "Please write your full name", r"([0-9.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])"
        )

        for user in t_consts.user_list:
            if username == user.username:
                print(f"Username {username} already exists")
                return False

        new_user = User(full_name=name, username=username, password=password)
        write_user_to_yaml("data/users.yaml", new_user)
        print(f"User {username} has been created. Welcome to Tasklists!")
        return new_user

    return sys.exit()  # New user not created


def validate_user():
    """Checks if user credentials are correct and retuns user data."""

    if len(t_consts.user_list) == 0:
        print(
            t_format.get_error(
                """There are no users inside this tasklist instance.
                To create the first user. Please include '-n' in your console command"""
            )
        )
        sys.exit()

    # Get Username
    username = u_input.typed_input("Username", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])")
    # Get Password
    password = u_input.typed_input("Password:")

    for user in t_consts.user_list:
        if username == user.username:
            # User has been found, check for for password
            print(user.get_password())
            if password == user.get_password():
                # User has been validated
                t_consts.CURRENT_USER = user
                return user

            # wrong password
            print("Incorrect password")
            return False

    print(
        t_format.get_error(
            f"""User '{username}' was not found.
            If you are trying to create a new profile,
            Make sure to include '-n' in your console command"""
        )
    )
    return False
