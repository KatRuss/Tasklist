"""Module Containing the Screen Class and all instances that make up the app.
In this case including:
    - CurrentTaskScreen
    - EntryScreen
"""

from dataclasses import dataclass, field
from typing import List

import objects.screen_actions as screen_action
import input.user_input as u_input
import formatting.text_format as t_format
import data.datalists as data_list


@dataclass
class Screen:
    """_summary_"""

    title: str = "Untitled Screen"
    intro_message: str = "[Intro message]"
    exit_function: screen_action.ScreenAction = screen_action.QuitAppAction()
    options_list: List[screen_action.ScreenAction] = field(default_factory=list)

    def __str__(self) -> str:
        return self.title

    def exit_screen(self):
        self.exit_function()

    def get_option(self):
        # get list of options, then case switch depending on what you want to do
        full_list = self.options_list.copy()
        full_list.append(self.exit_function)

        choice = u_input.list_choice_input(
            question="What would you like to do?", answer_list=full_list
        )

        if choice is not None:
            return choice.do()

        pass  # Error handle

    def show(self):
        print(t_format.get_title(self.title))
        should_return = False
        while not should_return:
            print(f"You are currently at: {self.title}")
            should_return = self.get_option()


# ===============
# === SCREENS ===
# ===============
currentTasksScreen = Screen(
    title="Current Tasks",
    intro_message="Here are your current tasks",
    exit_function=screen_action.ReturnAction(),
    options_list=[
        screen_action.ViewTaskListAction(data_list.task_list),
        screen_action.ViewTaskAction(data_list.task_list),
        screen_action.AddTaskAction(),
    ],
)

entryScreen = Screen(
    title="Main Screen",
    intro_message="Welcome to Tasklist",
    options_list=[screen_action.MoveScreenAction(currentTasksScreen)],
)
