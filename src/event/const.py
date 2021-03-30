from typing import Protocol


class Observable(Protocol):
    def update(self):
        ...
