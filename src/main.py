from typing import Union, cast

import PySimpleGUI as sg

from event.main import Addition, EventManager, Items, Search
from jsonserde import MemoData, json_to_data, writedata_to_file
from style.main import *


def app():

    while True:
        e, v = cast(tuple[main, dict[main, Union[str, list[str]]]], window())

        if e in (sg.WIN_CLOSED,):
            break

        print(f"{e=}\n{v=}")

        manager.register(Search(window, e), Addition(memodata, e), Items(e))
        manager.notify_observers()

    window.close()
    # writedata_to_file(memodata_path, memodata)


sg.theme("DarkGrey14")

memodata_path = "data/memodata.json"


memodata = json_to_data(memodata_path)
items_lb_val = memodata.titles()

items_col_lay = [
    [sg.Image(**search_img), sg.In(**search_in), sg.Btn(**add_btn)],
    [sg.LB(items_lb_val, **items_listbox)],
]

window = sg.Window(
    title="SimpleMemo",
    layout=[
        [sg.Col(items_col_lay), sg.VSep()],
    ],
    size=(500, 550),
    disable_close=True,
)


manager = EventManager(window, memodata)


app()
