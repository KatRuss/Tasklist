"""Handles the login and creations of users"""

import sys
import objects.user as users
import data.datalists as data_lists
import input.user_input as u_input


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

        for user in data_lists.user_list:
            if username == user.username:
                print(f"Username {username} already exists")
                return False

        new_user = users.User(full_name=name, username=username, password=password)
        users.write_user_to_yaml("users.yaml", new_user)
        return new_user

    return sys.exit()  # New user not created


def validate_user():
    """Checks if user credentials are correct and retuns user data."""

    # Get Username
    username = u_input.typed_input("Username", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])")
    # Get Password
    password = u_input.typed_input("Password:")

    for user in users.user_list:
        if username == user.username:
            # User has been found, check for for password
            print(user.get_password())
            if password == user.get_password():
                # User has been validated
                return user

            # wrong password
            print("Incorrect password")
            return False

    print(
        f"""User '{username}' was not found.
        If you are trying to create a new profile,
        Make sure to include '-n' in your console command"""
    )
    return False
