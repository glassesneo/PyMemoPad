from __future__ import annotations

from dataclasses import dataclass, field

import PySimpleGUI as sg
from jsonserde import MemoData
from keys import main
from popup import addition_popup

from .const import Observable, observables


@dataclass()
class Search:
    w: sg.Window
    e: main

    def update(self):
        if self.e == main.search_img:
            self.w[main.search_in].set_focus(True)


@dataclass()
class Addition:
    w: sg.Window
    md: MemoData
    e: main

    def update(self):
        if self.e == main.add_btn and addition_popup(self.md):
            self.w[main.items_lb].update(values=self.md.titles())


@dataclass()
class Items:
    e: main

    def update(self):
        if self.e == main.items_lb:
            ...


@dataclass()
class EventManager:
    window: sg.Window
    memodata: MemoData
    observers: observables = field(init=False)

    def __post_init__(self):
        self.observers = []

    def register(self, *observers: Observable) -> EventManager:
        self.observers += observers
        return self

    def unregister(self) -> EventManager:
        self.observers.clear()
        return self

    def notify_observers(self) -> EventManager:
        map(lambda o: o.update, self.observers)
        return self.unregister()
