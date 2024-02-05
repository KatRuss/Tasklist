from src.tasklist.systems.user_system import write_user_to_yaml, read_users_from_yaml
from src.tasklist.objects.user import User
from pathlib import Path

Test_User = User(full_name="Katherine Russell", username="KatRus", password="Eillom")

CWD = Path(__file__).parent.absolute()


def test_write_user():
    # Create Test YAML File
    write_user_to_yaml(CWD.joinpath("temp.yaml"), Test_User)
