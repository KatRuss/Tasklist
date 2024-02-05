from dataclasses import dataclass
from src.tasklist.systems.task_system import create_new_task
from src.tasklist.input.user_input import wait, list_choice_input


class ScreenAction:
    name: str = "Unamed Screen Action"

    def __str__(self) -> str:
        return self.name

    def do(self):
        return False


class QuitAppAction(ScreenAction):
    name = "Quit"

    def do(self):
        quit()


class TestAction(ScreenAction):
    name = "Say hi"

    def do(self):
        print("Hello!")
        return False


class ReturnAction(ScreenAction):
    name = "Return"

    def do(self):
        return True


class MoveScreenAction(ScreenAction):
    def __init__(self, target) -> None:
        self.name = f"Move to {target}"
        self.target = target

    def do(self):
        self.target.Show()
        return False


class ViewUserTaskListAction(ScreenAction):
    pass


@dataclass
class ViewTaskListAction(ScreenAction):
    name = "View All Tasks"
    tasklist: list

    def do(self):
        print("Here are all of the tasks that exist: ")
        for x, task in enumerate(self.tasklist):
            print(f"  {x+1}. {task.name}")
        wait()
        return False


@dataclass
class ViewTaskAction(ScreenAction):
    name = "View Specific Task"
    tasklist: list

    def do(self):
        choice = list_choice_input("Which task would you like to view?", self.tasklist)
        choice.printTaskDetails()
        wait()
        return False


class AddTaskAction(ScreenAction):
    name = "Add Task"

    def do(self):
        create_new_task()
        return False
