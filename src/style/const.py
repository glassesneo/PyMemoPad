from typing import Any

from PySimpleGUI import Element

args = dict[str, Any]


def widget_args(**kwargs: Any) -> args:
    return kwargs


grey = "grey"

green = "green"

red = "red"


def white_on(color: str) -> str:
    return f"white on {color}"
