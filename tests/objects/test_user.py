from src.tasklist.objects.user import User


def test_user_creation():
    name = "Katherine Russell"
    username = "Katruss"
    passw = "Eillom"

    test_user = User(full_name=name, username=username, password=passw)

    assert test_user.get_name() == name
    assert test_user.get_username() == username
    assert test_user.get_password() == passw


def test_user_setters():
    name = "Katherine Russell"
    username = "Katruss"
    passw = "Eillom"

    test_user = User()
    test_user.set_name(name)
    test_user.set_username(username)
    test_user.set_password(passw)

    assert test_user.get_name() == name
    assert test_user.get_username() == username
    assert test_user.get_password() == passw
