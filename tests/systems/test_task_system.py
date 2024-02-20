from pathlib import Path
import os
import yaml
from src.task import (
    get_task_from_yaml,
    Task,
    UpdateInfo,
)
from src.user import User

test_task = Task(
    name="Do things",
    priority="A",
    description="Make an App",
    creator=UpdateInfo(
        User(full_name="Katherine Rusell", username="KatRus"), creation_date="Test Date"
    ),
)


CWD = Path(__file__).parent.absolute()
temp_file1 = CWD.joinpath("temp_tasks1.yaml")
temp_file2 = CWD.joinpath("temp_tasks2.yaml")


def test_write_task():  # TODO: Re-write this to use write_all_tasks instead
    # write temp file
    # write_task_to_yaml(temp_file1, test_task)
    os.remove(temp_file1)


def test_read_task():
    # Read tempfile
    # write_task_to_yaml(temp_file2, test_task)

    stream = open(temp_file2, "r")
    data = yaml.safe_load(stream)

    for item in data:
        result = get_task_from_yaml(item)
        assert isinstance(result, Task)

    stream.close()
    os.remove(temp_file2)
