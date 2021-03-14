from typing import cast

import PySimpleGUI as sg

from event import EventManager, SearchUI
from jsonserde import MemoData, json_to_data, writedata_to_file
from keys import keys
from style import *


def main():

    while True:
        event, values = cast(tuple[keys, dict[keys, str]], window())

        if event in (sg.WIN_CLOSED,):
            break

        print(event, values)
        manager.register(SearchUI())

        manager.notify_observers(event, values)

    window.close()
    # writedata_to_file(memodata_path, memodata)


memodata_path = "data/memodata.json"

menubar_lay = [
    ["Settings", "File"],
]

memodata = json_to_data(memodata_path)
items_lb_val = memodata.titles()

items_col_lay = [
    [sg.Image(**search_img), sg.In(**search_in)],
    [sg.LB(items_lb_val, **items_listbox)],
]

window = sg.Window(
    title="SimpleMemo",
    layout=[
        [sg.MenuBar(menubar_lay)],
        [sg.Col(items_col_lay), sg.VSep()],
    ],
    location=(400, 200),
    size=(500, 550),
)


manager = EventManager(window, memodata)


main()
