from __future__ import annotations

from dataclasses import dataclass, field

import PySimpleGUI as sg
from jsonserde import MemoData
from keys import main
from popup import addition_popup

from .const import Observable, observables


@dataclass()
class Search:
    win: sg.Window
    e: main

    def update(self):
        if self.e == main.search_img:
            self.win[main.search_in].set_focus(True)


@dataclass()
class Addition:
    md: MemoData
    e: main

    def update(self):
        if self.e == main.add_btn:
            addition_popup(self.md)


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
    p_observers: observables = field(default_factory=observables)

    def __post_init__(self):
        self.observers = []

    def register(self, *observers: Observable) -> EventManager:
        self.observers += observers
        return self

    def unregister(self) -> EventManager:
        self.observers.clear()
        self.observers += self.p_observers
        return self

    def permanent_register(self, *observers: Observable) -> EventManager:
        self.observers += observers
        self.p_observers += observers
        return self

    def notify_observers(self) -> EventManager:
        for o in self.observers:
            o.update()
        return self.unregister()
