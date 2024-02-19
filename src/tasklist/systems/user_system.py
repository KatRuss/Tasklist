"""Handles both the data-handling of user classes. Both """

from __future__ import annotations
from pathlib import Path
import sys

import yaml
import data.datalists as data_lists
import systems.user_system as users


# ==========================
# === WRITE/READ SYSTEMS ===
# ==========================
def read_users_from_yaml(yaml_file: Path):
    """_summary_

    Args:
        yamlFile (str): _description_
    """

    with open(yaml_file, "r", encoding="utf8") as stream:

        data = yaml.safe_load(stream)
        if data is not None:
            data_lists.user_list.clear()  # Avoid Duplicate Data
            for item in data:
                new_user = users.User()
                new_user.full_name = item["name"]
                new_user.username = item["username"]
                new_user.password = item["password"]
                new_user.passKey = item["key"]
                data_lists.user_list.append(new_user)


def write_user_to_yaml(yaml_file: str, user: "users.User"):
    """_summary_

    Args:
        yamlFile (str): _description_
        user (User): _description_
    """

    with open(yaml_file, "a", encoding="utf8") as stream:

        stream.write("\n- \n")
        stream.write(f'  name: "{user.get_name()}" \n')
        stream.write(f'  username: "{user.get_username()}" \n')
        stream.write(f'  password: "{user.password}" \n')
        stream.write(f'  key: "{user.pass_key}" \n')
