"""Handles getting inputs from the user in formatted blocks."""

from enum import Enum
import re
from formatting.text_format import get_question, get_error


class DefaultInputs(Enum):
    """Default yes/no inputs for the application"""

    YES = "y"
    NO = "n"


def wait():
    """A generic command to pause the application and wait for the user to continue.
    mainly to make reading large amounts of text easier."""
    input("**Press Enter to Continue**")
    print("---------------------------")


def print_question_and_response(
    question: str = "", positive: str = None, negative: str = None
):
    """internal function for printing the question and the user
    response in a standardised way.

    Args:
        question (_type_): The Question diaplayed to the user
    """
    question_txt = question
    question_txt += (
        f"({positive}/{negative})"
        if positive is not None and negative is not None
        else ""
    )
    get_question(question_txt)
    return input("> ".rjust(6))


def check_regex(response: str, validation: str = "") -> bool:
    """General Regex checker for typed inputs"""
    for char in response:
        print(char)
        if re.match(validation, char):
            print(get_error(f"Response includes illegal character '{char}'"))
            return False
    return True  # Nothing illegal was found


def typed_input(question: str = "", validation: str = ""):
    """Get a written input from the user that is returned as a string.
    Useful for things such as typing in passwords or creating names for
    new tasts, etc. Should be given in the format:

    "
    What name would you like to give this task?
        > [user input goes here]
    "
    ---
    Args:
        question (str): The question the player is presented with.
        validation (str): The regex string used to validate the data.
                            If validation = "", the validation step is ignored
    """
    answer = print_question_and_response(question)
    if answer.strip() != "":
        # Validation
        if validation != "":
            if check_regex(answer, validation):
                return answer
            return typed_input(question, validation)  # Validation Failed

        return answer  # validation skipped

    # User inputted nothing
    print("Please write a value.")
    return typed_input(question, validation)


def binary_choice_input(
    question: str = "",
    positive: str = DefaultInputs.YES.value,
    negative: str = DefaultInputs.NO.value,
):
    """get a yes/no choice input from the user. Should be given in the format:

    "
    Would you like to save this task? (y/n)
        >
    "

    Args:
        question (str, optional): The question displayed to the user.
        positive (str, optional): The char user presses to return True.
                                    Defaults to defaultInputs.YES. ('y')
        negative (str, optional): The char user presses to reutnr False.
                                    Defaults to defaultInputs.NO. ('n')
    """
    answer = print_question_and_response(question, positive, negative).strip()
    if answer == positive:
        return True
    if answer == negative:
        return False

    print(f"{answer} is not a valid answer")
    return binary_choice_input(question, positive, negative)


def list_choice_input(question: str, answer_list: list):
    """_summary_

    Args:
        question (str, optional): _description_. Defaults to "".
    """
    print(question)

    for x, answer in enumerate(answer_list):
        print(f"{x+1}. {answer}")
    choice = input("> ".rjust(6))

    if choice.isdigit() and int(choice) > 0 and int(choice) <= len(answer_list):
        return answer_list[int(choice) - 1]
    else:
        print(f"{choice} is not a valid choice")
        return list_choice_input(question, answer_list)
