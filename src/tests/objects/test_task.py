import datetime
from src.tasklist.objects.task import Task, UpdateInfo
from src.tasklist.objects.user import User

test_user = User(
    full_name="Katherine Russell",
    username="KatRuss",
)

test_task = Task(
    name="Do Cool Things",
    priority="A",
    description="Make a really cool app",
    to_do=["Plan the App", "Make the App", "Test the App"],
    assigned_users=[test_user],
    creator=UpdateInfo(user=test_user, creation_date=datetime.datetime.now()),
    completion_info=UpdateInfo(user=test_user, creation_date=datetime.datetime.now()),
    completed=True,
)


def test_task_info():
    assert test_task.print_task_details() is True


def test_complete_task():
    test_task.completion_info = None
    test_task.completed = False

    test_task.complete_task(test_user)

    assert test_task.completed is True
    assert isinstance(test_task.completion_info, UpdateInfo)
