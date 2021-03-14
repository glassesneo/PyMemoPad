from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import PySimpleGUI as sg

from jsonserde import MemoData
from keys import keys


class Observable(Protocol):
    def update(self, win: sg.Window, md: MemoData, e: keys, v: dict[keys, str]):
        ...


@dataclass()
class SearchUI:
    def update(self, win: sg.Window, md: MemoData, e: keys, v: dict[keys, str]):
        if e == keys.search_img:
            win[keys.search_in].set_focus(True)


@dataclass()
class ItemsUI:
    def update(self, win: sg.Window, md: MemoData, e: keys, v: dict[keys, str]):
        if e == keys.items_lb:
            ...


@dataclass()
class EventManager:
    window: sg.Window
    memodata: MemoData
    observers: list[Observable] = field(default_factory=list[Observable], init=False)

    def register(self, observer: Observable) -> EventManager:
        self.observers.append(observer)
        return self

    def unregister(self, observer: Observable) -> EventManager:
        self.observers.remove(observer)
        return self

    def notify_observers(self, e: keys, v: dict[keys, str]) -> EventManager:
        for o in self.observers:
            o.update(self.window, self.memodata, e, v)

        return self
