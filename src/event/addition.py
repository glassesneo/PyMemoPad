from __future__ import annotations

from dataclasses import dataclass, field

import PySimpleGUI as sg
from keys import addition
from style.const import green, grey, red, white_on


@dataclass()
class SwitchButton:
    w: sg.Window
    _button: bool = field(default=False, init=False)

    def __call__(self, e: addition) -> bool:
        if e == addition.on_btn:
            self.w[e].update(text="on", button_color=green)
            self.w[addition.off_btn].update(text="", button_color=grey)
            self._button = True

        elif e == addition.off_btn:
            self.w[e].update(text="off", button_color=red)
            self.w[addition.on_btn].update(text="", button_color=grey)
            self._button = False

        return self._button
