import atexit
from os import mkdir, path
from typing import Union, cast

import PySimpleGUI as sg

from event.main import Addition, EventManager, Items, Search
from jsonserde import json_to_data, writedata_to_file
from style.main import *


def app():
    while True:
        e, v = cast(tuple[main, dict[main, Union[str, list[str]]]], window())

        if e in (sg.WIN_CLOSED, main.exit_btn):
            break

        print(f"{e=}\n{v=}")

        manager.register(Search(window, e), Addition(window, memodata, e), Items(e))
        manager.notify_observers()

    window.close()


sg.theme("DarkGrey14")

if not path.isdir("data"):
    mkdir("data")

memodata_path = "data/memodata.json"

memodata = json_to_data(memodata_path)
items_lb_val = memodata.titles()

items_col_lay = [
    [sg.Image(**search_img), sg.In(**search_in), sg.Btn(**add_btn)],
    [sg.LB(items_lb_val, **items_listbox)],
]

window = sg.Window(
    title="PyMemoPad",
    layout=[
        [sg.Col(items_col_lay), sg.VSep()],
        [sg.Btn(**exit_btn)],
    ],
    size=(550, 550),
    disable_close=True,
)


manager = EventManager(window, memodata)


def cleanup():
    writedata_to_file(memodata_path, memodata)


atexit.register(cleanup)

app()
