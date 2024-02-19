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
from pathlib import Path

import objects.screen as screens
import systems.task_system as tasks
import systems.user_system as users

parser = argparse.ArgumentParser(
    prog="tasklist",
    description="a central space for tasks and bugs on the command line!",
)
parser.add_argument("-n", "--new", dest="newUser", action="store_true")
args = parser.parse_args()

# Setup

# Get working directory and data paths
CWD = Path.cwd()
DATA_PATH = CWD.joinpath("src/tasklist/data")

# Load Tasks and Users
if args.newUser is False:
    users.read_users_from_yaml(DATA_PATH.joinpath("users.yaml"))
tasks.read_tasks_from_yaml(DATA_PATH.joinpath("tasks.yaml"))

# Login Check
if args.newUser is True:
    users.create_new_user()
    screens.entryScreen.show()
else:
    if users.validate_user() is False:
        # User has been validated, pass to main screen
        print("Login Success")
        # Send to main screen
        screens.entryScreen.show()
    else:
        # User not valid
        print("Login Fail")
