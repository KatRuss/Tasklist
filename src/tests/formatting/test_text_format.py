"""Tests for text_format.py, """

from t_format import get_title, get_error, get_question


def test_print_title():
    """Tests the title printing function"""
    assert get_title("My Application") == "=== My Application ==="


def test_print_question():
    """Tests the question printing function"""
    assert get_question("Would you like to save?") == "*Would you like to save?*"


def test_print_error():
    """Tests the question printing function"""
    assert get_error("no data was saved") == "!!!no data was saved!!!"
