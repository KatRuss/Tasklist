from src.tasklist.objects.screen import Screen
from src.tasklist.objects.screen_actions import (
    MoveScreenAction,
    ReturnAction,
    ViewTaskAction,
    ViewTaskListAction,
    AddTaskAction,
)
from src.data.datalists import task_list

currentTasksScreen = Screen(
    title="Current Tasks",
    intro_message="Here are your current tasks",
    exit_function=ReturnAction(),
    options_list=[
        ViewTaskListAction(task_list),
        ViewTaskAction(task_list),
        AddTaskAction(),
    ],
)

entryScreen = Screen(
    title="Main Screen",
    intro_message="Welcome to Tasklist",
    options_list=[MoveScreenAction(currentTasksScreen)],
)
