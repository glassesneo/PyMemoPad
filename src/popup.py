from typing import cast

import PySimpleGUI as sg

from event.addition import SwitchButtons, datas_to_memo, verify_title_is_valid
from jsonserde import MemoData
from keys import addition
from style.addition import *


def addition_popup(md: MemoData) -> bool:
    result = False
    pass_pin_col_lay = [
        [sg.Txt(**pass_txt), sg.In(**pass_in)],
        [sg.Check(**pass_check)],
    ]
    pass_pin_elem = sg.Col(pass_pin_col_lay, **pass_pin_col)

    error_pin_col_lay = [
        [sg.Txt(**error_txt)],
    ]
    error_pin_elem = sg.Col(error_pin_col_lay, **error_pin_col)

    w = sg.Window(
        title="add memo",
        layout=[
            [sg.Txt("title:"), sg.In(**title_in)],
            [sg.Txt("lock:"), sg.Btn(**on_btn), sg.Btn(**off_btn)],
            [sg.pin(pass_pin_elem)],
            [sg.pin(error_pin_elem)],
            [sg.Cancel(**cancel_btn), sg.OK(**ok_btn)],
        ],
        size=(255, 160),
        keep_on_top=True,
        disable_close=True,
        modal=True,
    )

    sb = SwitchButtons(w)

    while True:
        e, v = cast(tuple[addition, dict[addition, str]], w())

        if e in (sg.WIN_CLOSED, addition.cancel_btn):
            break

        lock = sb(e)

        w[addition.pass_col].update(visible=lock)

        char = "" if w[addition.pass_check].get() else "*"

        w[addition.pass_in].update(password_char=char)

        if e == addition.ok_btn:
            if verify_title_is_valid(w, md):
                md.memos.append(datas_to_memo(v, lock))
                result = True
                break

    w.close()
    return result
