from src.tasklist.login.login_system import create_new_user, validate_user
from src.data.datalists import user_list
from src.tasklist.objects.user import User
from unittest.mock import patch

user_list.append(
    User(full_name="Katherine Russell", username="KatRuss", password="Eillom")
)


@patch("builtins.input")
def test_create_user_accepted(m_input):
    m_input.side_effect = ["y", "Jimbo", "aasL:EIFjk", "Jimmy Bobert"]
    result = create_new_user()
    assert result is not False
    assert isinstance(result, User)


@patch("builtins.input")
def test_create_user_bounced(m_input):
    m_input.side_effect = ["y", "KatRuss", "Eillom", "Katherine Russell"]
    result = create_new_user()
    assert result is False


@patch("builtins.input")
def test_login_accepted(m_input):
    m_input.side_effect = ["KatRuss", "Eillom"]
    result = validate_user()
    assert result is not False
    assert isinstance(result, User)


@patch("builtins.input")
def test_login_failed(m_input):
    m_input.side_effect = ["KatRuss", "asdwawdawwgfaswgf"]
    result = validate_user()
    assert result is False


@patch("builtins.input")
def test_login_error(m_input):
    m_input.side_effect = ["Jimbo", "asdwawdawwgfaswgf"]
    result = validate_user()
    assert result is False
