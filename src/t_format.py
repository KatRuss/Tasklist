"""Helper methods for formatting text in the console."""


def get_title(message: str):
    """Prints 'message' as a page title"""
    return f"=== {message} ==="


def get_question(message: str):
    """Prints 'message' as a question"""
    return f"*{message}*"


def get_error(message: str):
    """Prints message as an error."""
    return f"!!!{message}!!!"
