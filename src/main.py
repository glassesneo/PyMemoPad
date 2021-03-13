from typing import cast

import PySimpleGUI as sg

from event import EventManager
from jsonserde import MemoData, json_to_data, writedata_to_file
from keys import keys
from style import *


def main():

    while True:
        event, values = cast(tuple[keys, dict[keys, str]], window())

        if event in (sg.WIN_CLOSED,):
            break

        print(event, values)
        # manager.notify_observers(event, values)

    window.close()
    # writedata_to_file(memodata_path, memodata)


memodata_path = "data/memodata.json"

menubar_lay = [
    ["File", ["Save", ["Save as"], "Copy"]],
]

# 読み込んだメモ全てのタイトルをtupleで返す
memodata = json_to_data(memodata_path)
items_lb_val = memodata.titles()


window = sg.Window(
    title="SimpleMemo",
    layout=[[sg.Listbox(items_lb_val, **items_listbox)]],
    location=(400, 200),
    size=(450, 500),
)


manager = EventManager(window, memodata)


main()
