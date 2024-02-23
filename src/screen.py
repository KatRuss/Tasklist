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

from src import task, u_input, t_consts, t_format


@dataclass
class Screen:
    """Dataclass for a UI screen"""

    title: str
    intro_message: str
    exit_function: "ScreenAction"
    options_list: List["ScreenAction"]

    def __str__(self) -> str:
        return self.title

    def exit_screen(self):
        """Auto runs the exit function so the user can leave the screen or application"""
        self.exit_function()

    def get_option(self):
        """Asks user what they want to do, then runs the"""
        # get list of options, then case switch depending on what you want to do
        full_list = self.options_list.copy()
        full_list.append(self.exit_function)

        choice = u_input.list_choice_input(
            question="What would you like to do?", answer_list=full_list
        )

        if choice is not None:
            return choice.do()

        # Error handle
        print(
            t_format.get_error(
                "Error, choice was not valid. Select something else please"
            )
        )
        return self.get_option()

    def show(self):
        """Presents the screen to the user"""
        should_return = False
        while not should_return:
            # Clear terminal for readability
            os.system(
                "cls" if os.name == "nt" else "clear"
            )  # For both windows and linux support

            # Print screen
            print(t_format.get_title(self.title))
            print(self.intro_message)
            # All screen actions returns a bool, depending on if it should close the screen or not
            should_return = self.get_option()


# ====================
# == SCREEN ACTIONS ==
# ====================
class ScreenAction:
    """Abstract class object for a ScreenAction.
    Meant to be"""

    name: str = "Unamed Screen Action"

    def __str__(self) -> str:
        return self.name

    def do(self):
        """Abstract function for initiating a ScreenAction.
        Needs to be implemented on all inhereted classes

        Returns False if action is not expected to close the screen.
        Returns True if screen should close after action.
        """
        return False


class QuitAppAction(ScreenAction):
    """Action to quit the application"""

    name = "Quit"

    def do(self):
        task.write_all_tasks_to_yaml("data/tasks.yaml", t_consts.TASK_LIST)
        sys.exit()


class ReturnAction(ScreenAction):
    """Action to close the screen and return to the previous action"""

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


@dataclass
class ViewUserTaskListAction(ScreenAction):
    name = "View Your Tasks"
    tasklist: list

    def do(self):
        print("Here are the tasks assigned to you: ")
        # TODO: Implement list of assigned tasks
        for x, tsk in enumerate(self.tasklist):
            has_user = t_consts.CURRENT_USER in tsk.assigned_users
            if has_user and tsk.completed is False:
                print(f"{x}. {tsk}")

        u_input.wait()
        return False


@dataclass
class ViewTaskListAction(ScreenAction):
    name = "View All Tasks"
    tasklist: list

    def do(self):
        if len(self.tasklist) != 0:
            print("Here are all of the tasks that exist: ")
            for x, tsk in enumerate(self.tasklist):
                print(f"  {x+1}. {tsk}")
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


@dataclass
class AssignTaskToUser(ScreenAction):
    name = "Assign Task to User"
    user_list: list
    task_list: list

    def do(self):
        if len(self.user_list) == 0:
            print(t_format.get_error("No users detected on this instance"))
            u_input.wait()
            return False
        if len(self.user_list) == 0:
            print(t_format.get_error("No users detected on this instance"))
            u_input.wait()

        # get task
        usr = u_input.list_choice_input(
            "Which user would you like to assign", self.user_list
        )

        tsk = u_input.list_choice_input(
            f"Which task would you like to assign {usr.username} to?", self.task_list
        )
        tsk.assigned_users.append(usr)
        print(f"{usr.username} has been set to {tsk.name}!")

        return False


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
            task.write_all_tasks_to_yaml("data/tasks.yaml", t_consts.TASK_LIST)
            u_input.wait()
            return False

        print(t_format.get_error("There are no tasks to look at!"))
        u_input.wait()
        return False


class AdminClearTasklist(ScreenAction):
    name = "ADMIN Clear Tasklist"

    def do(self):
        print(
            "WARNING: THIS WILL CLEAR ALL TASKS ON THIS TASKLIST. THIS ACTION IS NOT REVERSABLE"
        )
        if u_input.binary_choice_input("Are you sure you want to continue?"):
            # delete everything
            t_consts.TASK_LIST.clear()
            print("All tasks have now been deleted!")
            task.write_all_tasks_to_yaml("data/tasks.yaml", t_consts.TASK_LIST)
            u_input.wait()

<<<<<<< HEAD
        return False
=======
        return False  # user said no
>>>>>>> 888d16ed707005dd440b25ba6b8a08cfcfd13b77


class AdminClearUserlist(ScreenAction):
    name = "ADMIN Clear Userlist"

    def do(self):
        print(
            "WARNING: THIS WILL CLEAR ALL USERS ON THIS TASKLIST. THIS ACTION IS NOT REVERSABLE"
        )
        if u_input.binary_choice_input("Are you sure you want to continue?"):
            # delete everything
            t_consts.USER_LIST.clear()
            # Add current user back into the list
            t_consts.USER_LIST.append(t_consts.CURRENT_USER)
            print("All users have now been deleted!")
            u_input.wait()

<<<<<<< HEAD
        return False
=======
        return False  # user said no
>>>>>>> 888d16ed707005dd440b25ba6b8a08cfcfd13b77


# =============
# == SCREENS ==
# =============
currentTasksScreen = Screen(
    title="Current Tasks",
    intro_message="Here are your current tasks",
    exit_function=ReturnAction(),
    options_list=[
        ViewTaskListAction(t_consts.TASK_LIST),
        ViewTaskAction(t_consts.TASK_LIST),
        CompleteTask(t_consts.TASK_LIST),
        AssignTaskToUser(t_consts.USER_LIST, t_consts.TASK_LIST),
        AddTaskAction(),
    ],
)

adminScreen = Screen(
    title="Admin Screen",
    intro_message="Welcome to Admin Area",
    exit_function=ReturnAction(),
    options_list=[AdminClearUserlist(), AdminClearTasklist()],
)

entryScreen = Screen(
    title="Main Screen",
    intro_message="Welcome to Tasklist",
    exit_function=QuitAppAction(),
    options_list=[
        MoveScreenAction(currentTasksScreen),
        MoveScreenAction(adminScreen),
        SeeUsers(t_consts.USER_LIST),
    ],
)
