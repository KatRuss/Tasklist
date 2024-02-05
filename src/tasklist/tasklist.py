"""
-- TASKLIST.PY --
Entrypoint for the program. Takes in user login data and 
passes it to the login system to interpret and log the user in.

Linearly it should go:
1. Take user login info
2. Check is info is valid
3. Take info and pass user onto the main screen of the app
"""

import argparse
import src.tasklist.login.login_system as login_system
from src.data.screens import entryScreen
from src.tasklist.systems.task_system import read_tasks_from_yaml
from src.tasklist.systems.user_system import read_users_from_yaml

parser = argparse.ArgumentParser(
    prog="tasklist",
    description="a central space for tasks and bugs on the command line!",
)
parser.add_argument("-n", "--new", dest="newUser", action="store_true")
args = parser.parse_args()

# Setup
if args.newUser is False:
    read_users_from_yaml("users.yaml")
read_tasks_from_yaml("tasks.yaml")

# Login Check
if args.newUser is True:
    login_system.create_new_user()
    entryScreen.show()
else:
    if login_system.validate_user() is False:
        # User has been validated, pass to main screen
        print("Login Success")
        # Send to main screen
        entryScreen.show()
    else:
        # User not valid
        print("Login Fail")
