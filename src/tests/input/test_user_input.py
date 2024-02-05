from src.tasklist.input.user_input import (
    typed_input,
    wait,
    print_question_and_response,
    typed_input,
    binary_choice_input,
    list_choice_input,
)


def test_wait(monkeypatch):
    """Tests Wait Input Command"""
    monkeypatch.setattr("builtins.input", lambda _: " ")
    wait()
    assert True


def test_question_and_response(monkeypatch):
    """sdf"""
    monkeypatch.setattr("builtins.input", lambda _: "Hello Back")
    assert print_question_and_response("Hello World") == "Hello Back"


def test_typed_input_pass(monkeypatch):
    # Base Version
    monkeypatch.setattr("builtins.input", lambda _: "Hello Back")
    assert typed_input("Hello World") == "Hello Back"


def test_typed_input_regex(monkeypatch):
    # Success Case
    monkeypatch.setattr("builtins.input", lambda _: "Hello Back")
    result = typed_input("Hello World", r"([.\[\]'<>!*@\/\\`,\"\';:#~{}=+_|?/])")
    assert result == "Hello Back"
