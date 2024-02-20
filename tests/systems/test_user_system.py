from pathlib import Path
import os
from src.user import write_user_to_yaml, User


Test_User = User(full_name="Katherine Russell", username="KatRus", password="Eillom")

CWD = Path(__file__).parent.absolute()
temp_file = CWD.joinpath("temp.yaml")


def test_write_user():
    # Create Test YAML File
    write_user_to_yaml(temp_file, Test_User)
    os.remove(temp_file)


def test_read_user():
    pass
