"""_summary_"""

import yaml
from src.tasklist.objects.user import User
from src.data.datalists import user_list


def read_users_from_yaml(yaml_file: str):
    """_summary_

    Args:
        yamlFile (str): _description_
    """
    stream = open(yaml_file, "r", encoding="utf8")
    data = yaml.safe_load(stream)

    user_list.clear()  # Avoid Duplicate Data

    for item in data:
        new_user = User()
        new_user.full_name = item["name"]
        new_user.username = item["username"]
        new_user.password = item["password"]
        new_user.passKey = item["key"]
        user_list.append(new_user)

    stream.close()


def write_user_to_yaml(yaml_file: str, user: User):
    """_summary_

    Args:
        yamlFile (str): _description_
        user (User): _description_
    """
    stream = open(yaml_file, "a", encoding="utf8")

    stream.write("\n- \n")
    stream.write(f'  name: "{user.get_name()}" \n')
    stream.write(f'  username: "{user.get_username()}" \n')
    stream.write(f'  password: "{user.password}" \n')
    stream.write(f'  key: "{user.pass_key}" \n')

    stream.close()
