"""
-- LOGIN_SYSTEM.py --
handles taking in user login data and validating the information. Allowing the user to login.
"""

from src.tasklist.input.user_input import binary_choice_input, typed_input
from src.tasklist.objects.user import User
from src.data.datalists import user_list
from src.tasklist.systems.user_system import write_user_to_yaml


def create_new_user() -> None:
    """_summary_

    Args:
        username (str): _description_
    """
    if binary_choice_input("Would you like to create a new profile?") is True:

        # Get Username
        username = typed_input("New Username", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])")
        # Get Password
        password = typed_input("New Password")
        # Get real name
        name = typed_input(
            "Please write your full name", r"([0-9.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])"
        )

        for user in user_list:
            if username == user.username:
                print(f"Username {username} already exists")
                return False

        new_user = User(full_name=name, username=username, password=password)
        write_user_to_yaml("users.yaml", new_user)
        return new_user

    exit()  # New user not created


def validate_user() -> User:
    """Checks if user credentials are correct and retuns user data."""

    # Get Username
    username = typed_input("Username", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])")
    # Get Password
    password = typed_input("Password:")

    for user in user_list:
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
