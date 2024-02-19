""""""

import datetime
from typing import List
from dataclasses import dataclass, field

import yaml

import user
import u_input
import t_consts


@dataclass
class UpdateInfo:
    update_user: user.User = None
    creation_date: str = ""


@dataclass
class Task:
    """_summary_"""

    name: str = "unamed task"
    priority: str = "?"
    description: str = ""
    to_do: List[str] = field(default_factory=list)
    assigned_users: List[user.User] = field(default_factory=list)
    creator: UpdateInfo = field(default_factory=UpdateInfo)
    completion_date: str = ""
    completed: bool = False

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.priority if self.completed is False else 'Completed'})"
        )

    def complete_task(self):
        self.completed = True
        self.completion_date = datetime.datetime.now()

    def print_task_details(self) -> bool:
        header = f"=== {self.name}"
        header += f"({self.priority if self.completed is False else 'Completed'}) ==="
        print(header)
        print(f"created by: {self.creator.update_user} ({self.creator.creation_date})")
        print(self.description.center(16))
        print("Assigned To: ")
        if self.assigned_users != []:
            for u in self.assigned_users:
                print(u)
        else:
            print("No one")

        if self.to_do != []:
            print("--- To-Do ---".center(16))
            for item in self.to_do:
                print(f"- {item}")

        if self.completion_date != "":
            print(f"Completed: {self.completion_date}")

        return True


def get_task_from_yaml(item: dict) -> Task:
    return Task(
        name=item["title"],
        priority=item["priority"],
        description=item["description"],
        to_do=item["todo"],
        completed=item["completed"],
        completion_date=item["completed-date"],
        creator=UpdateInfo(item["creator"], item["created-date"]),
    )


def read_tasks_from_yaml(yaml_data: str):
    """_summary_

    Args:
        yamlData (str): _description_
    """
    with open(yaml_data, "r", encoding="utf8") as stream:
        data = yaml.safe_load(stream)
        if data is not None:
            for item in data:
                t_consts.task_list.append(get_task_from_yaml(item))


def write_task(task_object: Task, stream):
    stream.write("\n- \n")
    stream.write(f'  title: "{task_object.name}" \n')
    stream.write(f'  priority: "{task_object.priority}" \n')
    stream.write(f'  description: "{task_object.description}" \n')
    stream.write("  todo: \n")
    for task in task_object.to_do:
        stream.write(f'    - "{task}" \n')
    stream.write(f"  completed: {task_object.completed} \n")
    stream.write(f'  completed-date: "{task_object.completion_date}" \n')
    stream.write(f'  creator: "{task_object.creator.update_user}" \n')
    stream.write(f'  created-date: "{task_object.creator.creation_date}" \n')


def write_all_tasks_to_yaml(yaml_file: str, task_list):
    with open(yaml_file, "w", encoding="utf8") as stream:
        for task in task_list:
            write_task(task, stream)


def create_new_task():
    """_summary_"""
    task_title = u_input.typed_input("Name of New Task")
    task_description = u_input.typed_input("Task Description:")
    task_priority = u_input.list_choice_input("Task Priority", ["A", "B", "C", "D"])

    more_to_dos = True
    todos = []
    while more_to_dos:
        todos.append(u_input.typed_input("Add a todo"))
        more_to_dos = u_input.binary_choice_input("Would you like to add another todo?")

    new_task = Task(
        name=task_title,
        priority=task_priority,
        description=task_description,
        to_do=todos,
        creator=UpdateInfo(t_consts.CURRENT_USER, datetime.datetime.now()),
    )
    t_consts.task_list.append(new_task)
    write_all_tasks_to_yaml("data/tasks.yaml", t_consts.task_list)

    print("Task Successfully Created")
