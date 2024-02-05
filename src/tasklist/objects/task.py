from typing import List
from dataclasses import dataclass, field
from src.tasklist.objects.user import User
from src.tasklist.formatting.markdown_format import (
    printH1,
    printBold,
    printUL,
    printH2,
    printItalic,
)


@dataclass
class Task:
    """_summary_"""

    name: str = "unamed task"
    priority: str = "?"
    description: str = None
    to_do: List[str] = field(default_factory=list)
    assigned_users: List[User] = field(default_factory=list)
    creation_date: str = None
    creator: User = None
    completion_date: str = None
    completed: bool = False

    def __str__(self) -> str:
        return f"{self.name} ({self.priority if self.completed is not False else 'Completed'})"

    def complete_task(self):
        self.completed = True

    def print_task_details(self):
        print(
            f"=== {self.name} ({self.priority if self.completed is not False else 'Completed'}) ===".center(
                16
            )
        )
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

    def get_markdown(self):
        return f"""
{printH1(self.name)}
{printBold(f'Priority: {self.priority}')}
{printItalic(f'Created by: {self.creator} on {self.creation_date}')}
{self.description}
{printH2('Todo')}
{printUL(self.to_do)}
{printH2('Assigned Users')}
{printUL(self.assigned_users)}
    """.strip()
