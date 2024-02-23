"""Login System Unit Testing"""

import os
from unittest.mock import patch
from src.user import create_new_user, validate_user, User
from src.t_consts import USER_LIST

USER_LIST.append(
    User(full_name="Katherine Russell", username="KatRuss", password="Eillom")
)

FILENAME = "tempfile.yaml"


@patch("builtins.input")
def test_create_user_accepted(m_input):
    m_input.side_effect = ["y", "Jimbo", "aasL:EIFjk", "Jimmy Bobert"]
    result = create_new_user(filepath=FILENAME)
    assert result is not False
    assert isinstance(result, User)


@patch("builtins.input")
def test_create_user_bounced(m_input):
    m_input.side_effect = ["y", "KatRuss", "Eillom", "Katherine Russell"]
    result = create_new_user(filepath=FILENAME)
    assert result is False
    os.remove(FILENAME)  # Remove file as no longer needed for testing


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
