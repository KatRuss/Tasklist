import input.user_input as u_input
import data.datalists as data_lists
import objects.task as tasks

import yaml


def get_task_from_yaml(item: dict) -> tasks.Task:
    return tasks.Task(
        name=item["title"],
        priority=item["priority"],
        description=item["description"],
        to_do=item["todo"],
        completed=item["completed"],
        completion_date=item["completed-date"],
        creator=tasks.UpdateInfo(item["creator"], item["created-date"]),
    )


def read_tasks_from_yaml(yaml_data: str):
    """_summary_

    Args:
        yamlData (str): _description_
    """
    with open(yaml_data, "r", encoding="utf8") as stream:
        data = yaml.safe_load(stream)
        for item in data:
            data_lists.task_list.append(get_task_from_yaml(item))


def write_task_to_yaml(yaml_file: str, task_object: tasks.Task):
    """_summary_

    Args:
        yamlFile (str): _description_
        taskObject (Task): _description_
    """
    with open(yaml_file, "a", encoding="utf8") as stream:
        stream.write("\n- \n")
        stream.write(f'  title: "{task_object.name}" \n')
        stream.write(f'  priority: "{task_object.priority}" \n')
        stream.write(f'  description: "{task_object.description}" \n')
        stream.write("  todo: \n")
        for task in task_object.to_do:
            stream.write(f'    - "{task}" \n')
        stream.write(f"  completed: {task_object.completed} \n")
        stream.write(f'  completed-date: "{task_object.completion_date}" \n')
        stream.write(f'  creator: "{task_object.creator.user}" \n')
        stream.write(f'  created-date: "{task_object.creator.creation_date}" \n')


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

    new_task = tasks.Task(
        name=task_title,
        priority=task_priority,
        description=task_description,
        to_do=todos,
    )
    write_task_to_yaml("tasks.yaml", new_task)
    data_lists.task_list.append(new_task)

    print("Task Successfully Created")
