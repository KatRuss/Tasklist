"""Module Containing the Screen Class and all instances that make up the app.
In this case including:
    - CurrentTaskScreen
    - EntryScreen
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List
import sys
import os

import task
import u_input
import t_format
import t_consts


@dataclass
class Screen:
    """_summary_"""

    title: str
    intro_message: str
    exit_function: "ScreenAction"
    options_list: List["ScreenAction"]

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
        should_return = False
        while not should_return:
            # Clear terminal for readability
            os.system(
                "cls" if os.name == "nt" else "clear"
            )  # For both windows and linux support

            # Print screen
            print(t_format.get_title(self.title))
            should_return = self.get_option()


# ====================
# == SCREEN ACTIONS ==
# ====================
class ScreenAction:
    name: str = "Unamed Screen Action"

    def __str__(self) -> str:
        return self.name

    def do(self):
        """Abstract function for initiating a ScreenAction

        Returns False if action is not expected to close the screen.
        Returns True if screen should close after action.
        """
        return False


class QuitAppAction(ScreenAction):
    name = "Quit"

    def do(self):
        task.write_all_tasks_to_yaml("data/tasks.yaml", t_consts.task_list)
        sys.exit()


class ReturnAction(ScreenAction):
    name = "Return"

    def do(self):
        return True


class MoveScreenAction(ScreenAction):
    def __init__(self, target) -> None:
        self.name = f"Move to {target}"
        self.target = target

    def do(self):
        self.target.show()
        return False


class ViewUserTaskListAction(ScreenAction):
    pass  # To Be Implemented


@dataclass
class ViewTaskListAction(ScreenAction):
    name = "View All Tasks"
    tasklist: list

    def do(self):
        if len(self.tasklist) != 0:
            print("Here are all of the tasks that exist: ")
            for x, tsk in enumerate(self.tasklist):
                print(f"  {x+1}. {tsk.name}")
            u_input.wait()
            return False

        print(t_format.get_error("There are no tasks to look at!"))
        u_input.wait()
        return False


@dataclass
class ViewTaskAction(ScreenAction):
    name = "View Specific Task"
    tasklist: list

    def do(self):
        if len(self.tasklist) != 0:
            choice = u_input.list_choice_input(
                "Which task would you like to view?", self.tasklist
            )
            choice.print_task_details()
            u_input.wait()
            return False

        print(t_format.get_error("There are no tasks to look at!"))
        u_input.wait()
        return False


class AddTaskAction(ScreenAction):
    name = "Add Task"

    def do(self):
        task.create_new_task()
        return False


class AssignTaskToUser(ScreenAction):
    name = "Assign Task to User"
    pass  # To be implemented


class RemoveAssignedUser(ScreenAction):
    name = "Remove User From Task"


@dataclass
class SeeUsers(ScreenAction):
    name = "See All Users"
    user_list: list

    def do(self):
        if len(self.user_list) != 0:
            print("Here all all of the users in this tasklist:")
            for x, usr in enumerate(self.user_list):
                print(f"{x+1}. {usr.full_name}")
            u_input.wait()
            return False

        print(t_format.get_error("There are no tasks to look at!"))
        u_input.wait()
        return False


@dataclass
class CompleteTask(ScreenAction):
    name = "Complete Task"

    tasklist: list

    def do(self):
        if len(self.tasklist) != 0:
            choice = u_input.list_choice_input(
                "Which task would you like to complete?", self.tasklist
            )
            choice.complete_task()
            print(f"{choice} has been set to completed")
            task.write_all_tasks_to_yaml("data/tasks.yaml", t_consts.task_list)
            u_input.wait()
            return False

        print(t_format.get_error("There are no tasks to look at!"))
        u_input.wait()
        return False


class admin_clear_tasklist(ScreenAction):
    name = "ADMIN Clear Tasklist"

    pass  # to be implemented


class admin_clear_userlist(ScreenAction):
    name = "ADMIN Clear Userlist"

    pass  # to be implemented


# =============
# == SCREENS ==
# =============
currentTasksScreen = Screen(
    title="Current Tasks",
    intro_message="Here are your current tasks",
    exit_function=ReturnAction(),
    options_list=[
        ViewTaskListAction(t_consts.task_list),
        ViewTaskAction(t_consts.task_list),
        CompleteTask(t_consts.task_list),
        AddTaskAction(),
    ],
)

adminScreen = Screen(
    title="Admin Screen",
    intro_message="Welcome to Admin Area",
    exit_function=ReturnAction(),
    options_list=[admin_clear_userlist(), admin_clear_tasklist()],
)

entryScreen = Screen(
    title="Main Screen",
    intro_message="Welcome to Tasklist",
    exit_function=QuitAppAction(),
    options_list=[
        MoveScreenAction(currentTasksScreen),
        MoveScreenAction(adminScreen),
        SeeUsers(t_consts.user_list),
    ],
)
