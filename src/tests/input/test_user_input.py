from src.tasklist.input.user_input import (
    typed_input,
    wait,
    print_question_and_response,
    typed_input,
    binary_choice_input,
    list_choice_input,
    check_regex,
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
    monkeypatch.setattr("builtins.input", lambda _: "Hello Back")
    result = typed_input("Hello World", r".*[@_!#$%^&*()<>?/\|}{~:].*")
    assert result == "Hello Back"


def test_regex_fail():
    result = check_regex("Hello World<>", r".*[@_!#$%^&*()<>?/\|}{~:].*")
    assert result is False


def test_regex_pass():
    result = check_regex("Hello World", r".*[@_!#$%^&*()<>?/\|}{~:].*")
    assert result is True


def test_binary_choise_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    result = binary_choice_input("Hello World?")
    assert result is True


def test_binary_choise_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    result = binary_choice_input("Hello World?")
    assert result is False


def test_list_choise(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = list_choice_input("Hello World", ["option 1", "option 2"])
    assert result == "option 1"

    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = list_choice_input("Hello World", ["option 1", "option 2"])
    assert result == "option 2"
