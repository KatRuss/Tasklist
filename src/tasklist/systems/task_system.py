from src.tasklist.input.user_input import (
    typed_input,
    list_choice_input,
    binary_choice_input,
)
from src.data.datalists import task_list
from src.tasklist.objects.task import Task,UpdateInfo
import yaml


def get_task_from_yaml(item: dict) -> Task:
    return Task(
                name=item["title"],
                priority=item["priority"],
                description=item["description"],
                to_do=item["todo"],
                completed=item["completed"],
                completion_date = item["completed-date"],
                creator=UpdateInfo(item["creator"],item["created-date"])
            )

def read_tasks_from_yaml(yamlData: str):
    """_summary_

    Args:
        yamlData (str): _description_
    """
    stream = open(yamlData, "r")
    data = yaml.safe_load(stream)

    for item in data:
        task_list.append(get_task_from_yaml(item))

    stream.close()


def write_task_to_yaml(yamlFile: str, taskObject: Task):
    """_summary_

    Args:
        yamlFile (str): _description_
        taskObject (Task): _description_
    """
    stream = open(yamlFile, "a")

    stream.write("\n- \n")
    stream.write(f'  title: "{taskObject.name}" \n')
    stream.write(f'  priority: "{taskObject.priority}" \n')
    stream.write(f'  description: "{taskObject.description}" \n')
    stream.write("  todo: \n")
    for task in taskObject.to_do:
        stream.write(f'    - "{task}" \n')
    stream.write(f"  completed: {taskObject.completed} \n")
    stream.write(f'  completed-date: "{taskObject.completion_date}" \n')
    stream.write(f'  creator: "{taskObject.creator.user}" \n')
    stream.write(f'  created-date: "{taskObject.creator.creation_date}" \n')

    stream.close()


def create_new_task():
    taskTitle = typed_input("Name of New Task")
    taskDescription = typed_input("Task Description:")
    taskPriority = list_choice_input("Task Priority", ["A", "B", "C", "D"])

    MoreToDos = True
    todos = []
    while MoreToDos:
        todos.append(typed_input("Add a todo"))
        MoreToDos = binary_choice_input("Would you like to add another todo?")

    newTask = Task(
        name=taskTitle, priority=taskPriority, description=taskDescription, to_do=todos
    )
    write_task_to_yaml("tasks.yaml", newTask)
    task_list.append(newTask)

    print("Task Successfully Created")
