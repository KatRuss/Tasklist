from src.tasklist.systems.task_system import read_tasks_from_yaml, write_task_to_yaml, get_task_from_yaml
from src.tasklist.objects.task import Task,UpdateInfo
from src.tasklist.objects.user import User
from pathlib import Path
import yaml
import os
import time

test_task = Task(
    name = "Do things",
    priority = "A",
    description= "Make an App",
    creator=UpdateInfo(
        User(full_name="Katherine Rusell", username="KatRus"),
        creation_date="Test Date"
    )
)


CWD = Path(__file__).parent.absolute()
temp_file1 = CWD.joinpath("temp_tasks1.yaml")
temp_file2 = CWD.joinpath("temp_tasks2.yaml")


def test_write_task():
    # write temp file
    write_task_to_yaml(temp_file1,test_task)
    os.remove(temp_file1)

def test_read_task():
    # Read tempfile
    write_task_to_yaml(temp_file2,test_task)

    stream = open(temp_file2,'r')
    data = yaml.safe_load(stream)

    for item in data:
        result = get_task_from_yaml(item)
        assert isinstance(result,Task)

    stream.close()
    os.remove(temp_file2)
