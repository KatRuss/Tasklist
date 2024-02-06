import datetime
from typing import List
from dataclasses import dataclass, field
from src.tasklist.objects.user import User


@dataclass
class UpdateInfo:
    user: User = None
    creation_date: str = ""


@dataclass
class Task:
    """_summary_"""

    name: str = "unamed task"
    priority: str = "?"
    description: str = None
    to_do: List[str] = field(default_factory=list)
    assigned_users: List[User] = field(default_factory=list)
    creator: UpdateInfo = None
    completion_info: UpdateInfo = None
    completed: bool = False

    def __str__(self) -> str:
        return f"{self.name} ({self.priority if self.completed is not False else 'Completed'})"

    def complete_task(self, user: User):
        self.completed = True
        self.completion_info = UpdateInfo(user, datetime.datetime.now())

    def print_task_details(self) -> bool:
        header = f"=== {self.name}"
        header += (
            f"({self.priority if self.completed is not False else 'Completed'}) ==="
        )
        print(header)
        print(self.description.center(16))
        print("Assigned To: ")
        if self.assigned_users != []:
            for user in self.assigned_users:
                print(user)
        else:
            print("No one")

        if self.to_do != []:
            print("--- To-Do ---".center(16))
            for item in self.to_do:
                print(f"- {item}")

        return True
