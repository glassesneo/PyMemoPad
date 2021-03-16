from typing import Union, cast

import PySimpleGUI as sg

from event.addition import SwitchButton
from jsonserde import MemoData
from keys import addition
from style.addition import *


def addition_popup(md: MemoData):
    pass_pin_col_lay = [
        [sg.Text("password"), sg.In(**pass_in)],
        [sg.Text("confirm"), sg.In(**confirm_pass_in)],
    ]

    pass_pin_elem = sg.Col(pass_pin_col_lay, **pass_pin_col)
    w = sg.Window(
        title="add memo",
        layout=[
            [sg.Text("title:"), sg.In(**title_in)],
            [sg.Text("lock:"), sg.Btn(**on_btn), sg.Btn(**off_btn)],
            [sg.pin(pass_pin_elem)],
        ],
        size=(250, 150),
        return_keyboard_events=True,
        keep_on_top=True,
        disable_close=True,
        modal=True,
    )

    sb = SwitchButton(w)

    while True:
        e, v = cast(tuple[addition, dict[addition, Union[str, list[str]]]], w())

        if e in (sg.WIN_CLOSED,):
            break

        print(f"{e=}\n{v=}")

        w[addition.pass_col].update(visible=sb(e))

    w.close()
