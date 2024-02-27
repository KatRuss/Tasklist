"""
Entrypoint for the program. Takes in user login data and
passes it to the login system to interpret and log the user in.
"""

import os

import argparse


from t_consts import PATH_CONSTS
from src import screen, task, user

parser = argparse.ArgumentParser(
    prog="tasklist",
    description="a central space for tasks and bugs on the command line!",
)
parser.add_argument("-n", "--new", dest="newUser", action="store_true")
args = parser.parse_args()

# Setup
# Get working directory and data paths

# Load Tasks and Users
if args.newUser is False:
    user.read_users_from_yaml(PATH_CONSTS["USER_LIST"])
task.read_tasks_from_yaml(PATH_CONSTS["TASK_LIST"])

# Clear Screen before starting the app
os.system("cls" if os.name == "nt" else "clear")  # For both windows and linux support

# Login Check
if args.newUser is True:
    user.create_new_user()
    screen.entryScreen.show()
else:
    if user.validate_user() is not False:
        # User has been validated, pass to main screen
        print("Login Success")
        # Send to main screen
        screen.entryScreen.show()
    else:
        # User not valid
        print("Login Fail")
