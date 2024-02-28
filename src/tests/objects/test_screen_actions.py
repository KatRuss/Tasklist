"""Scnree Action Object Unit Testing"""

from unittest.mock import patch

from src import screen, task, user


def test_screen_action_base():
    """Testing the bass functionality of the abstract ScreenAction Class"""
    s = screen.ScreenAction()
    assert str(s) == s.name
    assert s.do() is False


def test_return_action():
    """Test Return action returns true"""
    s = screen.ReturnAction()
    assert s.do() is True


def test_move_action(monkeypatch):
    """Tests move screen functionality"""
    t_screen = screen.Screen("TestPage", "Test", screen.ReturnAction(), [])
    s = screen.MoveScreenAction(t_screen)

    # Monkeypatch input to leave the screen when moved to it
    monkeypatch.setattr("builtins.input", lambda _: "1")

    assert s.name == f"Move to {t_screen}"
    assert s.do() is False


def test_vew_user_task_list(monkeypatch):
    """Tests that action only shows user tasks"""
    usr = user.User("Someone Out There")
    tasklist = [task.Task("Test1", assigned_users=[usr]), task.Task("Test2")]
    s = screen.ViewUserTaskListAction(tasklist)

    monkeypatch.setattr("builtins.input", lambda _: " ")

    assert s.do() is False


def test_view_all_tasks(monkeypatch):
    tasklist = [task.Task("Test1"), task.Task("Test2")]
    s = screen.ViewTaskListAction(tasklist)

    monkeypatch.setattr("builtins.input", lambda _: " ")

    assert s.do() is False


def test_view_task(monkeypatch):
    tasklist = [task.Task("Test1"), task.Task("Test2")]
    s = screen.ViewTaskAction(tasklist)

    monkeypatch.setattr("builtins.input", lambda _: "1")

    assert s.do() is False


@patch("builtins.input")
def test_add_task(m_input):
    s = screen.AddTaskAction()
    m_input.side_effect = ["test_task", "Test Task", "1", "TestTo-Do", "n"]

    assert s.do(write_to_file=False) is False


def test_complete_task(monkeypatch):
    tsklist = [task.Task()]
    s = screen.CompleteTask(tsklist)

    monkeypatch.setattr("builtins.input", lambda _: "1")

    assert s.do(write_to_file=False) is False
    assert tsklist[0].completed is True


def test_see_users(monkeypatch):
    users = [user.User()]
    s = screen.SeeUsers(user_list=users)

    monkeypatch.setattr("builtins.input", lambda _: " ")

    assert s.do() is False
