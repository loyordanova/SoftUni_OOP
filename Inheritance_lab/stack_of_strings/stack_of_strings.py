from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


class AddStack(BaseStack):
    def push(self, element: str) -> None:
        self.data.append(element)


class RemoveStack(BaseStack):
    def pop(self) -> str:
        return self.data.pop()


class TopStack(BaseStack):
    def top(self):
        return self.data[-1]


class Stack(AddStack, RemoveStack, TopStack):
    pass