from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field

import PySimpleGUI as sg
from jsonserde import Memo, MemoData
from keys import addition
from style.const import green, grey, red


@dataclass()
class SwitchButtons:
    _w: sg.Window
    _btn: bool = field(default=False, init=False)

    def __call__(self, e: addition) -> bool:
        if e == addition.on_btn:
            self._w[e].update(button_color=green)
            self._w[addition.off_btn].update(button_color=grey)
            self._btn = True

        elif e == addition.off_btn:
            self._w[e].update(button_color=red)
            self._w[addition.on_btn].update(button_color=grey)
            self._btn = False

        return self._btn


def verify_title_is_valid(w: sg.Window, md: MemoData) -> bool:
    """Verify that title is valid."""
    is_valid = w[addition.title_in].get() not in md.titles()
    w[addition.error_col].update(visible=not is_valid)
    return is_valid


def datas_to_memo(v: dict[addition, str], lock: bool) -> Memo:
    title = v[addition.title_in]
    password = v[addition.pass_in] if lock else None
    date = dt.date.today()

    return Memo(title, lock, password, date.strftime("%Y%m%d"))
