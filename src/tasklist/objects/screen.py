from dataclasses import dataclass, field
from typing import List
from src.tasklist.objects.screen_actions import ScreenAction, QuitAppAction
from src.tasklist.input.user_input import list_choice_input
from src.tasklist.formatting.text_format import get_title


@dataclass
class Screen:
    """_summary_"""

    title: str = "Untitled Screen"
    intro_message: str = "[Intro message]"
    exit_function: ScreenAction = QuitAppAction()
    options_list: List[ScreenAction] = field(default_factory=list)

    def __str__(self) -> str:
        return self.title

    def exit_screen(self):
        self.exit_function()

    def get_option(self):
        # get list of options, then case switch depending on what you want to do
        full_list: List[ScreenAction] = self.options_list.copy()
        full_list.append(self.exit_function)

        choice: ScreenAction = list_choice_input(
            question="What would you like to do?", answer_list=full_list
        )

        if choice is not None:
            return choice.do()

        pass  # Error handle

    def show(self):
        print(get_title(self.title))
        should_return = False
        while not should_return:
            print(f"You are currently at: {self.title}")
            should_return = self.get_option()
